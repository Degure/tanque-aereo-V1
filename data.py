# data.py - Dados de produtos, medidas e preços da Casa do Frentista / GP Company

from typing import Dict, Any, List, Optional

# ==================== TANQUES ====================
TANQUES: Dict[str, Dict[str, Any]] = {
    "1.000L": {
        "preco": 4620.0,
        "diametro": "940mm",
        "comprimento": "1.500mm",
        "chapa": "2.65mm",
        "peso": 230,
        "label": "1.000L"
    },
    "3.000L": {
        "preco": 6915.0,
        "diametro": "1.270mm",
        "comprimento": "2.500mm",
        "chapa": "2.65mm",
        "peso": 500,
        "label": "3.000L"
    },
    "4.000L": {
        "preco": 8850.0,
        "diametro": "1.440mm",
        "comprimento": "3.100mm",
        "chapa": "3.00mm",
        "peso": 650,
        "label": "4.000L"
    },
    "5.000L": {
        "preco": 10640.0,
        "diametro": "1.440mm",
        "comprimento": "3.100mm",
        "chapa": "3.00mm",
        "peso": 680,
        "label": "5.000L"
    },
    "6.000L": {
        "preco": 13740.0,
        "diametro": "1.600mm",
        "comprimento": "3.100mm",
        "chapa": "3.00mm",
        "peso": 700,
        "label": "6.000L"
    },
    "7.500L": {
        "preco": 15780.0,
        "diametro": "1.900mm",
        "comprimento": "2.750mm",
        "chapa": "3.00mm",
        "peso": 800,
        "label": "7.500L"
    },
    "10.000L": {
        "preco": 18590.0,
        "diametro": "1.900mm",
        "comprimento": "3.600mm",
        "chapa": "3.00mm",
        "peso": 950,
        "label": "10.000L"
    },
    "12.000L": {
        "preco": 21000.0,
        "diametro": "1.900mm",
        "comprimento": "4.300mm",
        "chapa": "3.35mm",
        "peso": 1350,
        "label": "12.000L"
    },
    "14.900L": {
        "preco": 24860.0,
        "diametro": "1.900mm",
        "comprimento": "5.400mm",
        "chapa": "3.35mm",
        "peso": 1550,
        "label": "14.900L"
    },
    "20.000L": {
        "preco": 43365.0,
        "diametro": "2.100mm",
        "comprimento": "6.000mm",
        "chapa": "3.35mm",
        "peso": 2600,
        "label": "20.000L"
    },
    "30.000L": {
        "preco": 86000.0,
        "diametro": "2.540mm",
        "comprimento": "6.000mm",
        "chapa": "4.75mm",
        "peso": 3200,
        "label": "30.000L"
    },
    "BIPARTIDO 14.950L": {
        "preco": 27990.0,
        "diametro": "—",
        "comprimento": "—",
        "chapa": "—",
        "peso": 0,
        "label": "BIPARTIDO 14.950L"
    },
}

