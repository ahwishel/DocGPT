from typing import Self, IO
from service.input.input import Input
from PyPDF2 import PdfReader


class PDFInput(Input):
    def from_string(self, string: str) -> Self:
        return string

    def from_file(self, filename: str) -> PdfReader:
        return PdfReader(filename)
