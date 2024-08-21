from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def parse(self, filepath):
        pass

class TextParser(BaseParser):
    def parse(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        return content