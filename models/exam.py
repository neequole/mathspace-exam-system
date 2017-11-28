class Exam(object):
    DEFAULT_NUM_QUESTIONS = 10

    def __init__(self, name, exam_date, num_questions=DEFAULT_NUM_QUESTIONS):
        self.name = name
        self.exam_date = exam_date  # TODO: date validation
        self.num_questions = num_questions
        self.questions = []

    def add_question(self, question):
        assert len(self.questions) < self.num_questions, \
            'Max no. of questions reached'
        question.exam = self
        self.questions.append(question)

    def get_min_possible_mark(self):
        total = 0
        for question in self.questions:
            total += question.incorrect_score
        return total
