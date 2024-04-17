import random
from tkinter import filedialog


class TextManager:
    def __init__(self, filename: str):
        self.filename = filename

    def get_random_text(self) -> str:
        with open(self.filename, 'r') as file:
            lines = file.read().split('\n')
            return random.choice(lines)

    def load_file(self) -> None:
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file_to_read:
                file_content = file_to_read.read()
            with open(self.filename, 'a') as file_to_write:
                file_to_write.write('\n' + file_content)
