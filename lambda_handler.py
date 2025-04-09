import os
import json
import pandas as pd
from dotenv import load_dotenv

# Importar as classes de serviços necessárias para a Lambda Function
from services.s3bucket_services import S3BucketClass

# Importar a classe de avaliação de modelo
from controller.evaluation_model import EvaluationModel

load_dotenv()

# Obtém o nome do bucket do S3 do arquivo .env
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# Obtém o diretório de saída do S3 do arquivo .env
OUTPUT_FOLDER = 'outputs_classified/'

# ----------------------------------------------------------------------------
# Função Lambda para inferência de modelos de NLP e armazenamento no DynamoDB
# ----------------------------------------------------------------------------
def lambda_handler(event, context):

    # 1 - Imprime o evento recebido
    print('*********** Start Lambda ***************')
    print(f'[DEBUG] Event: {event}')

    # 2 - Instancia a classe S3 Bucket 
    s3bucket_service = S3BucketClass()
    
    # 3 - Instancia a classe EvaluationModel
    evaluation_model = EvaluationModel()

    try:
        # 4 - Lista os arquivos no S3 Bucket
        s3bucket_files = s3bucket_service.list_files(S3_BUCKET_NAME)
        print(f'[DEBUG] Arquivos no S3: {s3bucket_files}')

        # 5 - Filtra os arquivos que estão no root do S3 Bucket
        file_path_in_root = [file for file in s3bucket_files if '/' not in file]
        print(f'[DEBUG] Arquivos no root do S3: {file_path_in_root}')
    
        # 6 - Baixa o arquivo do S3 Bucket para o diretório temporário
        prediction_excel_file_paths = s3bucket_service.download_all_files(S3_BUCKET_NAME, OUTPUT_FOLDER, '.xlsx')
        print(f'[DEBUG] Arquivo baixado do S3 para: {prediction_excel_file_paths}')

        # 7 - Baixa o arquivo de validação do S3 Bucket para o diretório temporário
        validation_csv_path = s3bucket_service.download_file(S3_BUCKET_NAME, file_path_in_root)
        print(f'[DEBUG] Arquivo de validação baixado do S3 para: {validation_csv_path}')

        # 8 - Cria um dicionário para armazenar os resultados 
        results = {}

        # 9 - Envia os arquivos CSV para a função de benchmark
        for excel_file_path in prediction_excel_file_paths:
            print(f'[DEBUG] Analisando o EXCEL: {excel_file_path}')
            results[excel_file_path] = evaluation_model.model_benchmark(excel_file_path, validation_csv_path)
        
        # 10 - Retorna os resultados
        return {
            'statusCode': 200,
            'body': json.dumps(results)
        }

    except Exception as e:
        print(f"[DEBUG] Erro: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {e}')
        }


# Para teste local
if __name__ == "__main__":
    lambda_handler(None, None)