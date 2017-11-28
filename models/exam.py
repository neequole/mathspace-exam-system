class Exam(object):
    DEFAULT_NUM_QUESTIONS = 10

    def __init__(self, name, exam_date, num_questions=DEFAULT_NUM_QUESTIONS):
        self.name = name
        self.exam_date = exam_date  # TODO: date validation
        self.num_questions = num_questions
        self.questions = []

    def add_question(self, question):
        question.exam = self  # TODO: validate number of question
        self.questions.append(question)

    def get_min_possible_mark(self):
        pass
