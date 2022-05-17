import pandas as pd
from pandas import DataFrame

from ApplicationConstants import DATA_PATH
from services.model_service import ModelService


class DatabaseService:
    def __init__(self, model_service: ModelService):
        self.data = pd.read_csv(DATA_PATH + r'/data.csv', sep=";")
        self.model_service = model_service
        self.data['embeddings'] = self.data['text'].apply(self.model_service.get_embeddings)

    def get_data(self) -> DataFrame:
        """
        Get the full database as a DataFrame
        :return: DataFrame
        """
        return self.data

    def fetch_similar_sentence(self, request_text: str) -> DataFrame:
        """
        Retrieves a copy of the DataFrame where each of the entries is scored based on cosine similarity with the
        input request
        :param request_text: str
        :return: DataFrame
        """
        data = self.data.copy()
        request_text_embeddings = self.model_service.get_embeddings([request_text])
        data['score'] = data['embeddings'].apply(self.model_service.cos_sim, args=(request_text_embeddings, ))
        data.sort_values('score', ascending=False, inplace=True)
        return data

    def fetch_icd(self, request_text: str) -> str:
        """
        Returns the ICD Code of the  most similar entry in the DataFrame
        :param request_text: str
        :return: str
        """
        result = self.fetch_similar_sentence(request_text)
        return result.head(1)['icd_code'].values[0]
