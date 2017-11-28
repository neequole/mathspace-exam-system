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

    def test_default_mark(self):
        self.assertEqual(self.test_exam.mark, {})

    def test_add_questions_success(self):
        test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, 'Test question', 1)
        self.test_exam.add_question(test_question)
        self.assertEqual(test_question.exam, self.test_exam)
        self.assertEqual(len(self.test_exam.questions), 1)

    def test_add_questions_max_questions_reached(self):
        test_exam = Exam(EXAM_NAME, EXAM_DATE, 1)  # change max no of questions
        test_question = Question(
            QuestionTopic.ALGEBRA.value,
            AlgebraSubTopic.FRACTIONS.value, 'Test question', 1)
        test_exam.add_question(test_question)
        test_question.number = 2
        with self.assertRaises(AssertionError):
            test_exam.add_question(test_question)

    def test_get_min_possible_mark(self):
        test_exam = Exam(EXAM_NAME, EXAM_DATE)
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.FRACTIONS.value,
                 'dummy', 1, exam=test_exam)  # 0.5
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.QUADRATIC_EQ.value,
                 'dummy', 2, exam=test_exam)  # 0.5
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.SIMULTANEOUS_EQ.value,
                 'dummy', 3, exam=test_exam)  # 0.33
        Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.SIMULTANEOUS_EQ.value,
                 'dummy', 4, exam=test_exam)  # 0.33
        Question(QuestionTopic.GEOMETRY.value, GeometrySubTopic.CIRCLES.value,
                 'dummy', 5, exam=test_exam)  # 0
        min_mark = 0.5 + 0.5 + 0.33 + 0.33 + 0
        self.assertEqual(test_exam.get_min_possible_mark(), min_mark)

    def test_get_min_possible_mark_from_csv(self):
        test_exam = Exam('Test CSV Exam', '2017-10-10')
        test_exam.import_from_csv('revision_exam_20171010.csv')
        self.assertEqual(test_exam.get_min_possible_mark(), 2.66)

    def test_mark_result(self):
        test_exam = Exam('Test CSV Exam', '2017-10-10')
        test_exam.import_from_csv('revision_exam_20171010.csv')
        test_exam.mark_result('revision_exam_answers.csv')
        self.assertEqual(test_exam.mark['10001'],
                         sum([1, 1, 0.33, 1, 0.5, 1, 0, 1, 1, 0.5]))
        self.assertEqual(test_exam.mark['10005'],
                         test_exam.get_min_possible_mark())

    def test_get_average_mark(self):
        test_exam = Exam('Test CSV Exam', '2017-10-10')
        test_exam.import_from_csv('revision_exam_20171010.csv')
        test_exam.mark_result('revision_exam_answers.csv')
        marks = [7.33, 8.0,  7.33, 8, 2.66]
        self.assertEqual(test_exam.get_average_mark(), sum(marks)/len(marks))
