class Choice(object):
    def __init__(self, text, question=None, is_valid=False):
        self.text = text
        self.question = None  # Allow orphaned choice
        if question:
            question.add_choice(self)
        self.is_valid = is_valid
