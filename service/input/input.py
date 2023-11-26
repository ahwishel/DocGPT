from abc import ABC, abstractmethod
from typing import Self, IO


class Input(ABC):
    @abstractmethod
    def from_string(self, string: str) -> Self:
        """Create a source of input from a string"""
        pass

    @abstractmethod
    def from_file(self, filename: str) -> Self:
        """Create a source of input from a file"""
        pass