# ==================== BACIAS ====================
BACIAS: Dict[str, Dict[str, Any]] = {
    "SEM BACIA": {
        "preco": 0.0,
        "largura": "—",
        "altura": "—",
        "comprimento": "—",
        "chapa": "—",
        "peso": 0,
        "label": "SEM BACIA"
    },
    "1.000L": {
        "preco": 3500.0,
        "largura": "1.500mm",
        "altura": "300mm",
        "comprimento": "2.500mm",
        "chapa": "2.65mm",
        "peso": 200,
        "label": "1.000L"
    },
    "3.000L": {
        "preco": 5630.0,
        "largura": "2.000mm",
        "altura": "500mm",
        "comprimento": "3.600mm",
        "chapa": "2.65mm",
        "peso": 350,
        "label": "3.000L"
    },
    "4.000L": {
        "preco": 6115.0,
        "largura": "2.000mm",
        "altura": "600mm",
        "comprimento": "3.600mm",
        "chapa": "2.65mm",
        "peso": 430,
        "label": "4.000L"
    },
    "5.000L": {
        "preco": 6470.0,
        "largura": "2.000mm",
        "altura": "600mm",
        "comprimento": "4.800mm",
        "chapa": "2.65mm",
        "peso": 500,
        "label": "5.000L"
    },
    "6.000L": {
        "preco": 8875.0,
        "largura": "2.400mm",
        "altura": "600mm",
        "comprimento": "4.800mm",
        "chapa": "2.65mm",
        "peso": 650,
        "label": "6.000L"
    },
    "7.500L": {
        "preco": 13873.0,
        "largura": "2.400mm",
        "altura": "1.180mm",
        "comprimento": "4.000mm",
        "chapa": "2.65mm",
        "peso": 760,
        "label": "7.500L"
    },
    "10.000L": {
        "preco": 16485.0,
        "largura": "2.400mm",
        "altura": "1.180mm",
        "comprimento": "4.500mm",
        "chapa": "2.65mm",
        "peso": 900,
        "label": "10.000L"
    },
    "12.000L": {
        "preco": 17945.0,
        "largura": "2.400mm",
        "altura": "1.180mm",
        "comprimento": "5.000mm",
        "chapa": "2.65mm",
        "peso": 1100,
        "label": "12.000L"
    },
    "15.000L": {
        "preco": 20875.0,
        "largura": "2.400mm",
        "altura": "1.180mm",
        "comprimento": "6.500mm",
        "chapa": "2.65mm",
        "peso": 1300,
        "label": "15.000L"
    },
    "20.000L": {
        "preco": 32385.0,
        "largura": "2.600mm",
        "altura": "1.180mm",
        "comprimento": "7.200mm",
        "chapa": "2.65mm",
        "peso": 1800,
        "label": "20.000L"
    },
    "30.000L": {
        "preco": 64000.0,
        "largura": "3.000mm",
        "altura": "1.500mm",
        "comprimento": "7.800mm",
        "chapa": "2.65mm",
        "peso": 2800,
        "label": "30.000L"
    },
}

# ==================== BOMBAS ====================
BOMBAS: Dict[str, float] = {
    "SEM BOMBA": 0.0,
    "BOMBA ABASTECIMENTO 60LPM - 220V": 2299.0,
    "BOMBA ABASTECIMENTO GILBARCO 45LPM - ELETRÔNICA SIMPLES": 8790.0,
    "BOMBA ABASTECIMENTO GILBARCO 45LPM - ELETRÔNICA DUPLA": 9980.0,
    "BOMBA ABASTECIMENTO GILBARCO 110LPM - ELETRÔNICA ANTI-EXPLOSÃO": 13490.0,
    "BOMBA ABASTECIMENTO WAYNE 3G 50LPM - ELETRÔNICA SIMPLES": 13290.0,
    "BOMBA ABASTECIMENTO WAYNE 3G 50LPM - ELETRÔNICA DUPLA": 17480.0,
    "BOMBA ABASTECIMENTO WAYNE GLOBAL 50LPM - ELETRÔNICA DUPLA": 19790.0,
    "INDUSTRIAL MECÂNICA 90 LPM - DIESEL": 9690.0,
    "INDUSTRIAL MECÂNICA ANTI-EXPLOSÃO 90LPM": 15190.0,
    "SKID ABASTECIMENTO TRIF. 60LPM": 7890.0,
    "SKID ABASTECIMENTO TRIF. 60LPM DUPLA FILTRAGEM": 9890.0,
}

# ==================== FILTROS ====================
FILTROS: Dict[str, float] = {
    "SEM FILTRO": 0.0,
    "Filtro de 1'' para Filtragem de Partículas Gp Company": 350.00,
    "FOGUETINHO DESIDATRADOR 60LPM": 2190.0,
    "FOGUETINHO DESIDATRADOR 100LPM": 4190.0,
    "FOGUETINHO DESIDATRADOR 150LPM": 5190.0,
    "FOGUETINHO COALESCENTE 100LPM": 5890.0,
    "FOGUETINHO DESIDATRADOR DUPLO 100LPM": 6780.0,
}

# ==================== ELEMENTOS FILTRANTES ====================
ELEMENTOS: Dict[str, float] = {
    "SEM ELEMENTO": 0.0,
    "ELEMENTO FILTRANTE 1'' DESIDATRADOR - 4UN": 190.0,
    "ELEMENTO FILTRANTE 1'' DESIDATRADOR - 8UN": 350.0,
    "ELEMENTO FILTRANTE 1'' DESIDATRADOR - 12UN": 429.0,
}

