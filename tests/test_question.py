import unittest

from models import *


QUESTION_TEXT = 'Find x, x^2=4'


class TestQuestionModel(unittest.TestCase):
    def setUp(self):
        self.test_question = Question(
            QuestionTopic.ALGEBRA, AlgebraSubTopic.FRACTIONS, QUESTION_TEXT)

    def test_required_topic(self):
        with self.assertRaises(TypeError):
            Question(subtopic=AlgebraSubTopic.FRACTIONS, text=QUESTION_TEXT)

    def test_required_subtopic(self):
        with self.assertRaises(TypeError):
            Question(topic=QuestionTopic.ALGEBRA, text=QUESTION_TEXT)

    def test_required_text(self):
        with self.assertRaises(TypeError):
            Question(topic=QuestionTopic.ALGEBRA,
                     subtopic=AlgebraSubTopic.FRACTIONS)

    def test_default_exam(self):
        self.assertIsNone(self.test_question.exam)

    def test_default_num_options(self):
        self.assertEqual(
            self.test_question.num_options, Question.DEFAULT_NUM_OPTIONS)

    def test_default_num_valid_options(self):
        self.assertEqual(
            self.test_question.num_valid_options,
            Question.DEFAULT_NUM_VALID_OPTIONS)

    def test_default_choices(self):
        self.assertEqual(self.test_question.choices, [])

    def test_valid_choices(self):
        self.assertEqual(self.test_question.valid_choices, [])
        valid_choice = Choice('Test choice', question=self.test_question,
                              is_valid=True)
        self.test_question.add_choice(valid_choice)
        self.assertIn(valid_choice, self.test_question.valid_choices)

    def test_correct_score_default(self):
        self.assertEqual(
            self.test_question.correct_score, Question.CORRECT_SCORE_DEFAULT)

    def test_incorrect_score_geometry(self):
        geometry_question = Question(
            QuestionTopic.GEOMETRY, GeometrySubTopic.CIRCLES,
            'Parallel lines:')
        self.assertEqual(geometry_question.incorrect_score,
                         Question.INCORRECT_SCORE_GEOMETRY)

    def test_incorrect_score_algebra(self):
        self.assertEqual(
            self.test_question.incorrect_score,
            Question.INCORRECT_SCORE_ALGEBRA)

    def test_incorrect_score_algebra_se(self):
        algebra_se_question = Question(
            QuestionTopic.ALGEBRA, AlgebraSubTopic.SIMULTANEOUS_EQ,
            'Solve x+y=10, x-y=4')
        self.assertEqual(algebra_se_question.incorrect_score,
                         Question.INCORRECT_SCORE_ALGEBRA_SE)

    def test_add_choice(self):
        test_choice = Choice('Test choice')
        self.test_question.add_choice(test_choice)
        self.assertEqual(test_choice.question, self.test_question)
        self.assertEqual(len(self.test_question.choices), 1)

    def test_score_correct_answer(self):
        valid_choice = Choice('Test choice', question=self.test_question,
                              is_valid=True)
        self.assertEqual(self.test_question.score_answer(valid_choice),
                         Question.CORRECT_SCORE_DEFAULT)

    def test_score_incorrect_answer(self):
        invalid_choice = Choice('Test choice', question=self.test_question)
        self.assertEqual(self.test_question.score_answer(invalid_choice),
                         Question.INCORRECT_SCORE_ALGEBRA)
