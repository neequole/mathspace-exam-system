import csv

from .choice import Choice
from .question import Question


class Exam(object):
    DEFAULT_NUM_QUESTIONS = 10

    def __init__(self, name, exam_date, num_questions=DEFAULT_NUM_QUESTIONS):
        self.name = name
        self.exam_date = exam_date  # TODO: date validation
        self.num_questions = num_questions
        self.questions = []
        self.mark = {}

    def add_question(self, question):
        assert len(self.questions) < self.num_questions, \
            'Max no. of questions reached'
        question.exam = self
        self.questions.append(question)

    def get_question_by_number(self, number):
        # Credit to https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
        number = int(number)
        try:
            return (question for question in self.questions if
                    question.number == number).__next__()
        except StopIteration:
            return None

    def get_min_possible_mark(self):
        total = 0
        for question in self.questions:
            total += question.incorrect_score
        return total

    def import_from_csv(self, file_name):
        with open('assets/{}'.format(file_name), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                q = Question(row['Topic'], row['Subtopic'], row['Text'],
                             row['Question Number'], self)
                Choice(row['Option 1'], q)
                Choice(row['Option 2'], q)

    def export_to_csv(self, file_name):
        with open('assets/{}'.format(file_name), 'w', newline='') as csvfile:
            fieldnames = ['Question Number', 'Topic', 'Subtopic', 'Text',
                          'Option 1', 'Option 2']
            writer = csv.DictWriter(
                csvfile, quotechar='"', quoting=csv.QUOTE_NONNUMERIC,
                fieldnames=fieldnames)
            writer.writeheader()
            for question in self.questions:
                writer.writerow({
                    'Question Number': question.number,
                    'Topic': question.topic,
                    'Subtopic': question.subtopic,
                    'Text': question.text,
                    'Option 1': question.choices[0].text,
                    'Option 2': question.choices[1].text,
                })

    def mark_result(self, file_name):
        with open('assets/{}'.format(file_name), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                question = self.get_question_by_number(row['Question Number'])
                assert question, \
                    'Question {} not found'.format(row['Question Number'])
                current_score = self.mark.setdefault(row['Student Number'], 0)
                self.mark[row['Student Number']] = \
                    current_score + question.score_result(row['Result'])
