from abc import ABC, abstractmethod
from service.document.document import Document


class Embedder(ABC):
    @abstractmethod
    def embed(self, documents: list[Document]) -> list[list[float]]:
        """Creates embeddings from a list of documents"""
        pass
