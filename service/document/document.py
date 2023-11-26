from abc import ABC, abstractmethod
from service.input.input import Input
from typing import Self


class Document(ABC):
    @abstractmethod
    def create_doc(self, source):
        """Create a document from an `Input` source"""
        pass

    @abstractmethod
    def chunk(self):
        """Break down the document into sizeable chunks"""
        pass
