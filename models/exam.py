class Exam(object):
    def __init__(self, name, exam_date, num_questions=10):
        self.name = name
        self.exam_date = exam_date  # TODO: date validation
        self.num_questions = num_questions
        self.questions = []

    def add_question(self, question):
        question.exam = self
        self.questions.append(question)

    def get_min_possible_mark(self):
        pass
