from typing import Self
from service.document.document import Document
from langchain.document_loaders import PyPDFLoader
from langchain.docstore.document import Document as LangchainDoc


class PDFDoc(Document):

    def __init__(self):
        self.document: PyPDFLoader | None = None
        self.pages: int = 0

    def create_doc(self, source: PyPDFLoader) -> Self:
        self.document = source

        return self

    def chunk(self) -> list[LangchainDoc]:
        return self.document.load_and_split()


