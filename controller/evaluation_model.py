import pandas as pd

class EvaluationModel:
    def __init__(self):
        """
        Inicializa a classe EvaluationModel.
        """
        pass

    @staticmethod
    def read_csv(file_path):
        """
        Lê um arquivo CSV e retorna um DataFrame.
        
        Args:
            file_path (str): Caminho do arquivo CSV.
            
        Returns:
            pd.DataFrame: DataFrame contendo os dados do CSV.
        """
        return pd.read_csv(file_path)
    

    @staticmethod
    def read_excel(file_path):
        """
        Lê um arquivo Excel e retorna um DataFrame.
        
        Args:
            file_path (str): Caminho do arquivo Excel.
            
        Returns:
            pd.DataFrame: DataFrame contendo os dados do Excel.
        """
        return pd.read_excel(file_path)

    @staticmethod
    def validate_column_exists(dataframe, column_name):
        """
        Verifica se uma coluna existe no DataFrame.

        Args:
            dataframe (pd.DataFrame): DataFrame a ser verificado.
            column_name (str): Nome da coluna a ser verificada.
            
        Raises:
            ValueError: Se a coluna não existir no DataFrame.
        """
        if column_name not in dataframe.columns:
            raise ValueError(f"A coluna '{column_name}' não existe no DataFrame.")

    @staticmethod
    def transform_column_to_binary_prediction(dataframe, column_name, positive_value):
        """
        Transforma os valores de uma coluna em binário.
        Valores iguais a `positive_value` são transformados em 1, caso contrário em 0.

        Args:
            dataframe (pd.DataFrame): DataFrame a ser transformado.
            column_name (str): Nome da coluna a ser transformada.
            positive_value: Valor considerado positivo para transformação.

        Returns:
            pd.DataFrame: DataFrame com a coluna transformada.
        """
        dataframe[column_name] = dataframe[column_name].fillna(0)
        dataframe[column_name] = dataframe[column_name].apply(lambda x: 1 if x == positive_value else 0)
        return dataframe

    @staticmethod
    def transform_column_to_binary_validation(dataframe, column_name):
        """
        Transforma os valores de uma coluna em binário.
        Valores diferentes de 0 são transformados em 1, caso contrário em 0.

        Args:
            dataframe (pd.DataFrame): DataFrame a ser transformado.
            column_name (str): Nome da coluna a ser transformada.

        Returns:
            pd.DataFrame: DataFrame com a coluna transformada.
        """
        dataframe[column_name] = dataframe[column_name].fillna(0)
        dataframe[column_name] = dataframe[column_name].apply(lambda x: 1 if x != 0 else 0)
        return dataframe
    
    @staticmethod
    def calculate_accuracy(predictions, validations):
        """
        Calcula a acurácia comparando listas de predições e validações.

        Args:
            predictions (list): Lista de predições.
            validations (list): Lista de validações.
        
        Returns:
            float: Acurácia calculada como a proporção de predições corretas.
        """
        return sum([1 for p, v in zip(predictions, validations) if p == v]) / len(predictions)

    def model_benchmark(self, excel_file_path, validation_csv_path, column_prediction='Relevant', column_validation='Quick Hit?'):
        """
        Função para verificar a acurácia entre predições e validações.

        Args:
            prediction_csv_path (str): Caminho do CSV de predições.
            validation_csv_path (str): Caminho do CSV de validação.
            column_prediction (str): Nome da coluna de predições. Default é 'Relevancy'.
            column_validation (str): Nome da coluna de validação. Default é 'Quick Hit?'.

        Returns:
            dict: Dicionário contendo a acurácia calculada.
        """
        
        # Leitura dos CSVs
        dataframe_predictions = self.read_excel(excel_file_path)
        dataframe_validation = self.read_csv(validation_csv_path)

        # Validação das colunas
        self.validate_column_exists(dataframe_predictions, column_prediction)
        self.validate_column_exists(dataframe_validation, column_validation)

        # Verificação de valores únicos (opcional, para depuração)
        # print(f'[DEBUG] Valores únicos na coluna {column_prediction}: {dataframe_predictions[column_prediction].unique()}')
        # print(f'[DEBUG] Valores únicos na coluna {column_validation} de validação: {dataframe_validation[column_validation].unique()}')

        # Transformação das colunas em binário
        dataframe_predictions = self.transform_column_to_binary_prediction(dataframe_predictions, column_prediction, 'HIGHLY RELEVANT')
        dataframe_validation = self.transform_column_to_binary_validation(dataframe_validation, column_validation)

        # Obtenção das listas de valores
        predictions = dataframe_predictions[column_prediction].tolist()
        validations = dataframe_validation[column_validation].tolist()
        print(f'[DEBUG] Predições:  {predictions[:50]}...')
        print(f'[DEBUG] Validações: {validations[:50]}...')

        # Cálculo da acurácia
        accuracy = self.calculate_accuracy(predictions, validations)
        print(f'[DEBUG] Acurácia: {accuracy}')

        return {'accuracy': accuracy}