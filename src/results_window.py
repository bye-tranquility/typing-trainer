import tkinter as tk
import os
from .globals import Globals


class ResultsWindow(tk.Toplevel):
    """
    Окно статистики, вызываемое кнопкой RESULTS.
    """
    def __init__(self, parent):
        """
        Настраивает отображение запрашиваемой статистики.
        """
        super().__init__(parent)
        self.title("Previous Results")
        self.geometry("450x600")

        previous_stats = "No stats were generated."
        if os.path.exists(Globals.STATS_FILE):
            with open(Globals.STATS_FILE, 'r') as file:
                previous_stats = file.read()

        label = tk.Label(self, text="RESULTS OF THE PREVIOUS ROUNDS", font=(Globals.FONT, 18))
        label.pack(pady=10)
        stats_label = tk.Label(self, text=previous_stats, font=(Globals.FONT, 14))
        stats_label.pack(pady=5)
