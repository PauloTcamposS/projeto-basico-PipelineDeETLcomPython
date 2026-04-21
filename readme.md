# Pipeline ETL - Mensagens de Investimento 📈

Este projeto demonstra um fluxo básico de Engenharia de Dados utilizando o processo **ETL** (Extração, Transformação e Carga). O objetivo é processar uma lista de utilizadores e gerar mensagens personalizadas para o setor de investimentos.

## 🚀 Fluxo do Pipeline

1. **Extração (Extract):** O pipeline lê os dados brutos de um ficheiro `ids.csv`.
2. **Transformação (Transform):** Os dados são processados para criar uma mensagem personalizada de marketing financeiro para cada ID de utilizador.
3. **Carga (Load):** Os resultados transformados são guardados num novo ficheiro `output.csv`.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Biblioteca principal para manipulação e estruturação dos dados.

## 📦 Como Instalar e Executar

1. Certifique-se de que tem o Python instalado no seu computador.
2. Instale as dependências necessárias utilizando o ficheiro de requisitos:
   ```bash
   pip install -r requirements.txt
