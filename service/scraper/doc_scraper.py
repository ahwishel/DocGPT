from abc import ABC, abstractmethod
from service.document.document import Document


class DocScraper(ABC):
    @abstractmethod
    def get_as_text(self, url: str) -> Document:
        pass
