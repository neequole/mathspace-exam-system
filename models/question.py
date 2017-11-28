from enum import Enum


class QuestionTopic(Enum):
    ALGEBRA = 'Algebra'
    GEOMETRY = 'Geometry'


class AlgebraSubTopic(Enum):
    FRACTIONS = 'Fractions'
    QUADRATIC_EQ = 'Quadratic Equations'
    SIMULTANEOUS_EQ = 'Simultaneous Equations'


class GeometrySubTopic(Enum):
    PARALLEL_LINES = 'Parallel Lines'
    CIRCLES = 'Circles'


class Question(object):
    def __init__(self, topic, subtopic, text, exam=None, num_options=2,
                 num_valid_options=1):
        self.exam = exam  # Allow orphaned question
        self.topic = topic  # TODO: Should be member of QuestionTopic
        self.subtopic = subtopic  # TODO: Should be member of SubTopic
        self.text = text
        self.num_options = num_options
        self.num_valid_options = num_valid_options
        self.choices = []

    @property
    def valid_choices(self):
        return list(filter(lambda choice: choice.is_valid, self.choices))

    @property
    def correct_score(self):
        return 1

    @property
    def incorrect_score(self):
        if self.topic == QuestionTopic.GEOMETRY:
            return 0
        elif self.topic == QuestionTopic.ALGEBRA:
            if self.subtopic == AlgebraSubTopic.SIMULTANEOUS_EQ:
                return 0.33
            else:
                return 0.5
        else:
            return 0

    def add_choice(self, choice):
        choice.question = self  # TODO: Validate num_options/num_valid_options
        self.choices.append(choice)

    def check_answer(self, answer):
        if answer in self.valid_choices:
            return self.correct_score
        else:
            return self.incorrect_score
