from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def has_value(cls, value):
        # Credit to https://stackoverflow.com/questions/43634618/how-do-i-test-if-int-value-exists-in-python-enum-without-using-try-catch
        for item in cls:
            if item.value == value:
                return True
        return False


class QuestionTopic(CustomEnum):
    ALGEBRA = 'Algebra'
    GEOMETRY = 'Geometry'


class AlgebraSubTopic(CustomEnum):
    FRACTIONS = 'Fractions'
    QUADRATIC_EQ = 'Quadratic Equations'
    SIMULTANEOUS_EQ = 'Simultaneous Equations'


class GeometrySubTopic(CustomEnum):
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
        self.exam = None   # Allow orphaned question
        if exam:
            exam.add_question(self)
        assert QuestionTopic.has_value(topic), \
            'Invalid topic: {}'.format(topic)
        self.topic = topic
        if self.topic == QuestionTopic.ALGEBRA.value:
            assert AlgebraSubTopic.has_value(subtopic), \
                'Invalid Algebra subtopic: {}'.format(subtopic)
        else:
            assert GeometrySubTopic.has_value(subtopic), \
                'Invalid Geometry subtopic: {}'.format(subtopic)
        self.subtopic = subtopic
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
        if self.topic == QuestionTopic.GEOMETRY.value:
            return self.INCORRECT_SCORE_GEOMETRY
        elif self.topic == QuestionTopic.ALGEBRA.value:
            if self.subtopic == AlgebraSubTopic.SIMULTANEOUS_EQ.value:
                return self.INCORRECT_SCORE_ALGEBRA_SE
            else:
                return self.INCORRECT_SCORE_ALGEBRA

    def add_choice(self, choice):
        assert len(self.choices) < self.num_options, \
            'Max no of options reached'
        assert len(self.valid_choices) < self.num_valid_options, \
            'Max no of valid options reached'
        choice.question = self
        self.choices.append(choice)

    def score_answer(self, answer):
        if answer in self.valid_choices:
            return self.correct_score
        else:
            return self.incorrect_score
