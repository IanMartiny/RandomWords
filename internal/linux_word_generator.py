from os.path import isfile
from random import choice
from typing import Optional, Set

from word_generator_interface import WordGeneratorInterface


DEFAULT_LOCATIONS = ["/usr/share/dict/words", "/usr/dict/words"]


class LinuxWordGenerator(WordGeneratorInterface):
    """
        Generate a set of random words using a provided dictionary or the linux
        default
    """
    def __init__(self, dict_location: Optional[str] = None) -> None:
        if dict_location and isfile(dict_location):
            with open(dict_location, 'r') as f:
                self._dictionary = f.read().splitlines()
        elif isfile(DEFAULT_LOCATIONS[0]):
            with open(DEFAULT_LOCATIONS[0], 'r') as f:
                self._dictionary = f.read().splitlines()
        elif isfile(DEFAULT_LOCATIONS[1]):
            with open(DEFAULT_LOCATIONS[1], 'r') as f:
                self._dictionary = f.read().splitlines()
        else:
            raise NameError("No valid dictionary found")

    def generate_word(self) -> str:
        """
            generate word from dictionary, assures no ' in word
        """
        word = ""
        while not word:
            tmp = choice(self._dictionary)
            if "'" not in tmp:
                word = tmp

        return word

    def generate_words(self, num: int) -> Set[str]:
        """
            generate a given number of distinct words from dictionary by calling
            generate_word numerous times
        """
        # random_words = set()
        # while len(random_words) != num:
        #     needed = num - len(random_words)
        #     tmp = sample(self._dictionary, needed)

        #     tmp = [x for x in tmp if "'" not in x]
        #     random_words.union(tmp)

        # return random_words
        random_words = set()
        while len(random_words) != num:
            random_words.add(self.generate_word())

        return random_words
