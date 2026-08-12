# app.py - Sistema de Propostas Comerciais
# Casa do Frentista / GP Company

import streamlit as st
import json
import os
from datetime import datetime, timedelta
from typing import List

from data import (
    TANQUES, BACIAS, BOMBAS, FILTROS, ELEMENTOS,
    EMPRESA, VENDEDORES_INICIAL,
    get_imagem_tanque, get_imagens_selecionadas,
)
from pdf_generator import gerar_pdf, format_brl

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


# ==================== DADOS DO CLIENTE ====================
st.subheader("1. Dados do Cliente")
col1, col2, col3 = st.columns(3)

with col1:
    razao_social = st.text_input("Razão Social *", value="")
    cnpj = st.text_input("CNPJ", value="")
    contato = st.text_input("A/c (Contato)", value="")

with col2:
    endereco = st.text_input("Endereço / Cidade", value="")
    telefone = st.text_input("Telefone", value="")
    email = st.text_input("E-mail", value="")

with col3:
    vendedores = carregar_vendedores()
    vendedor = st.selectbox("Agente de Vendas *", vendedores if vendedores else ["—"])
    numero_cotacao = st.text_input("Nº da Cotação", value=f"{datetime.now().year}-")
    data_cotacao = st.date_input("Data", value=datetime.now())
    validade_dias = st.number_input("Validade (dias)", min_value=1, max_value=60, value=7)


# ==================== SELEÇÃO DE PRODUTOS ====================
st.subheader("2. Seleção de Produtos")

col_t, col_b = st.columns(2)

with col_t:
    tanque_key = st.selectbox(
        "Tanque Aéreo",
        options=list(TANQUES.keys()),
        index=list(TANQUES.keys()).index("10.000L") if "10.000L" in TANQUES else 0,
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
        index=list(BACIAS.keys()).index("10.000L") if "10.000L" in BACIAS else 0,
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
    bomba_key = st.selectbox("Bomba de Abastecimento", options=list(BOMBAS.keys()), index=0)
    preco_bomba = st.number_input(
        "Preço Bomba (R$)",
        value=float(BOMBAS[bomba_key]),
        min_value=0.0,
        step=10.0,
        key=f"p_bomba_{bomba_key}",
    )

with col_f:
    filtro_key = st.selectbox("Filtro", options=list(FILTROS.keys()), index=0)
    preco_filtro = st.number_input(
        "Preço Filtro (R$)",
        value=float(FILTROS[filtro_key]),
        min_value=0.0,
        step=10.0,
        key=f"p_filtro_{filtro_key}",
    )

with col_e:
    elemento_key = st.selectbox("Elemento Filtrante", options=list(ELEMENTOS.keys()), index=0)
    preco_elemento = st.number_input(
        "Preço Elemento (R$)",
        value=float(ELEMENTOS[elemento_key]),
        min_value=0.0,
        step=10.0,
        key=f"p_elem_{elemento_key}",
    )

# Preview das imagens de todos os produtos selecionados (tanque, bacia, bomba, filtro)
st.markdown("**Imagens dos produtos selecionados**")
imagens_sel = get_imagens_selecionadas(tanque_key, bacia_key, bomba_key, filtro_key)
imagens_existentes = [(titulo, path) for titulo, path in imagens_sel if path and os.path.exists(path)]

if imagens_existentes:
    cols_img = st.columns(min(len(imagens_existentes), 4))
    for idx, (titulo, path) in enumerate(imagens_existentes):
        with cols_img[idx % len(cols_img)]:
            st.image(path, use_container_width=True, caption=titulo)
    st.caption("* Imagens meramente ilustrativas – GP Company · entram no PDF da proposta")
else:
    st.caption("Nenhuma imagem encontrada. Coloque fotos em `imagens_produtos/tanques|bacias|bombas|filtros/`.")

# Itens extras manuais
st.markdown("**Itens adicionais (opcional)**")
extra_desc = st.text_input("Descrição do item extra", value="")
extra_qtd = st.number_input("Qtd extra", min_value=0, value=0, step=1)
extra_valor = st.number_input("Valor unitário extra (R$)", min_value=0.0, value=0.0, step=10.0)


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

# Extra
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


# ==================== RESUMO EM TEMPO REAL ====================
st.subheader("4. Resumo do Orçamento")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Produtos", format_brl(total_produtos))
c2.metric(f"Desconto {desconto_pct:.1f}%", f"- {format_brl(valor_desconto)}")
c3.metric("Valor à Vista", format_brl(total_avista))
c4.metric("Peso aprox.", f"{peso_total} kg")

if frete_valor > 0:
    st.info(f"Frete: {format_brl(frete_valor)} → **Total geral: {format_brl(total_geral)}**")

# Tabela de itens
import pandas as pd
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

# Monta dict de dados para o PDF
dados_pdf = {
    "cliente": {
        "razao_social": razao_social or "—",
        "cnpj": cnpj or "—",
        "endereco": endereco or "—",
        "telefone": telefone or "—",
        "email": email or "—",
        "contato": contato or "—",
    },
    "cotacao": {
        "vendedor": vendedor,
        "numero": numero_cotacao,
        "data": data_cotacao.strftime("%d/%m/%Y"),
        "validade": f"{validade_dias} dias",
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
    "imagem_produto": get_imagem_tanque(tanque_key),
    "imagens": get_imagens_selecionadas(tanque_key, bacia_key, bomba_key, filtro_key),
}

col_btn1, col_btn2 = st.columns([1, 3])

with col_btn1:
    gerar = st.button("📄 Gerar PDF", type="primary", use_container_width=True)

if gerar:
    if not razao_social.strip():
        st.warning("Preencha pelo menos a **Razão Social** do cliente.")
    else:
        with st.spinner("Gerando proposta profissional..."):
            try:
                pdf_bytes = gerar_pdf(dados_pdf, modo=modo_pdf)
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
