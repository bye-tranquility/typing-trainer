import tkinter as tk
import os

FONT = 'Monospace'
STATS_FILE = '../tmp/stats.txt'


class ResultsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Previous Results")
        self.geometry("450x600")

        previous_stats = "No stats were generated."
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, 'r') as file:
                previous_stats = file.read()

        label = tk.Label(self, text="RESULTS OF THE PREVIOUS ROUNDS", font=(FONT, 18))
        label.pack(pady=10)
        stats_label = tk.Label(self, text=previous_stats, font=(FONT, 14))
        stats_label.pack(pady=5)
