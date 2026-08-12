# Sistema de Propostas Comerciais – Casa do Frentista / GP Company

Aplicação web em **Streamlit** + geração de **PDF profissional** para orçamentos de tanques aéreos, bacias, bombas e filtros.

## Funcionalidades

- Seleção de Tanque, Bacia, Bomba, Filtro e Elemento filtrante
- Preços editáveis (não travados)
- Desconto à vista configurável (padrão 5%)
- Frete e observações
- Gestão de vendedores (adicionar / remover)
- Três tipos de PDF:
  1. **Orçamento resumido** (1 página)
  2. **Proposta completa** (valores + especificações técnicas + condições/garantia/cláusulas)
  3. **Somente condições, garantias e cláusulas**
- Layout elegante com logos da Casa do Frentista e GP Company

## Como rodar localmente

```bash
# 1. Entre na pasta do projeto
cd pasta-do-projeto

# 2. Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate          # Linux/Mac
# ou
venv\Scripts\activate             # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`.

## Publicar de graça no Streamlit Cloud

1. Crie uma conta em [share.streamlit.io](https://share.streamlit.io)
2. Faça upload deste projeto para um repositório GitHub (pode ser privado)
3. Conecte o repositório no Streamlit Cloud
4. Deploy → pronto. Todos os vendedores usam a mesma URL sem conflito.

## Arquivos principais

| Arquivo            | Função                                      |
|--------------------|---------------------------------------------|
| `app.py`           | Interface Streamlit                         |
| `data.py`          | Preços, medidas e textos da empresa         |
| `pdf_generator.py` | Geração do PDF com ReportLab                |
| `vendedores.json`  | Lista de vendedores (editável pela interface)|
| `logo_casa.png`    | Logo Casa do Frentista                      |
| `logo_gp.png`      | Logo GP Company                             |

## Próximas melhorias possíveis

- Incluir imagens ilustrativas do tanque no PDF
- Campo de desconto por item individual
- Histórico de propostas geradas
- Integração com WhatsApp / e-mail
- Assinatura digital

---
Desenvolvido para uso interno da **Casa do Frentista**.
