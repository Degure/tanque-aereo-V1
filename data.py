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
    "Filtro de 1 polegada para Filtragem de Partículas Gp Company": 350.00,
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
    "site": "",
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
    "Filtro de 1 polegada para Filtragem de Partículas Gp Company": "imagens_produtos/filtros/5332-1-filtro de linha.jpg",
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
    Usado no preview da tela e no PDF.
    """
    imgs = []
    t = get_imagem_tanque(tanque_key)
    if t:
        imgs.append(("Tanque " + tanque_key, t))
    b = get_imagem_bacia(bacia_key)
    if b:
        imgs.append(("Bacia " + bacia_key, b))
    bo = get_imagem_bomba(bomba_key)
    if bo:
        imgs.append((bomba_key[:40], bo))
    f = get_imagem_filtro(filtro_key)
    if f:
        imgs.append((filtro_key[:40], f))
    return imgs
