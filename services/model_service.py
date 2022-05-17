from typing import List

from numpy import float32
from sentence_transformers import SentenceTransformer, util
from torch import Tensor


class ModelService:
    def __init__(self):
        self.model = SentenceTransformer('Sahajtomar/German-semantic')

    def get_embeddings(self, sentences: List[str]) -> Tensor:
        """
        Retrieves embeddings for the input text
        :param sentences: List
        :return: Tensor
        """
        return self.model.encode(sentences, convert_to_tensor=True)

    @staticmethod
    def cos_sim(embeddings_1: Tensor, embeddings_2: Tensor) -> float32:
        """
        Calculates similarity between embeddings
        :param embeddings_1: Tensor
        :param embeddings_2: Tensor
        :return: float32
        """
        return util.pytorch_cos_sim(embeddings_1, embeddings_2).cpu().numpy()[0][0]
