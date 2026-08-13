# app.py - Sistema de Propostas Comerciais
# Casa do Frentista / GP Company

import streamlit as st
import json
import os
from datetime import datetime, timedelta
from typing import List
import pandas as pd

from data import (
    TANQUES, BACIAS, BOMBAS, FILTROS, ELEMENTOS, OPCIONAIS,
    EMPRESA, VENDEDORES_INICIAL, TEMPLATES, UFS_BRASIL,
    UF_ORIGEM_PADRAO, calcular_difal,
    get_imagem_tanque, get_imagens_selecionadas,
)
from pdf_generator import gerar_pdf, format_brl
from storage import (
    proximo_numero_cotacao, salvar_proposta,
    listar_propostas, carregar_proposta,
)

# ==================== CONFIG ====================
st.set_page_config(
    page_title="Casa do Frentista | Propostas",
    page_icon="⛽",
    layout="wide",
    initial_sidebar_state="expanded",
)

VENDEDORES_FILE = os.path.join(os.path.dirname(__file__), "vendedores.json")


def carregar_vendedores() -> List[str]:
    if os.path.exists(VENDEDORES_FILE):
        try:
            with open(VENDEDORES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return VENDEDORES_INICIAL.copy()


def salvar_vendedores(lista: List[str]):
    with open(VENDEDORES_FILE, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


# ==================== SIDEBAR - CONFIGURAÇÕES ====================
with st.sidebar:
    st.image("logo_casa.png", width=180)
    st.markdown("### Configurações")

    # Gestão de vendedores
    with st.expander("👥 Vendedores", expanded=False):
        vendedores = carregar_vendedores()
        novo_vendedor = st.text_input("Adicionar vendedor", key="novo_vend")
        if st.button("Adicionar") and novo_vendedor.strip():
            if novo_vendedor.strip() not in vendedores:
                vendedores.append(novo_vendedor.strip())
                salvar_vendedores(vendedores)
                st.success(f"Adicionado: {novo_vendedor}")
                st.rerun()
        remover = st.selectbox("Remover vendedor", ["—"] + vendedores, key="rem_vend")
        if st.button("Remover") and remover != "—":
            vendedores = [v for v in vendedores if v != remover]
            salvar_vendedores(vendedores)
            st.success(f"Removido: {remover}")
            st.rerun()
        st.caption("Lista atual: " + ", ".join(vendedores) if vendedores else "Nenhum")

    st.markdown("---")
    st.caption(f"{EMPRESA['nome']} · GP Company")
    st.caption(EMPRESA["cidade"])


# ==================== TÍTULO ====================
st.title("⛽ Proposta Comercial – Tanques Aéreos")
st.markdown(f"**{EMPRESA['nome']}** · Equipamentos **GP Company**")
st.markdown("---")

# ==================== TEMPLATE + HISTÓRICO ====================
col_tpl, col_hist = st.columns(2)
with col_tpl:
    template_nome = st.selectbox("Template rápido", list(TEMPLATES.keys()))
    template = TEMPLATES.get(template_nome)
with col_hist:
    propostas = listar_propostas()
    opcoes_hist = ["— Nova proposta —"] + [
        f"{p['numero']} | {p['cliente'][:30]} | {p['salvo_em'][:10]}"
        for p in propostas[:30]
    ]
    escolha_hist = st.selectbox("Carregar / duplicar proposta salva", opcoes_hist)
    proposta_carregada = None
    if escolha_hist != "— Nova proposta —" and propostas:
        idx = opcoes_hist.index(escolha_hist) - 1
        if 0 <= idx < len(propostas):
            proposta_carregada = carregar_proposta(propostas[idx]["path"])
            if proposta_carregada:
                st.caption("Proposta carregada — revise os campos e gere um **novo** número ao salvar.")

# Defaults a partir do template ou histórico
_def = {}
if proposta_carregada:
    _def = proposta_carregada
elif template:
    _def = {"_template": template}

# ==================== DADOS DO CLIENTE ====================
st.subheader("1. Dados do Cliente")
col1, col2, col3 = st.columns(3)

_cli = (_def.get("cliente") or {}) if proposta_carregada else {}
_cot = (_def.get("cotacao") or {}) if proposta_carregada else {}

with col1:
    razao_social = st.text_input("Razão Social *", value=_cli.get("razao_social", "") if _cli.get("razao_social") != "—" else "")
    cnpj = st.text_input("CNPJ", value=_cli.get("cnpj", "") if _cli.get("cnpj") != "—" else "")
    contato = st.text_input("A/c (Contato)", value=_cli.get("contato", "") if _cli.get("contato") != "—" else "")

with col2:
    endereco = st.text_input("Endereço / Cidade", value=_cli.get("endereco", "") if _cli.get("endereco") != "—" else "")
    telefone = st.text_input("Telefone", value=_cli.get("telefone", "") if _cli.get("telefone") != "—" else "")
    email = st.text_input("E-mail", value=_cli.get("email", "") if _cli.get("email") != "—" else "")
    uf_origem = st.selectbox(
        "UF origem (ICMS)",
        UFS_BRASIL,
        index=UFS_BRASIL.index(UF_ORIGEM_PADRAO) if UF_ORIGEM_PADRAO in UFS_BRASIL else UFS_BRASIL.index("SC"),
        help="Padrão: SC (fábrica). Altere se a saída fiscal for de outro estado.",
    )
    uf_destino = st.selectbox(
        "UF destino (DIFAL/ICMS)",
        ["—"] + UFS_BRASIL,
        index=0,
    )

with col3:
    vendedores = carregar_vendedores()
    vend_default = _cot.get("vendedor") if _cot.get("vendedor") in vendedores else (vendedores[0] if vendedores else "—")
    vendedor = st.selectbox(
        "Agente de Vendas *",
        vendedores if vendedores else ["—"],
        index=(vendedores.index(vend_default) if vend_default in vendedores else 0),
    )
    if "numero_auto" not in st.session_state:
        st.session_state.numero_auto = proximo_numero_cotacao()
    if st.button("Gerar novo nº de cotação"):
        st.session_state.numero_auto = proximo_numero_cotacao()
        st.rerun()
    numero_cotacao = st.text_input("Nº da Cotação *", value=st.session_state.numero_auto)
    data_cotacao = st.date_input("Data", value=datetime.now())
    validade_dias = st.number_input("Validade (dias)", min_value=1, max_value=60, value=7)
    data_validade_fim = data_cotacao + timedelta(days=int(validade_dias))
    st.caption(f"Válido até **{data_validade_fim.strftime('%d/%m/%Y')}**")


# ==================== SELEÇÃO DE PRODUTOS ====================
st.subheader("2. Seleção de Produtos")

def _idx(options, key, fallback=0):
    try:
        return list(options).index(key)
    except (ValueError, AttributeError):
        return fallback

# Preferência: template > padrão
_tpl = template or {}
_tk = _tpl.get("tanque", "10.000L")
_bk = _tpl.get("bacia", "10.000L")
_bok = _tpl.get("bomba", "SEM BOMBA")
_fk = _tpl.get("filtro", "SEM FILTRO")
_ek = _tpl.get("elemento", "SEM ELEMENTO")

col_t, col_b = st.columns(2)

with col_t:
    tanque_key = st.selectbox(
        "Tanque Aéreo",
        options=list(TANQUES.keys()),
        index=_idx(TANQUES.keys(), _tk, list(TANQUES.keys()).index("10.000L") if "10.000L" in TANQUES else 0),
    )
    tinfo = TANQUES[tanque_key]
    st.caption(f"Ø {tinfo['diametro']} · Comp. {tinfo['comprimento']} · Chapa {tinfo['chapa']} · {tinfo['peso']} kg")
    # key muda com a seleção → preço atualiza automaticamente
    preco_tanque = st.number_input(
        "Preço Tanque (R$)",
        value=float(tinfo["preco"]),
        min_value=0.0,
        step=10.0,
        key=f"p_tanque_{tanque_key}",
    )

with col_b:
    bacia_key = st.selectbox(
        "Bacia de Contenção",
        options=list(BACIAS.keys()),
        index=_idx(BACIAS.keys(), _bk, list(BACIAS.keys()).index("10.000L") if "10.000L" in BACIAS else 0),
    )
    binfo = BACIAS[bacia_key]
    if bacia_key != "SEM BACIA":
        st.caption(f"L {binfo['largura']} · A {binfo['altura']} · C {binfo['comprimento']} · {binfo['peso']} kg")
    else:
        st.caption("Sem bacia de contenção")
    preco_bacia = st.number_input(
        "Preço Bacia (R$)",
        value=float(binfo["preco"]),
        min_value=0.0,
        step=10.0,
        key=f"p_bacia_{bacia_key}",
    )

col_bo, col_f, col_e = st.columns(3)

with col_bo:
    bomba_key = st.selectbox("Bomba de Abastecimento", options=list(BOMBAS.keys()), index=_idx(BOMBAS.keys(), _bok, 0))
    preco_bomba = st.number_input(
        "Preço Bomba (R$)",
        value=float(BOMBAS[bomba_key]),
        min_value=0.0,
        step=10.0,
        key=f"p_bomba_{bomba_key}",
    )

with col_f:
    filtro_key = st.selectbox("Filtro", options=list(FILTROS.keys()), index=_idx(FILTROS.keys(), _fk, 0))
    preco_filtro = st.number_input(
        "Preço Filtro (R$)",
        value=float(FILTROS[filtro_key]),
        min_value=0.0,
        step=10.0,
        key=f"p_filtro_{filtro_key}",
    )

with col_e:
    elemento_key = st.selectbox("Elemento Filtrante", options=list(ELEMENTOS.keys()), index=_idx(ELEMENTOS.keys(), _ek, 0))
    preco_elemento = st.number_input(
        "Preço Elemento (R$)",
        value=float(ELEMENTOS[elemento_key]),
        min_value=0.0,
        step=10.0,
        key=f"p_elem_{elemento_key}",
    )

# ==================== PRODUTOS OPCIONAIS (checkbox) ====================
st.markdown("**Produtos opcionais**")
st.caption("Marque os itens que deseja incluir no orçamento. O preço pode ser ajustado.")

opcionais_selecionados = {}  # nome -> preco final
if OPCIONAIS:
    for nome_op, info_op in OPCIONAIS.items():
        col_ck, col_pr, col_ds = st.columns([2, 1, 3])
        with col_ck:
            marcado = st.checkbox(nome_op, value=False, key=f"opt_{nome_op}")
        with col_pr:
            preco_op = st.number_input(
                "R$",
                value=float(info_op.get("preco", 0)),
                min_value=0.0,
                step=50.0,
                key=f"opt_preco_{nome_op}",
                label_visibility="collapsed",
            )
        with col_ds:
            if info_op.get("descricao"):
                st.caption(info_op["descricao"])
            # Mini preview da foto do opcional (se existir)
            img_op = info_op.get("imagem")
            if img_op and os.path.exists(img_op):
                st.image(img_op, width=120)
            elif img_op:
                st.caption(f"⚠️ Imagem não encontrada: {img_op}")
        if marcado:
            opcionais_selecionados[nome_op] = {
                "preco": preco_op,
                "descricao": info_op.get("descricao", ""),
                "imagem": info_op.get("imagem"),
            }
else:
    st.caption("Nenhum opcional cadastrado em data.py")

# Item extra livre (fora da lista de opcionais)
st.markdown("**Item avulso (texto livre)**")
extra_desc = st.text_input("Descrição do item extra", value="")
extra_qtd = st.number_input("Qtd extra", min_value=0, value=0, step=1)
extra_valor = st.number_input("Valor unitário extra (R$)", min_value=0.0, value=0.0, step=10.0)

# ==================== GALERIA DE IMAGENS (produtos + opcionais marcados) ====================
st.markdown("**Imagens dos produtos selecionados**")
imagens_sel = get_imagens_selecionadas(tanque_key, bacia_key, bomba_key, filtro_key)

# Inclui fotos dos opcionais marcados
for nome_op, info_op in opcionais_selecionados.items():
    img_op = info_op.get("imagem")
    if img_op:
        imagens_sel.append((f"Opcional: {nome_op}", img_op))

imagens_existentes = [(titulo, path) for titulo, path in imagens_sel if path and os.path.exists(path)]

if imagens_existentes:
    cols_img = st.columns(min(len(imagens_existentes), 4))
    for idx, (titulo, path) in enumerate(imagens_existentes):
        with cols_img[idx % len(cols_img)]:
            st.image(path, use_container_width=True, caption=titulo)
    st.caption("* Imagens meramente ilustrativas – GP Company · entram no PDF da proposta")
else:
    st.caption(
        "Nenhuma imagem encontrada. Coloque fotos em "
        "`imagens_produtos/tanques|bacias|bombas|filtros|opcionais/`."
    )


# ==================== DESCONTOS E FRETE ====================
st.subheader("3. Descontos, Frete e Observações")

col_d1, col_d2, col_d3 = st.columns(3)

with col_d1:
    desconto_pct = st.number_input(
        "Desconto à vista (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.5,
        help="Percentual de desconto para pagamento à vista. Pode ser alterado livremente."
    )

with col_d2:
    frete_valor = st.number_input("Valor do Frete (R$)", min_value=0.0, value=0.0, step=50.0)
    frete_obs = st.text_input("Observação do Frete", value="A COMBINAR")

with col_d3:
    fluido = st.text_input("Fluido a ser armazenado", value="Diesel")
    obs_gerais = st.text_area("Observações gerais (aparecem no PDF)", value="", height=80)

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    custo_total = st.number_input(
        "Custo interno total (R$) — opcional",
        min_value=0.0,
        value=0.0,
        step=100.0,
        help="Se preenchido, calcula margem sobre o valor à prazo.",
    )
with col_m2:
    comissao_pct = st.number_input(
        "Comissão vendedor (%)",
        min_value=0.0,
        max_value=30.0,
        value=0.0,
        step=0.5,
    )
with col_m3:
    obs_item = st.text_input(
        "Observação extra nos itens (PDF)",
        value="",
        help="Texto livre que aparece junto à descrição dos produtos.",
    )

# ==================== FORMA DE PAGAMENTO ====================
st.markdown("**Forma de pagamento (parcelas)**")
st.caption(
    "Defina as etapas e o percentual de cada uma. "
    "A soma dos % deve dar 100%. Os valores em R$ aparecem no resumo abaixo."
)

base_pagamento = st.radio(
    "Calcular parcelas sobre:",
    options=["Valor à prazo (sem desconto)", "Valor à vista (com desconto)"],
    index=0,
    horizontal=True,
)

# Quantidade de parcelas configuráveis
n_parcelas = st.number_input(
    "Quantidade de etapas de pagamento",
    min_value=1,
    max_value=8,
    value=3,
    step=1,
)

# Padrão clássico: 30% / 30% / 40%
_defaults_label = [
    "Entrada (ato do pedido)",
    "No embarque",
    "Faturado (após análise)",
    "Parcela 4",
    "Parcela 5",
    "Parcela 6",
    "Parcela 7",
    "Parcela 8",
]
_defaults_pct = [30.0, 30.0, 40.0, 0.0, 0.0, 0.0, 0.0, 0.0]

parcelas_cfg = []  # lista de {label, pct}
cols_parc = st.columns(min(int(n_parcelas), 4))
for i in range(int(n_parcelas)):
    with cols_parc[i % len(cols_parc)]:
        lab = st.text_input(
            f"Etapa {i+1} – nome",
            value=_defaults_label[i] if i < len(_defaults_label) else f"Parcela {i+1}",
            key=f"parc_lab_{i}",
        )
        pct = st.number_input(
            f"Etapa {i+1} – %",
            min_value=0.0,
            max_value=100.0,
            value=float(_defaults_pct[i]) if i < len(_defaults_pct) else 0.0,
            step=1.0,
            key=f"parc_pct_{i}",
        )
        parcelas_cfg.append({"label": lab, "pct": pct})

soma_pct = sum(p["pct"] for p in parcelas_cfg)
if abs(soma_pct - 100.0) > 0.05:
    st.warning(f"A soma dos percentuais está em **{soma_pct:.1f}%** (ideal: 100%).")
else:
    st.success(f"Soma dos percentuais: **{soma_pct:.1f}%**")


# ==================== CÁLCULOS ====================
itens = []

# Tanque
itens.append({
    "descricao": f"TANQUE AÉREO – AÇO CARBONO ASTM A-36 – {tanque_key} (GP Company)",
    "qtd": 1,
    "unitario": preco_tanque,
    "total": preco_tanque,
})

# Bacia
if bacia_key != "SEM BACIA" or preco_bacia > 0:
    itens.append({
        "descricao": f"BACIA DE CONTENÇÃO – {bacia_key} (GP Company)",
        "qtd": 1,
        "unitario": preco_bacia,
        "total": preco_bacia,
    })

# Bomba
if bomba_key != "SEM BOMBA" or preco_bomba > 0:
    itens.append({
        "descricao": bomba_key,
        "qtd": 1,
        "unitario": preco_bomba,
        "total": preco_bomba,
    })

# Filtro
if filtro_key != "SEM FILTRO" or preco_filtro > 0:
    itens.append({
        "descricao": filtro_key,
        "qtd": 1,
        "unitario": preco_filtro,
        "total": preco_filtro,
    })

# Elemento
if elemento_key != "SEM ELEMENTO" or preco_elemento > 0:
    itens.append({
        "descricao": elemento_key,
        "qtd": 1,
        "unitario": preco_elemento,
        "total": preco_elemento,
    })

# Opcionais marcados (checkbox) — descrição completa, sem corte
for nome_op, info_op in opcionais_selecionados.items():
    if info_op.get("descricao"):
        desc_op = f"OPCIONAL: {nome_op} – {info_op['descricao']}"
    else:
        desc_op = f"OPCIONAL: {nome_op}"
    itens.append({
        "descricao": desc_op,
        "qtd": 1,
        "unitario": info_op["preco"],
        "total": info_op["preco"],
    })

# Item avulso (texto livre)
if extra_qtd > 0 and extra_desc.strip():
    itens.append({
        "descricao": extra_desc.strip(),
        "qtd": extra_qtd,
        "unitario": extra_valor,
        "total": extra_qtd * extra_valor,
    })

total_produtos = sum(i["total"] for i in itens)
valor_desconto = total_produtos * (desconto_pct / 100.0)
total_avista = total_produtos - valor_desconto
total_geral = total_avista + frete_valor  # frete normalmente não entra no desconto à vista

peso_total = tinfo.get("peso", 0) + binfo.get("peso", 0)

# Base das parcelas: à prazo ou à vista (+ frete se houver)
if base_pagamento.startswith("Valor à vista"):
    base_parcela = total_avista + frete_valor
else:
    base_parcela = total_produtos + frete_valor

parcelas_calc = []
for p in parcelas_cfg:
    if p["pct"] > 0:
        valor_p = base_parcela * (p["pct"] / 100.0)
        parcelas_calc.append({
            "label": p["label"],
            "pct": p["pct"],
            "valor": valor_p,
        })

# Margem e comissão
margem_valor = (total_produtos - custo_total) if custo_total > 0 else None
margem_pct = ((total_produtos - custo_total) / total_produtos * 100) if custo_total > 0 and total_produtos > 0 else None
comissao_valor = total_produtos * (comissao_pct / 100.0) if comissao_pct > 0 else 0.0
primeira_parcela = parcelas_calc[0]["valor"] if parcelas_calc else 0.0

# DIFAL + total estimado cliente (antes da sidebar para aparecer no resumo lateral)
base_difal = total_produtos
difal_info = calcular_difal(
    base_difal,
    uf_destino if uf_destino != "—" else "",
    uf_origem or UF_ORIGEM_PADRAO,
)
valor_difal = float(difal_info.get("valor_difal") or 0)
total_cliente_avista = total_avista + frete_valor + valor_difal
total_cliente_prazo = total_produtos + frete_valor + valor_difal

# Resumo fixo na sidebar (sempre visível)
with st.sidebar:
    st.markdown("---")
    st.markdown("### Resumo rápido")
    st.metric("Total produtos", format_brl(total_produtos))
    st.metric("À vista", format_brl(total_avista))
    if primeira_parcela:
        st.metric("1ª parcela", format_brl(primeira_parcela))
    if valor_difal > 0:
        st.metric("DIFAL", format_brl(valor_difal))
    st.metric("Total cliente (à vista+DIFAL)", format_brl(total_cliente_avista))
    if margem_pct is not None:
        st.metric("Margem", f"{margem_pct:.1f}%")
        if margem_pct < 15:
            st.warning("Margem abaixo de 15%")
    if comissao_valor > 0:
        st.caption(f"Comissão: {format_brl(comissao_valor)}")


# ==================== RESUMO EM TEMPO REAL ====================
st.subheader("4. Resumo do Orçamento")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Produtos", format_brl(total_produtos))
c2.metric(f"Desconto {desconto_pct:.1f}%", f"- {format_brl(valor_desconto)}")
c3.metric("Valor à Vista", format_brl(total_avista))
c4.metric("Peso aprox.", f"{peso_total} kg")

c5, c6, c7 = st.columns(3)
c5.metric("À prazo × À vista", f"Economia {format_brl(valor_desconto)}")
if margem_valor is not None:
    c6.metric("Margem", f"{format_brl(margem_valor)} ({margem_pct:.1f}%)")
else:
    c6.metric("Margem", "—")
c7.metric("Comissão", format_brl(comissao_valor) if comissao_valor else "—")

# ----- DIFAL (já calculado acima) + totais para o cliente -----
st.markdown("**DIFAL estimado (ICMS interestadual)**")
st.caption(
    "Fórmula: valor da NF × (alíquota interna do **destino** − alíquota interestadual). "
    "Produtos nacionais. Tabela ICMS 2025 com matriz interestadual completa (27×27)."
)
if uf_destino and uf_destino != "—":
    d1, d2, d3, d4 = st.columns(4)
    d1.metric("UF", f"{uf_origem} → {uf_destino}")
    d2.metric("Interna destino", f"{difal_info['aliquota_interna_destino']:.1f}%")
    d3.metric("Interestadual", f"{difal_info['aliquota_interestadual']:.1f}%")
    d4.metric("DIFAL estimado", format_brl(valor_difal))
    if difal_info["aplica"] and valor_difal > 0:
        st.success(
            f"Diferença: {difal_info['diferenca_pp']:.1f} p.p. sobre base {format_brl(base_difal)}. "
            "Orientativo — confirmar com o fiscal na NF."
        )
    else:
        st.info(difal_info.get("observacao") or "Sem DIFAL para esta combinação.")
else:
    st.warning("Selecione a **UF destino** nos dados do cliente para calcular o DIFAL.")

st.markdown("**Total estimado para o cliente**")
t1, t2, t3 = st.columns(3)
t1.metric("À prazo + frete + DIFAL", format_brl(total_cliente_prazo))
t2.metric("À vista + frete + DIFAL", format_brl(total_cliente_avista))
t3.metric("Só DIFAL", format_brl(valor_difal))
st.caption(
    "Composição à vista: produtos com desconto + frete + DIFAL. "
    "Composição à prazo: produtos sem desconto + frete + DIFAL."
)

if frete_valor > 0:
    st.info(f"Frete: {format_brl(frete_valor)} → **Total geral: {format_brl(total_geral)}**")

# Parcelas em tempo real
if parcelas_calc:
    st.markdown(
        f"**Parcelas** (sobre {format_brl(base_parcela)} — "
        f"{'à vista' if base_pagamento.startswith('Valor à vista') else 'à prazo'}"
        f"{' + frete' if frete_valor > 0 else ''})"
    )
    cols_v = st.columns(min(len(parcelas_calc), 4))
    for idx, p in enumerate(parcelas_calc):
        with cols_v[idx % len(cols_v)]:
            st.metric(
                f"{p['label']} ({p['pct']:.0f}%)",
                format_brl(p["valor"]),
            )
    # Tabela detalhada
    df_parc = pd.DataFrame([
        {
            "Etapa": p["label"],
            "%": f"{p['pct']:.1f}%",
            "Valor": format_brl(p["valor"]),
        }
        for p in parcelas_calc
    ])
    st.dataframe(df_parc, use_container_width=True, hide_index=True)

# Tabela de itens
df = pd.DataFrame([
    {
        "Descrição": i["descricao"],
        "Qtd": i["qtd"],
        "Unitário": format_brl(i["unitario"]),
        "Total": format_brl(i["total"]),
    }
    for i in itens
])
st.dataframe(df, use_container_width=True, hide_index=True)


# ==================== GERAÇÃO DO PDF ====================
st.subheader("5. Gerar Proposta PDF")

modo = st.radio(
    "Tipo de documento",
    options=[
        "Orçamento resumido (1 página – valores + dados)",
        "Proposta completa (valores + especificações + condições/garantia)",
        "Somente condições, garantias e cláusulas",
    ],
    index=1,
    horizontal=True,
)

modo_map = {
    "Orçamento resumido (1 página – valores + dados)": "resumo",
    "Proposta completa (valores + especificações + condições/garantia)": "completa",
    "Somente condições, garantias e cláusulas": "condicoes",
}
modo_pdf = modo_map[modo]

# Monta dict de dados para o PDF / histórico
dados_pdf = {
    "cliente": {
        "razao_social": razao_social or "—",
        "cnpj": cnpj or "—",
        "endereco": endereco or "—",
        "telefone": telefone or "—",
        "email": email or "—",
        "contato": contato or "—",
        "uf": uf_destino if uf_destino != "—" else "",
        "uf_origem": uf_origem or UF_ORIGEM_PADRAO,
    },
    "cotacao": {
        "vendedor": vendedor,
        "numero": numero_cotacao,
        "data": data_cotacao.strftime("%d/%m/%Y"),
        "validade": f"{validade_dias} dias",
        "validade_ate": data_validade_fim.strftime("%d/%m/%Y"),
    },
    "itens": itens,
    "total_produtos": total_produtos,
    "desconto_pct": desconto_pct,
    "valor_desconto": valor_desconto,
    "total_avista": total_avista,
    "frete": frete_valor,
    "frete_obs": frete_obs,
    "total_geral": total_geral if frete_valor > 0 else total_avista,
    "tanque_key": tanque_key,
    "bacia_key": bacia_key,
    "bomba_key": bomba_key,
    "filtro_key": filtro_key,
    "fluido": fluido,
    "obs": obs_gerais,
    "obs_item": obs_item,
    "imagem_produto": get_imagem_tanque(tanque_key),
    "imagens": imagens_sel,
    "opcionais": opcionais_selecionados,
    "parcelas": parcelas_calc,
    "base_pagamento": base_pagamento,
    "base_parcela": base_parcela,
    "custo_total": custo_total,
    "margem_valor": margem_valor,
    "margem_pct": margem_pct,
    "comissao_pct": comissao_pct,
    "comissao_valor": comissao_valor,
    "marca_dagua": True,
    "capa": True,
    "difal": difal_info,
    "total_cliente_avista": total_cliente_avista,
    "total_cliente_prazo": total_cliente_prazo,
}

incluir_capa = st.checkbox("Incluir capa no PDF", value=True)
marca_dagua = st.checkbox("Marca d'água ORÇAMENTO no PDF", value=True)
dados_pdf["capa"] = incluir_capa
dados_pdf["marca_dagua"] = marca_dagua

col_btn1, col_btn2 = st.columns([1, 3])

with col_btn1:
    gerar = st.button("📄 Gerar PDF", type="primary", use_container_width=True)

if gerar:
    erros = []
    if not razao_social.strip():
        erros.append("Razão Social do cliente")
    if not numero_cotacao.strip():
        erros.append("Número da cotação")
    if not vendedor or vendedor == "—":
        erros.append("Agente de vendas")
    soma_pct = sum(p["pct"] for p in parcelas_cfg)
    if parcelas_cfg and abs(soma_pct - 100.0) > 0.5:
        erros.append(f"Soma das parcelas = {soma_pct:.1f}% (precisa ser 100%)")
    if margem_pct is not None and margem_pct < 0:
        erros.append("Margem negativa (custo maior que o preço)")

    if erros:
        st.error("Corrija antes de gerar o PDF:\n- " + "\n- ".join(erros))
    else:
        with st.spinner("Gerando proposta profissional..."):
            try:
                pdf_bytes = gerar_pdf(dados_pdf, modo=modo_pdf)
                # Histórico
                try:
                    path_salvo = salvar_proposta(numero_cotacao, dados_pdf, pdf_bytes)
                    st.caption(f"Salvo no histórico: `{path_salvo}`")
                except Exception as e_hist:
                    st.warning(f"PDF ok, mas histórico não gravou: {e_hist}")

                nome_arquivo = f"Proposta_{numero_cotacao.replace('/', '-')}_{razao_social[:30].replace(' ', '_')}.pdf"
                st.success("Proposta gerada com sucesso!")
                st.download_button(
                    label="⬇️ Baixar PDF",
                    data=pdf_bytes,
                    file_name=nome_arquivo,
                    mime="application/pdf",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(f"Erro ao gerar PDF: {e}")
                st.exception(e)

st.markdown("---")
st.caption("Sistema de propostas · Casa do Frentista · GP Company · Uso interno")
