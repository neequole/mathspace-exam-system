import unittest

from models import *


EXAM_NAME = 'Math'
EXAM_DATE = '2017-12-12'


class TestExamModel(unittest.TestCase):
    def setUp(self):
        self.test_exam = Exam(EXAM_NAME, EXAM_DATE)

    def test_required_name(self):
        with self.assertRaises(TypeError):
            Exam(exam_date=EXAM_DATE)

    def test_required_exam_date(self):
        with self.assertRaises(TypeError):
            Exam(name=EXAM_NAME)

    def test_default_num_questions(self):
        self.assertEqual(
            self.test_exam.num_questions, Exam.DEFAULT_NUM_QUESTIONS)

    def test_default_questions(self):
        self.assertEqual(self.test_exam.questions, [])

    def test_add_questions_success(self):
        test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, 'Test question')
        self.test_exam.add_question(test_question)
        self.assertEqual(test_question.exam, self.test_exam)
        self.assertEqual(len(self.test_exam.questions), 1)

    def test_add_questions_max_questions_reached(self):
        test_exam = Exam(EXAM_NAME, EXAM_DATE, 1)  # change max no of questions
        test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, 'Test question')
        test_exam.add_question(test_question)
        with self.assertRaises(AssertionError):
            test_exam.add_question(test_question)
