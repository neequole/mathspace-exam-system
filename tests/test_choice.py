import unittest

from models import *


class TestChoiceModel(unittest.TestCase):
    def setUp(self):
        self.test_choice = Choice('2 and -2')

    def test_required_text(self):
        with self.assertRaises(TypeError):
            Choice()

    def test_default_question(self):
        self.assertIsNone(self.test_choice.question)

    def test_default_is_valid(self):
        self.assertEqual(self.test_choice.is_valid, False)
