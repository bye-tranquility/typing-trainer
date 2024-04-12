import random

class TextManager:
    def __init__(self, filename):
        self.filename = filename

    def get_random_text(self) -> str:
        with open(self.filename, 'r') as file:
            lines = file.read().split('\n')
            return random.choice(lines)