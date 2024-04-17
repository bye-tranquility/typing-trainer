import tkinter as tk

FONT: str = 'Monospace'


class MyLabel(tk.Label):
    def __init__(self, frame, location, textvar):
        super().__init__(frame, textvariable=textvar, font=(FONT, 20), fg="grey")
        self.pack(side=location, padx=10, pady=5)


class MyButton(tk.Button):
    def __init__(self, frame, location, txt, command):
        super().__init__(frame, text=txt, font=(FONT, 12), command=command)
        self.pack(side=location, padx=8, pady=5)


class MyFrame(tk.Frame):
    def __init__(self, window, location):
        super().__init__(window)
        self.pack(side=location, expand=True, fill=tk.BOTH)