# ==================== PRODUTOS OPCIONAIS ====================
# Marque com checkbox na tela. Cada item pode ter preço editável.
# "imagem": caminho opcional da foto (None se não tiver)
OPCIONAIS: Dict[str, Dict[str, Any]] = {
    "DESCARGA SELADA 4''": {
        "preco": 3500.0,
        "descricao": (
            "Abastecimento do combustível no tanque realizado por baixo, "
            "pela válvula. Caso não opte por esta forma, o abastecimento "
            "será pela parte superior do tanque."
        ),
        # Prefira nome de arquivo SEM espaços e SEM aspas: descarga_selada_4.jpg
        "imagem": "imagens_produtos/opcionais/descarga_selada_4.jpg",
    },
    # Adicione mais opcionais abaixo, no mesmo formato:
    # "NOME DO OPCIONAL": {
    #     "preco": 0.0,
    #     "descricao": "Texto explicativo que aparece no PDF.",
    #     "imagem": "imagens_produtos/opcionais/foto.jpg",
    # },
}

# ==================== VENDEDORES (inicial) ====================
VENDEDORES_INICIAL: List[str] = [
    "Elvio Martins",
    "Ana Lívia Godoy",
]

# ==================== DADOS DA EMPRESA ====================
EMPRESA = {
    "nome": "Casa do Frentista",
    "marca_equipamentos": "GP Company",
    "endereco": "Estrada Porto Grande, 1771",
    "cep": "89245-000",
    "cidade": "Araquari - SC",
    "cnpj": "21.463.174/0002-41",
    "telefone": "",  # preencher se tiver
    "email": "",
    "site": "https://www.casadofrentista.com.br",
    "whatsapp": "",  # só números com DDI, ex: 5547999999999
    "ncm": "7309.90.00",
    "norma": "NBR 15.461",
    "garantia_meses": 6,
    "prazo_fabricacao": "15 à 30 dias",
}

# Textos padrão
TEXTOS = {
    "acompanha": "Data book; ART; Desenho orientativo; Certificado de qualidade dos materiais; Relatório de teste de estanqueidade.",
    "tratamento_interno_tanque": "Limpeza Mecânica",
    "tratamento_externo": "Fundo Primer anticorrosivo, acabamento em esmalte sintético cor cinza",
    "pressao": "Atmosférica",
    "temperatura": "Ambiente",
    "fluido_padrao": "Diesel",
}

# Templates rápidos (preenche seleções na tela)
TEMPLATES = {
    "— Manual (sem template) —": None,
    "Frota padrão 10.000L + Bacia": {
        "tanque": "10.000L",
        "bacia": "10.000L",
        "bomba": "BOMBA ABASTECIMENTO 60LPM - 220V",
        "filtro": "SEM FILTRO",
        "elemento": "SEM ELEMENTO",
    },
    "Agro 20.000L + Bacia": {
        "tanque": "20.000L",
        "bacia": "20.000L",
        "bomba": "BOMBA ABASTECIMENTO 60LPM - 220V",
        "filtro": "FOGUETINHO DESIDATRADOR 100LPM",
        "elemento": "SEM ELEMENTO",
    },
    "Compacto 5.000L + Bacia": {
        "tanque": "5.000L",
        "bacia": "5.000L",
        "bomba": "SEM BOMBA",
        "filtro": "SEM FILTRO",
        "elemento": "SEM ELEMENTO",
    },
}

# Ordem alinhada à tabela ICMS interestadual 2025 (fiscal.io)
UFS_BRASIL = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RN", "RS", "RJ", "RO", "RR", "SC",
    "SP", "SE", "TO",
]

# Empresa em Araquari-SC
UF_ORIGEM_PADRAO = "SC"

# Alíquota interna (mesmo estado) — diagonal da tabela ICMS 2025
ICMS_INTERNA = {
    "AC": 19.0, "AL": 19.0, "AM": 20.0, "AP": 18.0, "BA": 20.5, "CE": 20.0,
    "DF": 20.0, "ES": 17.0, "GO": 19.0, "MA": 22.0, "MT": 17.0, "MS": 17.0,
    "MG": 18.0, "PA": 19.0, "PB": 20.0, "PR": 19.5, "PE": 20.5, "PI": 21.0,
    "RN": 18.0, "RS": 17.0, "RJ": 20.0, "RO": 19.5, "RR": 20.0, "SC": 17.0,
    "SP": 18.0, "SE": 19.0, "TO": 20.0,
}

