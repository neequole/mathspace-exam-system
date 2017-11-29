class Choice(object):
    def __init__(self, text, question=None, is_valid=False):
        self.text = text
        self.is_valid = is_valid
        self.question = None  # Allow orphaned choice
        if question:
            question.add_choice(self)
