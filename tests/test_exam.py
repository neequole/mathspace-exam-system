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

    def test_get_min_possible_mark(self):
        test_exam = Exam(EXAM_NAME, EXAM_DATE)
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.FRACTIONS.value,
                 'dummy', exam=test_exam)  # 0.5
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.QUADRATIC_EQ.value,
                 'dummy', exam=test_exam)  # 0.5
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.SIMULTANEOUS_EQ.value,
                 'dummy', exam=test_exam)  # 0.33
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.SIMULTANEOUS_EQ.value,
                 'dummy', exam=test_exam)  # 0.33
        Question(QuestionTopic.GEOMETRY.value, GeometrySubTopic.CIRCLES.value,
                 'dummy', exam=test_exam)  # 0
        min_mark = 0.5 + 0.5 + 0.33 + 0.33 + 0
        self.assertEqual(test_exam.get_min_possible_mark(), min_mark)

    def test_get_min_possible_mark_from_csv(self):
        test_exam = Exam('Test CSV Exam', '2017-10-10')
        test_exam.import_from_csv('revision_exam_20171010.csv')
        self.assertEqual(test_exam.get_min_possible_mark(), 2.66)