# Matriz interestadual completa 27×27 — Tabela Alíquota ICMS 2025 (fiscal.io)
# ICMS_MATRIZ[origem][destino] = alíquota %  |  diagonal = interna
_UFS = UFS_BRASIL
_ROWS = {
    "AC": [19, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "AL": [12, 19, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "AM": [12, 12, 20, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "AP": [12, 12, 12, 18, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "BA": [12, 12, 12, 12, 20.5, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "CE": [12, 12, 12, 12, 12, 20, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "DF": [12, 12, 12, 12, 12, 12, 20, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "ES": [12, 12, 12, 12, 12, 12, 12, 17, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "GO": [12, 12, 12, 12, 12, 12, 12, 12, 19, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "MA": [12, 12, 12, 12, 12, 12, 12, 12, 12, 22, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "MT": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 17, 7, 7, 7, 7, 7, 12, 7, 7, 7, 12, 7, 7, 12, 7, 12, 7],
    "MS": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 17, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "MG": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 18, 7, 12, 7, 7, 7, 12, 7, 7, 7, 12, 7, 12, 7, 7],
    "PA": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 19, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "PB": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 20, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "PR": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 7, 19.5, 7, 7, 7, 12, 12, 7, 7, 12, 7, 12, 7],
    "PE": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 20.5, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "PI": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 21, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "RN": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 18, 12, 12, 12, 12, 12, 12, 12, 12],
    "RS": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 7, 12, 7, 7, 7, 17, 7, 7, 12, 7, 12, 7, 7],
    "RJ": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 7, 12, 7, 7, 7, 12, 20, 7, 7, 12, 7, 12, 7],
    "RO": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 19.5, 12, 12, 12, 12, 12],
    "RR": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 20, 12, 12, 12, 12],
    "SC": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 7, 12, 7, 7, 7, 12, 12, 7, 7, 12, 7, 17, 7, 7, 7],
    "SP": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 7, 12, 7, 7, 7, 12, 7, 7, 12, 7, 18, 7, 7],
    "SE": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 19, 12],
    "TO": [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 20],
}
ICMS_MATRIZ = {o: {_UFS[i]: float(_ROWS[o][i]) for i in range(27)} for o in _UFS}


def aliquota_interna(uf: str) -> float:
    return float(ICMS_INTERNA.get(uf, 18.0))


def aliquota_interestadual(origem: str, destino: str) -> float:
    """Retorna alíquota da matriz ICMS 2025 (interna se origem == destino)."""
    if not origem or not destino:
        return 12.0
    if origem in ICMS_MATRIZ and destino in ICMS_MATRIZ[origem]:
        return float(ICMS_MATRIZ[origem][destino])
    if origem == destino:
        return aliquota_interna(destino)
    return 12.0


