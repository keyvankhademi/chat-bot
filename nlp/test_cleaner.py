import unittest

from .cleaner import Cleaner


class TestCleaner(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(Cleaner.to_lower("Hello My name is Mike OXLONG"), "hello my name is mike oxlong")

    def test_spell_check(self):
        self.assertEqual(Cleaner.spell_check(['hwllo', 'goof']), ['hello', 'good'])

    def test_remove_punctuation(self):
        self.assertEqual(
            Cleaner.remove_punctuation("Hello, My name is Mike OXLONG!"),
            "Hello  My name is Mike OXLONG ",
        )

    def test_remove_stop_words(self):
        self.assertEqual(
            Cleaner.remove_stop_words(["my", "name", "is", "mike"]),
            ["name", "mike"],
        )

    def test_clean(self):
        self.assertEqual(
            Cleaner.clean("Hello, My name is Mike OXLONG!"),
            "hello name mike oblong",
        )

    def test_combine_synonyms(self):
        synonyms = Cleaner.combine_synonyms(['active', 'dead'])
        self.assertCountEqual(
            synonyms['active'],
            ['dynamic', 'fighting', 'combat-ready', 'active_voice', 'active_agent', 'participating', 'alive', 'active']
        )
        self.assertCountEqual(
            synonyms['dead'],
            ['dead', 'all_in', 'beat', 'bushed', 'numb', 'deadened', 'idle', 'stagnant', 'utter', 'drained', 'abruptly',
             'suddenly', 'short', 'absolutely', 'perfectly', 'utterly']
        )
