import unittest

from models import *


QUESTION_TEXT = 'Find x, x^2=4'


class TestQuestionModel(unittest.TestCase):
    def setUp(self):
        self.test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, QUESTION_TEXT, 1)

    def test_required_topic(self):
        with self.assertRaises(TypeError):
            Question(subtopic=AlgebraSubTopic.FRACTIONS.value,
                     text=QUESTION_TEXT, number=1)

    def test_required_subtopic(self):
        with self.assertRaises(TypeError):
            Question(topic=QuestionTopic.ALGEBRA.value, text=QUESTION_TEXT,
                     number=1)

    def test_required_text(self):
        with self.assertRaises(TypeError):
            Question(topic=QuestionTopic.ALGEBRA.value,
                     subtopic=AlgebraSubTopic.FRACTIONS.value, number=1)

    def test_required_number(self):
        with self.assertRaises(TypeError):
            Question(topic=QuestionTopic.ALGEBRA.value,
                     subtopic=AlgebraSubTopic.FRACTIONS.value,
                     text=QUESTION_TEXT)

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

    def test_invalid_topic(self):
        with self.assertRaises(AssertionError):
            Question('Geography', AlgebraSubTopic.FRACTIONS.value,
                     QUESTION_TEXT, 1)

    def test_invalid_algebra_topic(self):
        with self.assertRaises(AssertionError):
            Question(QuestionTopic.ALGEBRA.value, 'Addition', QUESTION_TEXT, 1)

    def test_invalid_geometry_topic(self):
        with self.assertRaises(AssertionError):
            Question(QuestionTopic.GEOMETRY.value, 'Map', QUESTION_TEXT, 1)

    def test_valid_choices(self):
        self.assertEqual(self.test_question.valid_choices, [])
        valid_choice = Choice('Test choice', is_valid=True)
        self.test_question.add_choice(valid_choice)
        self.assertIn(valid_choice, self.test_question.valid_choices)

    def test_correct_score_default(self):
        self.assertEqual(
            self.test_question.correct_score, Question.CORRECT_SCORE_DEFAULT)

    def test_incorrect_score_geometry(self):
        geometry_question = Question(
            QuestionTopic.GEOMETRY.value, GeometrySubTopic.CIRCLES.value,
            'Parallel lines:', 1)
        self.assertEqual(geometry_question.incorrect_score,
                         Question.INCORRECT_SCORE_GEOMETRY)

    def test_incorrect_score_algebra(self):
        self.assertEqual(
            self.test_question.incorrect_score,
            Question.INCORRECT_SCORE_ALGEBRA, 1)

    def test_incorrect_score_algebra_se(self):
        algebra_se_question = Question(
            QuestionTopic.ALGEBRA.value, AlgebraSubTopic.SIMULTANEOUS_EQ.value,
            'Solve x+y=10, x-y=4', 1)
        self.assertEqual(algebra_se_question.incorrect_score,
                         Question.INCORRECT_SCORE_ALGEBRA_SE)

    def test_add_choice_success(self):
        test_choice = Choice('Test choice')
        self.test_question.add_choice(test_choice)
        self.assertEqual(test_choice.question, self.test_question)
        self.assertEqual(len(self.test_question.choices), 1)

    def test_add_choice_max_choices_reached(self):
        test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, QUESTION_TEXT, 1, num_options=1)
        test_choice = Choice('Test choice', question=test_question)
        with self.assertRaises(AssertionError):
            test_question.add_choice(test_choice)

    def test_add_choice_max_valid_choices_reached(self):
        test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, QUESTION_TEXT, 1, num_options=2,
            num_valid_options=1)
        test_choice = Choice(
            'Test choice', question=test_question, is_valid=True)
        with self.assertRaises(AssertionError):
            test_question.add_choice(test_choice)

    def test_score_correct_answer(self):
        valid_choice = Choice('Test choice', question=self.test_question,
                              is_valid=True)
        self.assertEqual(self.test_question.score_answer(valid_choice),
                         Question.CORRECT_SCORE_DEFAULT)

    def test_score_incorrect_answer(self):
        invalid_choice = Choice('Test choice', question=self.test_question)
        self.assertEqual(self.test_question.score_answer(invalid_choice),
                         Question.INCORRECT_SCORE_ALGEBRA)
