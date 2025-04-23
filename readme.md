# AWS Lambda - Benchmark de Modelos de LLM com AWS Lambda

## 👨‍💻 Projeto desenvolvido por: 
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* [📚 Contextualização do projeto](#-contextualização-do-projeto)
* [🛠️ Tecnologias/Ferramentas utilizadas](#%EF%B8%8F-tecnologiasferramentas-utilizadas)
* [🖥️ Funcionamento do sistema](#%EF%B8%8F-funcionamento-do-sistema)
   * [🧩 Parte 1 - Backend](#parte-1---backend)
* [🔀 Arquitetura da aplicação](#arquitetura-da-aplicação)
* [📁 Estrutura do projeto](#estrutura-do-projeto)
* [📌 Como executar o projeto](#como-executar-o-projeto)
* [🕵️ Dificuldades Encontradas](#%EF%B8%8F-dificuldades-encontradas)

## 📚 Contextualização do projeto

Este projeto tem como objetivo realizar o **benchmark de modelos de linguagem natural (LLM)** utilizando **AWS Lambda**. Ele processa arquivos de entrada, como planilhas e CSVs, para avaliar a acurácia de predições geradas por modelos de NLP, comparando-as com dados de validação.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/AWS-Lambda-FF9900?logo=amazonaws&logoColor=white">](https://aws.amazon.com/lambda/)
[<img src="https://img.shields.io/badge/Boto3-0073BB?logo=amazonaws&logoColor=white">](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[<img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white">](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)

## 🖥️ Funcionamento do sistema

### 🧩 Parte 1 - Backend

O backend foi desenvolvido em **Python** e utiliza **AWS Lambda** para executar funções serverless. Ele é responsável por:

* **Gerenciamento de arquivos no S3**:
   - Upload e download de arquivos utilizando a classe [`S3BucketClass`](services/s3bucket_services.py).
   - Listagem e manipulação de objetos no bucket S3.
* **Avaliação de modelos**:
   - A classe [`EvaluationModel`](controller/evaluation_model.py) realiza a leitura de arquivos CSV e Excel, valida colunas e calcula a acurácia entre predições e validações.
* **Execução da lógica principal**:
   - A função [`lambda_handler`](lambda_handler.py) orquestra o fluxo de execução, incluindo o download de arquivos, avaliação de modelos e retorno dos resultados.

## 🔀 Arquitetura da aplicação

A aplicação segue uma arquitetura modular, com as seguintes responsabilidades:

1. **Serviços AWS**:
   - Gerenciamento de arquivos no S3 utilizando a biblioteca **Boto3**.
2. **Avaliação de Modelos**:
   - Processamento de dados e cálculo de métricas de desempenho.
3. **Execução Serverless**:
   - Uso de **AWS Lambda** para execução escalável e sem necessidade de gerenciamento de servidores.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── controller/
│   ├── evaluation_model.py
├── services/
│   ├── s3bucket_services.py
├── utils/
│   ├── check_aws.py
│   ├── import_credentials.py
├── tmp/
│   ├── results.csv
│   ├── outputs_classified/
│       ├── sonnet_results_classified.xlsx
├── lambda_handler.py
├── .env
├── .env.example
├── readme.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rafael-torres-nantes/aws-lambda-benchmark-llm.git
   ```

2. **Configure as credenciais AWS:**
   - Preencha o arquivo `.env` com suas credenciais AWS e o nome do bucket S3.

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a função Lambda localmente:**
   ```bash
   python lambda_handler.py
   ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento, algumas dificuldades foram enfrentadas, como:

- **Gerenciamento de arquivos no S3**: Garantir que os arquivos fossem manipulados corretamente, incluindo a criação de URLs pré-assinadas.
- **Validação de dados**: Ajustar o processamento de arquivos CSV e Excel para lidar com diferentes formatos e colunas.
- **Execução serverless**: Configurar e testar a execução da função Lambda localmente antes de implantá-la na AWS.
```
