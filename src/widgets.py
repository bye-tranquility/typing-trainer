import tkinter as tk
from .globals import Globals


class MyLabel(tk.Label):
    """
    Класс основного ярлыка, используемого в программе.
    """
    def __init__(self, frame, location, textvar):
        """
        Настраивает размеры, шрифт, задний фон, текст и положение в рамке
        """
        super().__init__(frame, textvariable=textvar, font=(Globals.FONT, 20), fg="grey")
        self.pack(side=location, padx=10, pady=5)


class MyButton(tk.Button):
    """
    Класс основной кнопки, используемой в программе.
    """
    def __init__(self, frame, location, txt, command):
        """
        Настраивает размеры, шрифт, команду, текст и положение в рамке.
        """
        super().__init__(frame, text=txt, font=(Globals.FONT, 12), command=command)
        self.pack(side=location, padx=8, pady=5)


class MyFrame(tk.Frame):
    """
   Класс основной рамки, используемой в программе.
   """
    def __init__(self, window, location):
        """
        Настраивает расположение в окне.
        """
        super().__init__(window)
        self.pack(side=location, expand=True, fill=tk.BOTH)
