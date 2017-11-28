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
    DEFAULT_NUM_OPTIONS = 2
    DEFAULT_NUM_VALID_OPTIONS = 1
    CORRECT_SCORE_DEFAULT = 1
    INCORRECT_SCORE_GEOMETRY = 0
    INCORRECT_SCORE_ALGEBRA_SE = 0.33
    INCORRECT_SCORE_ALGEBRA = 0.5

    def __init__(self, topic, subtopic, text, exam=None,
                 num_options=DEFAULT_NUM_OPTIONS,
                 num_valid_options=DEFAULT_NUM_VALID_OPTIONS):
        self.exam = exam  # Allow orphaned question
        if self.exam:
            exam.add_question(self)
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
        return self.CORRECT_SCORE_DEFAULT

    @property
    def incorrect_score(self):
        if self.topic == QuestionTopic.GEOMETRY:
            return self.INCORRECT_SCORE_GEOMETRY
        elif self.topic == QuestionTopic.ALGEBRA:
            if self.subtopic == AlgebraSubTopic.SIMULTANEOUS_EQ:
                return self.INCORRECT_SCORE_ALGEBRA_SE
            else:
                return self.INCORRECT_SCORE_ALGEBRA

    def add_choice(self, choice):
        choice.question = self  # TODO: Validate num_options/num_valid_options
        self.choices.append(choice)

    def score_answer(self, answer):
        if answer in self.valid_choices:
            return self.correct_score
        else:
            return self.incorrect_score
