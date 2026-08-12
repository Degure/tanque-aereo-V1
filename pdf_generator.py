# pdf_generator.py - Geração de propostas comerciais profissionais
# Casa do Frentista / GP Company

import os
from io import BytesIO
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, KeepTogether, HRFlowable, ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from data import EMPRESA, TEXTOS, TANQUES, BACIAS

# Cores elegantes
AZUL_ESCURO = colors.HexColor("#1a365d")
AZUL_MEDIO = colors.HexColor("#2c5282")
LARANJA = colors.HexColor("#e65c00")
CINZA_ESCURO = colors.HexColor("#2d3748")
CINZA_CLARO = colors.HexColor("#f7fafc")
CINZA_BORDA = colors.HexColor("#e2e8f0")
VERDE_DESCONTO = colors.HexColor("#276749")

LOGO_CASA = os.path.join(os.path.dirname(__file__), "logo_casa.png")
LOGO_GP = os.path.join(os.path.dirname(__file__), "logo_gp.png")


def format_brl(valor: float) -> str:
    """Formata valor em Real brasileiro."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _imagem_responsiva(path: str, max_w: float, max_h: float):
    """
    Carrega imagem e dimensiona mantendo proporção dentro de max_w x max_h.
    Retorna objeto Image do ReportLab ou None se falhar.
    """
    if not path or not os.path.exists(path):
        return None
    try:
        from PIL import Image as PILImage
        with PILImage.open(path) as pil_im:
            iw, ih = pil_im.size
        if iw <= 0 or ih <= 0:
            return None
        ratio = min(max_w / iw, max_h / ih)
        return Image(path, width=iw * ratio, height=ih * ratio)
    except Exception:
        return None


def _grade_imagens(imagens: list, styles, max_total_width: float = 180 * mm, max_h: float = 42 * mm):
    """
    Monta uma grade adaptativa de imagens (1 a 4 itens).
    - 1 imagem: larga e centralizada
    - 2 imagens: lado a lado
    - 3–4 imagens: grid proporcional
    Retorna lista de flowables ou lista vazia.
    """
    from PIL import Image as PILImage

    validas = [(t, p) for t, p in imagens if p and os.path.exists(p)]
    if not validas:
        return []

    n = min(len(validas), 4)
    validas = validas[:n]
    gap = 3 * mm
    cell_w = (max_total_width - gap * (n - 1)) / n

    cells = []
    for titulo, path in validas:
        img = _imagem_responsiva(path, cell_w - 2 * mm, max_h)
        if img is None:
            continue
        # Nome completo do produto — Paragraph quebra linha automaticamente se for longo
        estilo_legenda = ParagraphStyle(
            name="LegendaImg",
            parent=styles["CorpoPequeno"],
            fontSize=6.5,
            alignment=TA_CENTER,
            leading=8,
        )
        legenda = Paragraph(f"<b>{titulo}</b>", estilo_legenda)
        cell = Table([[img], [legenda]], colWidths=[cell_w])
        cell.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
            ("VALIGN", (0, 1), (0, 1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ]))
        cells.append(cell)

    if not cells:
        return []

    # Completa células vazias para manter alinhamento visual se quiser 4 colunas fixas
    # Aqui usamos exatamente o número de imagens para layout mais limpo
    col_widths = [cell_w] * len(cells)
    row = Table([cells], colWidths=col_widths)
    row.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.5, CINZA_BORDA),
        ("BACKGROUND", (0, 0), (-1, -1), CINZA_CLARO),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))

    nota = Paragraph(
        "<i>* Imagens meramente ilustrativas – equipamentos GP Company</i>",
        styles["CorpoPequeno"],
    )
    return [row, Spacer(1, 2 * mm), nota, Spacer(1, 3 * mm)]


def criar_estilos():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="TituloPrincipal",
        fontName="Helvetica-Bold",
        fontSize=14,
        textColor=AZUL_ESCURO,
        alignment=TA_CENTER,
        spaceAfter=6,
        spaceBefore=4,
    ))

    styles.add(ParagraphStyle(
        name="Subtitulo",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=AZUL_MEDIO,
        alignment=TA_LEFT,
        spaceBefore=10,
        spaceAfter=4,
    ))

    styles.add(ParagraphStyle(
        name="Corpo",
        fontName="Helvetica",
        fontSize=9,
        textColor=CINZA_ESCURO,
        alignment=TA_JUSTIFY,
        leading=12,
        spaceAfter=3,
    ))

    styles.add(ParagraphStyle(
        name="CorpoPequeno",
        fontName="Helvetica",
        fontSize=8,
        textColor=CINZA_ESCURO,
        alignment=TA_LEFT,
        leading=10,
    ))

    styles.add(ParagraphStyle(
        name="Label",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=AZUL_ESCURO,
    ))

    styles.add(ParagraphStyle(
        name="ValorDestaque",
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=AZUL_ESCURO,
        alignment=TA_RIGHT,
    ))

    styles.add(ParagraphStyle(
        name="Desconto",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=VERDE_DESCONTO,
        alignment=TA_RIGHT,
    ))

    styles.add(ParagraphStyle(
        name="Rodape",
        fontName="Helvetica",
        fontSize=7,
        textColor=colors.gray,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name="ItemLista",
        fontName="Helvetica",
        fontSize=8.5,
        textColor=CINZA_ESCURO,
        leftIndent=10,
        leading=11,
    ))

    return styles


def cabecalho(canvas, doc):
    canvas.saveState()
    # Linha superior
    canvas.setStrokeColor(LARANJA)
    canvas.setLineWidth(3)
    canvas.line(15*mm, A4[1] - 12*mm, A4[0] - 15*mm, A4[1] - 12*mm)

    canvas.setStrokeColor(AZUL_ESCURO)
    canvas.setLineWidth(1)
    canvas.line(15*mm, A4[1] - 13.5*mm, A4[0] - 15*mm, A4[1] - 13.5*mm)

    # Rodapé
    canvas.setStrokeColor(CINZA_BORDA)
    canvas.setLineWidth(0.5)
    canvas.line(15*mm, 12*mm, A4[0] - 15*mm, 12*mm)

    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.gray)
    texto_rodape = f"{EMPRESA['nome']}  |  {EMPRESA['endereco']} - {EMPRESA['cidade']}  |  CNPJ {EMPRESA['cnpj']}"
    canvas.drawCentredString(A4[0]/2, 7*mm, texto_rodape)
    canvas.drawRightString(A4[0] - 15*mm, 7*mm, f"Pág. {doc.page}")

    canvas.restoreState()


def gerar_pdf(dados: Dict[str, Any], modo: str = "completa") -> bytes:
    """
    Gera PDF da proposta.
    modo: 'resumo' | 'completa' | 'condicoes'
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=15*mm,
        rightMargin=15*mm,
        topMargin=18*mm,
        bottomMargin=18*mm,
    )

    styles = criar_estilos()
    story = []

    # ========== CABEÇALHO COM LOGOS ==========
    logo_casa = None
    logo_gp = None
    if os.path.exists(LOGO_CASA):
        try:
            logo_casa = Image(LOGO_CASA, width=45*mm, height=14*mm)
        except Exception:
            pass
    if os.path.exists(LOGO_GP):
        try:
            # GP logo is large/black background – crop conceptually by sizing carefully
            logo_gp = Image(LOGO_GP, width=28*mm, height=18*mm)
        except Exception:
            pass

    header_data = []
    if logo_casa and logo_gp:
        header_data = [[logo_casa, Paragraph(
            f"<b>{EMPRESA['nome'].upper()}</b><br/>"
            f"<font size='8'>Equipamentos GP Company</font><br/>"
            f"<font size='7'>{EMPRESA['endereco']}<br/>{EMPRESA['cep']} - {EMPRESA['cidade']}<br/>CNPJ {EMPRESA['cnpj']}</font>",
            styles["CorpoPequeno"]
        ), logo_gp]]
        col_widths = [50*mm, 90*mm, 35*mm]
    elif logo_casa:
        header_data = [[logo_casa, Paragraph(
            f"<b>{EMPRESA['nome'].upper()}</b><br/>"
            f"<font size='8'>Equipamentos GP Company</font><br/>"
            f"<font size='7'>{EMPRESA['endereco']} - {EMPRESA['cidade']}<br/>CNPJ {EMPRESA['cnpj']}</font>",
            styles["CorpoPequeno"]
        )]]
        col_widths = [55*mm, 120*mm]
    else:
        header_data = [[Paragraph(
            f"<b>{EMPRESA['nome'].upper()}</b><br/>Equipamentos GP Company<br/>"
            f"{EMPRESA['endereco']} - {EMPRESA['cidade']}<br/>CNPJ {EMPRESA['cnpj']}",
            styles["Corpo"]
        )]]
        col_widths = [175*mm]

    t_header = Table(header_data, colWidths=col_widths)
    t_header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ("ALIGN", (-1, 0), (-1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 3*mm))
    story.append(HRFlowable(width="100%", thickness=1.5, color=AZUL_ESCURO, spaceBefore=1, spaceAfter=4))

    # ========== TÍTULO ==========
    if modo == "resumo":
        titulo = "ORÇAMENTO COMERCIAL"
    elif modo == "condicoes":
        titulo = "CONDIÇÕES COMERCIAIS, GARANTIAS E CLÁUSULAS"
    else:
        titulo = "PROPOSTA TÉCNICA E COMERCIAL"

    story.append(Paragraph(titulo, styles["TituloPrincipal"]))
    story.append(Paragraph("Solução de Abastecimento Interno – Tanques Aéreos GP Company", styles["CorpoPequeno"]))
    story.append(Spacer(1, 3*mm))

    # ========== DADOS DO CLIENTE + COTAÇÃO ==========
    cliente = dados.get("cliente", {})
    cotacao = dados.get("cotacao", {})

    dados_cliente = [
        [Paragraph("<b>CLIENTE</b>", styles["Label"]), "",
         Paragraph("<b>Ag. Vendas</b>", styles["Label"]),
         Paragraph(cotacao.get("vendedor", "—"), styles["CorpoPequeno"])],
        [Paragraph("Razão Social", styles["CorpoPequeno"]),
         Paragraph(cliente.get("razao_social", "—"), styles["CorpoPequeno"]),
         Paragraph("<b>Cotação</b>", styles["Label"]),
         Paragraph(str(cotacao.get("numero", "—")), styles["CorpoPequeno"])],
        [Paragraph("CNPJ", styles["CorpoPequeno"]),
         Paragraph(cliente.get("cnpj", "—"), styles["CorpoPequeno"]),
         Paragraph("<b>Data</b>", styles["Label"]),
         Paragraph(cotacao.get("data", "—"), styles["CorpoPequeno"])],
        [Paragraph("Endereço", styles["CorpoPequeno"]),
         Paragraph(cliente.get("endereco", "—"), styles["CorpoPequeno"]),
         Paragraph("<b>Validade</b>", styles["Label"]),
         Paragraph(cotacao.get("validade", "7 dias"), styles["CorpoPequeno"])],
        [Paragraph("Telefone / E-mail", styles["CorpoPequeno"]),
         Paragraph(f"{cliente.get('telefone', '—')}  |  {cliente.get('email', '—')}", styles["CorpoPequeno"]),
         Paragraph("<b>Contato</b>", styles["Label"]),
         Paragraph(cliente.get("contato", "—"), styles["CorpoPequeno"])],
    ]

    t_cli = Table(dados_cliente, colWidths=[32*mm, 78*mm, 28*mm, 37*mm])
    t_cli.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CINZA_CLARO),
        ("BOX", (0, 0), (-1, -1), 0.6, CINZA_BORDA),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, CINZA_BORDA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(t_cli)
    story.append(Spacer(1, 4*mm))

    # ========== IMAGENS RESPONSIVAS DOS PRODUTOS ==========
    if modo != "condicoes":
        from data import get_imagens_selecionadas

        imagens = dados.get("imagens")
        if not imagens:
            imagens = get_imagens_selecionadas(
                dados.get("tanque_key", "10.000L"),
                dados.get("bacia_key", "SEM BACIA"),
                dados.get("bomba_key", "SEM BOMBA"),
                dados.get("filtro_key", "SEM FILTRO"),
            )

        # Grade adapta automaticamente: 1, 2, 3 ou 4 colunas
        for flowable in _grade_imagens(imagens, styles):
            story.append(flowable)

    # ========== ITENS / VALORES (exceto modo condições) ==========
    if modo != "condicoes":
        story.append(Paragraph("DESCRIÇÃO DOS PRODUTOS", styles["Subtitulo"]))

        itens = dados.get("itens", [])
        header_itens = [
            Paragraph("<b>Descrição</b>", styles["CorpoPequeno"]),
            Paragraph("<b>Qtd</b>", styles["CorpoPequeno"]),
            Paragraph("<b>Valor Unit.</b>", styles["CorpoPequeno"]),
            Paragraph("<b>Valor Final</b>", styles["CorpoPequeno"]),
        ]
        rows = [header_itens]
        for item in itens:
            rows.append([
                Paragraph(item.get("descricao", ""), styles["CorpoPequeno"]),
                Paragraph(str(item.get("qtd", 1)), styles["CorpoPequeno"]),
                Paragraph(format_brl(item.get("unitario", 0)), styles["CorpoPequeno"]),
                Paragraph(format_brl(item.get("total", 0)), styles["CorpoPequeno"]),
            ])

        t_itens = Table(rows, colWidths=[105*mm, 15*mm, 30*mm, 30*mm])
        t_itens.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, CINZA_CLARO]),
            ("BOX", (0, 0), (-1, -1), 0.7, AZUL_ESCURO),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, CINZA_BORDA),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (1, 0), (-1, -1), "CENTER"),
            ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        story.append(t_itens)
        story.append(Spacer(1, 3*mm))

        # Totais
        total_produtos = dados.get("total_produtos", 0)
        desconto_pct = dados.get("desconto_pct", 5.0)
        valor_desconto = dados.get("valor_desconto", 0)
        total_avista = dados.get("total_avista", total_produtos)
        frete = dados.get("frete", 0)
        frete_obs = dados.get("frete_obs", "A COMBINAR")
        total_geral = dados.get("total_geral", total_produtos)

        totais_data = [
            [Paragraph("<b>VALOR TOTAL PRODUTOS</b>", styles["CorpoPequeno"]),
             Paragraph(f"<b>{format_brl(total_produtos)}</b>", styles["ValorDestaque"])],
            [Paragraph(f"Desconto pagamento à vista ({desconto_pct:.1f}%)", styles["CorpoPequeno"]),
             Paragraph(f"- {format_brl(valor_desconto)}", styles["CorpoPequeno"])],
            [Paragraph("<b>VALOR ESPECIAL À VISTA</b>", styles["CorpoPequeno"]),
             Paragraph(f"<b>{format_brl(total_avista)}</b>", styles["Desconto"])],
        ]
        if frete > 0:
            totais_data.append([
                Paragraph(f"Frete: {frete_obs}", styles["CorpoPequeno"]),
                Paragraph(format_brl(frete), styles["CorpoPequeno"])
            ])
            totais_data.append([
                Paragraph("<b>TOTAL GERAL (c/ frete)</b>", styles["CorpoPequeno"]),
                Paragraph(f"<b>{format_brl(total_geral)}</b>", styles["ValorDestaque"])
            ])
        else:
            totais_data.append([
                Paragraph(f"Frete: {frete_obs}", styles["CorpoPequeno"]),
                Paragraph("—", styles["CorpoPequeno"])
            ])

        t_tot = Table(totais_data, colWidths=[130*mm, 45*mm])
        t_tot.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.7, AZUL_ESCURO),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, CINZA_BORDA),
            ("BACKGROUND", (0, 0), (-1, 0), CINZA_CLARO),
            ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#e6fffa")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (1, 0), (1, -1), "RIGHT"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        story.append(t_tot)
        story.append(Spacer(1, 3*mm))

        story.append(Paragraph(
            f"<b>Prazo de fabricação:</b> {EMPRESA['prazo_fabricacao']} &nbsp;&nbsp;|&nbsp;&nbsp; "
            f"<b>NCM:</b> {EMPRESA['ncm']} &nbsp;&nbsp;|&nbsp;&nbsp; "
            f"<b>Norma:</b> {EMPRESA['norma']}",
            styles["CorpoPequeno"]
        ))
        story.append(Paragraph(
            f"* Guincho Munck para descarga por conta do cliente. Imagem meramente ilustrativa.",
            styles["CorpoPequeno"]
        ))

    # ========== ESPECIFICAÇÕES TÉCNICAS (modo completa) ==========
    if modo == "completa":
        story.append(Spacer(1, 4*mm))
        story.append(HRFlowable(width="100%", thickness=0.8, color=CINZA_BORDA, spaceBefore=2, spaceAfter=4))
        story.append(Paragraph("ESPECIFICAÇÕES TÉCNICAS", styles["Subtitulo"]))

        tanque_sel = dados.get("tanque_key", "10.000L")
        bacia_sel = dados.get("bacia_key", "10.000L")
        tinfo = TANQUES.get(tanque_sel, {})
        binfo = BACIAS.get(bacia_sel, {})

        story.append(Paragraph("<b>Tanque Aéreo Horizontal – Aço Carbono ASTM A-36</b>", styles["CorpoPequeno"]))
        specs_t = [
            f"• Capacidade: {tinfo.get('label', tanque_sel)}",
            f"• Diâmetro: {tinfo.get('diametro', '—')}",
            f"• Comprimento: {tinfo.get('comprimento', '—')}",
            f"• Espessura da chapa: {tinfo.get('chapa', '—')}",
            f"• Peso aproximado: {tinfo.get('peso', 0)} kg",
            f"• Fluido: {dados.get('fluido', TEXTOS['fluido_padrao'])}",
            f"• Tratamento interno: {TEXTOS['tratamento_interno_tanque']}",
            f"• Tratamento externo: {TEXTOS['tratamento_externo']}",
            f"• Pressão de trabalho: {TEXTOS['pressao']}",
            f"• Temperatura: {TEXTOS['temperatura']}",
            f"• Padrão de fabricação: {EMPRESA['norma']}",
        ]
        for s in specs_t:
            story.append(Paragraph(s, styles["ItemLista"]))

        if bacia_sel != "SEM BACIA":
            story.append(Spacer(1, 2*mm))
            story.append(Paragraph("<b>Bacia de Contenção</b>", styles["CorpoPequeno"]))
            specs_b = [
                f"• Capacidade: {binfo.get('label', bacia_sel)}",
                f"• Largura: {binfo.get('largura', '—')}",
                f"• Altura: {binfo.get('altura', '—')}",
                f"• Comprimento: {binfo.get('comprimento', '—')}",
                f"• Espessura da chapa: {binfo.get('chapa', '—')}",
                f"• Peso aproximado: {binfo.get('peso', 0)} kg",
                f"• Tratamento interno: Limpeza Mecânica (sem pintura)",
                f"• Tratamento externo: {TEXTOS['tratamento_externo']}",
            ]
            for s in specs_b:
                story.append(Paragraph(s, styles["ItemLista"]))

        story.append(Spacer(1, 2*mm))
        story.append(Paragraph("<b>Acessórios padrão inclusos</b>", styles["CorpoPequeno"]))
        acessorios = [
            "01 Bocal de saída 1.1/2''",
            "01 Bocal de entrada 4''",
            "03 Bocais para 2''",
            "02 Bocais de dreno 3/4''",
            "01 Bocal de visita",
            "02 Berços de apoio com 200mm de altura",
            "02 Alças de içamento",
            "01 Válvula de Segurança Get Fuel",
            "Todos os bocais em meia luva com rosca interna BSP + bujões em PVC",
        ]
        for a in acessorios:
            story.append(Paragraph(f"• {a}", styles["ItemLista"]))

        peso_total = tinfo.get("peso", 0) + binfo.get("peso", 0)
        story.append(Paragraph(f"<b>Peso total aproximado do conjunto:</b> {peso_total} kg", styles["CorpoPequeno"]))
        story.append(Paragraph(f"<b>Documentação que acompanha:</b> {TEXTOS['acompanha']}", styles["CorpoPequeno"]))

    # ========== CONDIÇÕES / GARANTIA / CONTRATO ==========
    if modo in ("completa", "condicoes"):
        if modo == "completa":
            story.append(PageBreak())
            # Mini cabeçalho na página 2
            story.append(Paragraph(f"<b>{EMPRESA['nome']}</b> – Condições Comerciais e Garantias", styles["Subtitulo"]))
            story.append(HRFlowable(width="100%", thickness=1, color=AZUL_ESCURO, spaceBefore=1, spaceAfter=4))

        story.append(Paragraph("1. CONDIÇÕES COMERCIAIS", styles["Subtitulo"]))
        story.append(Paragraph(
            "Os valores apresentados são para pagamento nas condições abaixo. "
            "<b>Caso o cliente não seja contribuinte de ICMS, poderá ser adicionado o diferencial de alíquota conforme o estado de destino.<b>",
            styles["Corpo"]
        ))
        story.append(Paragraph(
            "<b>Forma de pagamento sugerida:</b> 30% de entrada no ato do pedido + 30% no embarque + 40% faturado mediante análise financeira e aprovação de cadastro. "
            "Alternativamente: parcelamento no cartão de crédito em até 6x (sujeito a juros da operadora).",
            styles["Corpo"]
        ))
        story.append(Paragraph(
            f"<b>Prazo de fabricação:</b> {EMPRESA['prazo_fabricacao']} após confirmação do pagamento da entrada e formalização do pedido.",
            styles["Corpo"]
        ))
        story.append(Paragraph(
            f"<b>Validade desta proposta:</b> {cotacao.get('validade', '7 dias')}.",
            styles["Corpo"]
        ))

        story.append(Paragraph("2. GARANTIA", styles["Subtitulo"]))
        story.append(Paragraph(
            f"Garantimos o tanque e a bacia de contenção contra defeitos de fabricação pelo período de "
            f"<b>{EMPRESA['garantia_meses']} (seis) meses</b>, contados a partir da data de emissão da Nota Fiscal, "
            "desde que observados os procedimentos de instalação, operação e manutenção recomendados. "
            "Em caso de necessidade de reparo, o equipamento deverá ser enviado à fábrica.",
            styles["Corpo"]
        ))
        story.append(Paragraph(
            "Bombas e filtros: garantia conforme o fabricante do equipamento (geralmente 90 dias a 12 meses). "
            "Estão excluídos da garantia: desgaste normal, uso inadequado, líquidos incompatíveis, influências climáticas, "
            "modificações ou consertos realizados por terceiros sem autorização prévia por escrito.",
            styles["Corpo"]
        ))

        story.append(Paragraph("3. RESPONSABILIDADES", styles["Subtitulo"]))
        story.append(Paragraph("<b>Do Fornecedor (Casa do Frentista / GP Company):</b>", styles["CorpoPequeno"]))
        story.append(Paragraph("• Fabricação, soldagem e pintura do tanque e bacia conforme normas aplicáveis.", styles["ItemLista"]))
        story.append(Paragraph("• Fornecimento da documentação técnica listada (Data book, ART, etc.).", styles["ItemLista"]))
        story.append(Paragraph("• Transporte até o local combinado (quando incluso no valor ou frete contratado).", styles["ItemLista"]))

        story.append(Paragraph("<b>Do Comprador:</b>", styles["CorpoPequeno"]))
        story.append(Paragraph("<b>• Acesso rodoviário livre e desimpedido para descarga.<b>", styles["ItemLista"]))
        story.append(Paragraph("<b>• Descarregamento com guincho Munck por conta do cliente.<b> ", styles["ItemLista"]))
        story.append(Paragraph("<b>• Preparação da base de apoio (concreto ou estrutura adequada).<b>", styles["ItemLista"]))
        story.append(Paragraph("<b>• Obtenção de licenças e alvarás locais, quando exigidos.<b>", styles["ItemLista"]))

        story.append(Paragraph("4. OBSERVAÇÕES GERAIS / CLÁUSULAS", styles["Subtitulo"]))
        story.append(Paragraph(
            "• Todo item não descrito expressamente nesta proposta não está incluso no escopo e no valor.",
            styles["ItemLista"]
        ))
        story.append(Paragraph(
            "• Exigências adicionais de testes, documentação extra ou plano de rigging serão cobradas à parte e devem ser informadas no fechamento.",
            styles["ItemLista"]
        ))
        story.append(Paragraph(
            "• Em caso de cancelamento do pedido pelo comprador após confirmação, será aplicada multa de 10% sobre o valor do contrato.",
            styles["ItemLista"]
        ))
        story.append(Paragraph(
            "• A presente proposta tem caráter comercial e técnico. A formalização se dará mediante pedido de compra ou contrato assinado pelas partes.",
            styles["ItemLista"]
        ))

        story.append(Spacer(1, 8*mm))
        story.append(Paragraph(
            "Agradecemos a oportunidade e colocamo-nos à disposição para quaisquer esclarecimentos.",
            styles["Corpo"]
        ))
        story.append(Spacer(1, 10*mm))

        # Assinaturas
        ass_data = [
            [Paragraph("_________________________________<br/><b>Casa do Frentista</b><br/>GP Company", styles["CorpoPequeno"]),
             Paragraph("_________________________________<br/><b>Cliente / Representante</b>", styles["CorpoPequeno"])],
        ]
        t_ass = Table(ass_data, colWidths=[90*mm, 90*mm])
        t_ass.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        story.append(t_ass)

    # Build
    doc.build(story, onFirstPage=cabecalho, onLaterPages=cabecalho)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
