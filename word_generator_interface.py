from typing import Set

class WordGeneratorInterface:
    """
        Generates random words, one at a time, or in a set
    """
    def generate_word(self) -> str:
        """
            Generate one word at a time
        """
        raise NotImplementedError

    def generate_words(self, num: int) -> Set[str]:
        """
            Generate a collection of distinct words all at once
        """
        raise NotImplementedError
