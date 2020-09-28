#! /usr/bin/env python3
"""
    Command line interface for generating random words
"""

import argparse
from typing import Optional

from internal.ubuntu_word_generator import UbuntuWordGenerator, WordGeneratorInterface


def _set_up() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate random words")
    parser.add_argument(
       "-nw", "--num-words", dest="num_words", type=int, default=5
    )
    parser.add_argument(
        "-d", "--dictionary", dest="dictionary", type=Optional[str], default=None
    )
    return parser.parse_args()

def _get_generator(dictionary: Optional[str] = None) -> WordGeneratorInterface:
    return UbuntuWordGenerator(dict_location=dictionary)

args = _set_up()
gen = _get_generator(dictionary=args.dictionary)
words = gen.generate_words(num=args.num_words)
print(" ".join(words))
