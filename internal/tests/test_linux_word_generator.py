"""
    Unit test for LinuxWordGenerator.
    Ensures that all the words with ' in them are dropped
"""
import builtins
from testslide import TestCase

# pylint: disable=import-error
from linux_word_generator import LinuxWordGenerator

# pylint: disable=too-few-public-methods
class MockFile:
    """
        Mock file, for when passing in specific dictionary
    """
    def __init__(self):
        self._dicitonary_string = "First\nSecond\nThird's\nFourth\n"
    def read(self):
        """
            set up to return a string broken up by \n
        """
        return self._dicitonary_string

class TestLinuxWordGenerator(TestCase):
    """
        Test class, ensures everything works
    """
    def setUp(self):
        """
            Mock out calls to open files, if the library determines that a file
            exists and wants to open it that is fine (i.e., an actual
            dictionary). If a made up dictionary is passed in, use the mock file
        """
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
        """
            Tests both a fake and real dictionary that the words returned don't
            have apostrophe's in them
        """
        real_word = self._real_dict.generate_word()
        fake_word = self._fake_dict.generate_word()

        self.assertNotIn("'", real_word)
        self.assertNotIn("'", fake_word)

    def test_generate_words(self):
        """
            Tests that both the fake and real dictionary will return the correct
            number of words. LinuxWordDictionary is set up so that
            generate_words repeatedly calls generate_word, so this test doesn't
            need to ensure no apostrophes
        """
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

    def test_no_dictionary(self):
        """
            This will test that if no dictionary is available,
            LinuxWordGenerator will throw a NameError
        """
        self.mock_callable("linux_word_generator", "isfile").to_return_value(False)

        with self.assertRaises(NameError):
            LinuxWordGenerator()
        with self.assertRaises(NameError):
            LinuxWordGenerator("made_up")
