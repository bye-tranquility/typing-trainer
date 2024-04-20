import random
from tkinter import filedialog


class TextManager:
    """
    Управление загрузкой и извлечением случайных текстов для тренировки печати.
    """
    def __init__(self, filename: str):
        """
        Инициализирует объект с именем файла, содержащего текстовые отрывки.
        """
        self.filename = filename

    def get_random_text(self) -> str:
        """
        Возвращает случайный текстовый отрывок из загруженного файла.
        """
        with open(self.filename, 'r') as file:
            lines = file.read().split('\n')
            return random.choice(lines)

    def load_file(self) -> None:
        """
        Загрузка в банк текстов.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file_to_read:
                file_content = file_to_read.read()
            with open(self.filename, 'a') as file_to_write:
                file_to_write.write('\n' + file_content)
