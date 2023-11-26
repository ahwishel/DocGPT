from service.document.document import Document
from service.embedder.embedder import Embedder
from langchain.embeddings import OpenAIEmbeddings


class AdaEmbedder(Embedder):
    def __init__(self):
        self.embedder = OpenAIEmbeddings()

    def embed(self, documents: list[Document]) -> list[list[float]]:
        pass