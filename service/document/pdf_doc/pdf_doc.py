from typing import Self
from service.document.document import Document
from PyPDF2 import PdfReader
from langchain.docstore.document import Document as LangchainDoc


class PDFDoc(Document):

    def __init__(self):
        self.document: PdfReader | None = None
        self.pages: int = 0

    def create_doc(self, source: PdfReader) -> Self:
        self.document = source

        return self

    def chunk(self) -> list[LangchainDoc]:
        return [LangchainDoc(page_content=page.extract_text()) for page in self.document.pages]


