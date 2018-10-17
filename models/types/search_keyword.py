from .basetype import BaseType
from .suggest_tokenizer import SuggestTokenizer


class SearchKeyword(BaseType):
    text: str
    suggestTokenizer: SuggestTokenizer

    def __init__(self, text: str = None, suggestTokenizer: SuggestTokenizer = None):
        self.text = text
        self.suggestTokenizer = suggestTokenizer
