import builtins
from testslide import TestCase

from linux_word_generator import LinuxWordGenerator


class MockFile:
    def read(self):
        return "First\nSecond\nThird's\nFourth\n"

class TestLinuxWordGenerator(TestCase):
    def setUp(self):
        super().setUp()
        self.mock_callable(builtins, "open").for_call(
            "/usr/share/dict/words", 'r'
        ).to_call_original()
        self.mock_callable(builtins, "open").for_call(
            "/usr/dict/words", 'r'
        ).to_call_original()
        self.mock_callable(builtins, "open").for_call(
            "made_up_location", 'r'
        ).to_return_value(MockFile())
        self._real_dict = LinuxWordGenerator()
        self._fake_dict = LinuxWordGenerator(dict_location="made_up_location")

    def test_generate_word(self):
        real_word = self._real_dict.generate_word()
        fake_word = self._fake_dict.generate_word()

        self.assertNotIn("'", real_word)
        self.assertNotIn("'", fake_word)

    def test_generate_words(self):
        real_words = self._real_dict.generate_words(num=3)
        fake_words = self._fake_dict.generate_words(num=3)

        self.assertEqual(
            len(real_words),
            3,
            "Got a different number of words than requested from the real "
            "dictionary"
        )
        self.assertEqual(
            len(fake_words),
            3,
            "Got a different number of words than requested from the fake "
            "dictionary"
        )
