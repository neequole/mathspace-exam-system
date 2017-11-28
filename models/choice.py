class Choice(object):
    def __init__(self, question, text, is_valid=False):
        self.question = question
        self.text = text
        self.is_valid = is_valid