def calcular_difal(
    valor_nf: float,
    uf_destino: str,
    uf_origem: str = UF_ORIGEM_PADRAO,
) -> dict:
    """
    Estimativa comercial de DIFAL (produtos nacionais), matriz ICMS 2025 completa:

        DIFAL = valor_NF × (alíquota interna DESTINO − alíquota interestadual origem→destino) / 100

    Mesmo estado: DIFAL = 0. Orientativo — validar com o fiscal na NF.
    """
    resultado = {
        "uf_origem": uf_origem or UF_ORIGEM_PADRAO,
        "uf_destino": uf_destino or "",
        "aliquota_interna_destino": 0.0,
        "aliquota_interestadual": 0.0,
        "diferenca_pp": 0.0,
        "valor_base": float(valor_nf or 0),
        "valor_difal": 0.0,
        "aplica": False,
        "observacao": "",
    }
    if not uf_destino or uf_destino in ("—", "-"):
        resultado["observacao"] = "Informe a UF de destino para calcular o DIFAL."
        return resultado

    origem = uf_origem or UF_ORIGEM_PADRAO
    interna = aliquota_interna(uf_destino)
    inter = aliquota_interestadual(origem, uf_destino)
    resultado["aliquota_interna_destino"] = interna
    resultado["aliquota_interestadual"] = inter

    if origem == uf_destino:
        resultado["observacao"] = (
            f"Operação interna ({origem}). Não há DIFAL interestadual. "
            f"Alíquota interna: {interna:.1f}%."
        )
        return resultado

    diff = interna - inter
    resultado["diferenca_pp"] = diff
    resultado["aplica"] = True
    if diff <= 0:
        resultado["valor_difal"] = 0.0
        resultado["observacao"] = (
            f"Diferença de alíquota ≤ 0 ({interna:.1f}% − {inter:.1f}%). DIFAL estimado zerado."
        )
        return resultado

    valor_difal = float(valor_nf or 0) * (diff / 100.0)
    resultado["valor_difal"] = round(valor_difal, 2)
    resultado["observacao"] = (
        f"DIFAL estimado = base × ({interna:.1f}% − {inter:.1f}%) = "
        f"R$ {resultado['valor_difal']:,.2f}. "
        f"Origem {origem} → destino {uf_destino}. Validar com o fiscal na NF."
    ).replace(",", "X").replace(".", ",").replace("X", ".")
    return resultado

# ==================== IMAGENS DOS PRODUTOS ====================
# Estrutura de pastas:
#   imagens_produtos/tanques/   → fotos dos tanques
#   imagens_produtos/bacias/    → fotos das bacias
#   imagens_produtos/bombas/    → fotos das bombas
#   imagens_produtos/filtros/   → fotos dos filtros
# Formatos: PNG ou JPG. Troque as fotos quando tiver as reais.

IMAGEM_PADRAO_TANQUE = "imagens_produtos/tanques/tanque_horizontal_1.png"
IMAGEM_PADRAO_BACIA = "imagens_produtos/bacias/bacia_padrao.png"
IMAGEM_PADRAO_BOMBA = "imagens_produtos/bombas/bomba_padrao.png"
IMAGEM_PADRAO_FILTRO = "imagens_produtos/filtros/filtro_padrao.png"

# --- Tanques por volume ---
IMAGEM_POR_TANQUE = {
    "1.000L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "3.000L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "4.000L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "5.000L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "6.000L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "7.500L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "10.000L": "imagens_produtos/tanques/tanque_horizontal_1.png",
    "12.000L": "imagens_produtos/tanques/tanque_horizontal_2.png",
    "14.900L": "imagens_produtos/tanques/tanque_horizontal_2.png",
    "20.000L": "imagens_produtos/tanques/tanque_bacia_1.png",
    "30.000L": "imagens_produtos/tanques/tanque_bacia_2.png",
    "BIPARTIDO 14.950L": "imagens_produtos/tanques/tanque_horizontal_2.png",
}

# --- Bacias por volume ---
IMAGEM_POR_BACIA = {
    "SEM BACIA": None,
    "1.000L": "imagens_produtos/bacias/bacia_padrao.png",
    "3.000L": "imagens_produtos/bacias/bacia_padrao.png",
    "4.000L": "imagens_produtos/bacias/bacia_padrao.png",
    "5.000L": "imagens_produtos/bacias/bacia_padrao.png",
    "6.000L": "imagens_produtos/bacias/bacia_padrao.png",
    "7.500L": "imagens_produtos/bacias/bacia_padrao.png",
    "10.000L": "imagens_produtos/bacias/bacia_com_tanque.png",
    "12.000L": "imagens_produtos/bacias/bacia_com_tanque.png",
    "15.000L": "imagens_produtos/bacias/bacia_com_tanque.png",
    "20.000L": "imagens_produtos/bacias/bacia_com_tanque.png",
    "30.000L": "imagens_produtos/bacias/bacia_com_tanque.png",
}

