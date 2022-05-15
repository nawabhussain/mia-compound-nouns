from sentence_transformers import SentenceTransformer, util


class ModelService:
    def __init__(self):
        self.model = SentenceTransformer('Sahajtomar/German-semantic')

    def get_embeddings(self, sentences):
        return self.model.encode(sentences, convert_to_tensor=True)

    @staticmethod
    def cos_sim(embeddings_1, embeddings_2):
        return util.pytorch_cos_sim(embeddings_1, embeddings_2)