# --- Bombas (por nome do produto) ---
IMAGEM_POR_BOMBA = {
    "SEM BOMBA": None,
    # Todas usam a mesma foto por enquanto — troque quando tiver fotos específicas
    "BOMBA ABASTECIMENTO 60LPM - 220V": "imagens_produtos/bombas/bomba_padrao.png",
    "BOMBA ABASTECIMENTO GILBARCO 45LPM - ELETRÔNICA SIMPLES": "imagens_produtos/bombas/bomba_padrao.png",
    "BOMBA ABASTECIMENTO GILBARCO 45LPM - ELETRÔNICA DUPLA": "imagens_produtos/bombas/bomba_padrao.png",
    "BOMBA ABASTECIMENTO GILBARCO 110LPM - ELETRÔNICA ANTI-EXPLOSÃO": "imagens_produtos/bombas/bomba_padrao.png",
    "BOMBA ABASTECIMENTO WAYNE 3G 50LPM - ELETRÔNICA SIMPLES": "imagens_produtos/bombas/bomba_padrao.png",
    "BOMBA ABASTECIMENTO WAYNE 3G 50LPM - ELETRÔNICA DUPLA": "imagens_produtos/bombas/bomba_padrao.png",
    "BOMBA ABASTECIMENTO WAYNE GLOBAL 50LPM - ELETRÔNICA DUPLA": "imagens_produtos/bombas/bomba_padrao.png",
    "INDUSTRIAL MECÂNICA 90 LPM - DIESEL": "imagens_produtos/bombas/bomba_padrao.png",
    "INDUSTRIAL MECÂNICA ANTI-EXPLOSÃO 90LPM": "imagens_produtos/bombas/bomba_padrao.png",
    "SKID ABASTECIMENTO TRIF. 60LPM": "imagens_produtos/bombas/bomba_padrao.png",
    "SKID ABASTECIMENTO TRIF. 60LPM DUPLA FILTRAGEM": "imagens_produtos/bombas/bomba_padrao.png",
}

# --- Filtros ---
IMAGEM_POR_FILTRO = {
    "SEM FILTRO": None,
    "Filtro de 1'' para Filtragem de Partículas Gp Company": "imagens_produtos/filtros/5332-1-filtro de linha.jpg",
    "FOGUETINHO DESIDATRADOR 60LPM": "imagens_produtos/filtros/filtro_padrao.png",
    "FOGUETINHO DESIDATRADOR 100LPM": "imagens_produtos/filtros/filtro_padrao.png",
    "FOGUETINHO DESIDATRADOR 150LPM": "imagens_produtos/filtros/filtro_padrao.png",
    "FOGUETINHO COALESCENTE 100LPM": "imagens_produtos/filtros/filtro_padrao.png",
    "FOGUETINHO DESIDATRADOR DUPLO 100LPM": "imagens_produtos/filtros/filtro_padrao.png",
}


def get_imagem_tanque(tanque_key: str):
    """Caminho da foto do tanque (ou padrão)."""
    return IMAGEM_POR_TANQUE.get(tanque_key, IMAGEM_PADRAO_TANQUE)


def get_imagem_bacia(bacia_key: str):
    """Caminho da foto da bacia (None se SEM BACIA)."""
    return IMAGEM_POR_BACIA.get(bacia_key, IMAGEM_PADRAO_BACIA)


def get_imagem_bomba(bomba_key: str):
    """Caminho da foto da bomba (None se SEM BOMBA)."""
    return IMAGEM_POR_BOMBA.get(bomba_key, IMAGEM_PADRAO_BOMBA)


def get_imagem_filtro(filtro_key: str):
    """Caminho da foto do filtro (None se SEM FILTRO)."""
    return IMAGEM_POR_FILTRO.get(filtro_key, IMAGEM_PADRAO_FILTRO)


def get_imagens_selecionadas(tanque_key: str, bacia_key: str, bomba_key: str, filtro_key: str):
    """
    Retorna lista de (titulo, caminho) das imagens dos produtos selecionados.
    Títulos completos — sem corte — para legenda na tela e no PDF.
    """
    imgs = []
    t = get_imagem_tanque(tanque_key)
    if t:
        imgs.append((f"Tanque {tanque_key}", t))
    b = get_imagem_bacia(bacia_key)
    if b:
        imgs.append((f"Bacia {bacia_key}", b))
    bo = get_imagem_bomba(bomba_key)
    if bo:
        imgs.append((bomba_key, bo))  # nome completo da bomba
    f = get_imagem_filtro(filtro_key)
    if f:
        imgs.append((filtro_key, f))  # nome completo do filtro
    return imgs
