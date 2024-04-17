import tkinter as tk
import os
from .timer import Timer
from .text_manager import TextManager

DEFAULT_STATS: str = "Stats \n0.00 CPM\n0.00 WPM"
FONT: str = 'Monospace'
TEXTS_SOURCE: str = 'assets/texts.txt'
STATS_FILE: str = 'tmp/stats.txt'
STATS_DIR: str = 'tmp'


class TextBox(tk.Text):
    def __init__(self, frame, template_textvar, stats_textvar):

        super().__init__(frame, bg="white smoke", height=20, width=50,
                         font=(FONT, 16), borderwidth=4)
        self.pack(expand=True, fill="both")

        self.bind("<KeyRelease>", self.handle_typing)
        self.timer = Timer()
        self.text_manager = TextManager(filename=TEXTS_SOURCE)

        self.template_textvar = template_textvar
        self.stats_textvar = stats_textvar

        self.screens = ['Congrats', 'Training']
        self.screen_ix: int = 0
        self.insert(tk.END, "Welcome to my typing trainer!\n\nPress any key to proceed.\n")

        self.mistakes: int = 0
        self.round: int = 0

    def change_status(self) -> None:
        self.screen_ix = (self.screen_ix + 1) % 2
        self.show()

    def show(self) -> None:
        self.config(state=tk.NORMAL)
        self.delete("0.0", tk.END)
        self.config(fg="black")
        screen = self.screens[self.screen_ix]
        if screen == "Congrats":
            self.insert(tk.END, "Good job!\n\nPress any key to load the next text.\n")
        elif screen == "Training":
            self.template_textvar.set(self.text_manager.get_random_text())
            self.stats_textvar.set(DEFAULT_STATS)

    def handle_typing(self, event) -> None:
        if self.screen_ix == 1 and self.cget("state") == tk.NORMAL:
            if not self.timer.is_running():
                self.timer.start()
                self.update_stats()

            if not self.template_textvar.get().startswith(self.get("1.0", tk.END).strip()):
                self.config(fg="red")
                self.mistakes += 1
            else:
                self.config(fg="black")

            if self.template_textvar.get() == self.get("1.0", tk.END).strip():
                self.timer.stop()
                self.round += 1
                self.config(fg="green")
                self.save_stats()
                self.mistakes = 0
                self.config(state=tk.DISABLED)
        else:
            self.change_status()

    def calculate_stats(self) -> None:
        elapsed_time = self.timer.elapsed_time()
        cps = len(self.get("1.0", tk.END)) / elapsed_time
        cpm = cps * 60
        wps = len(self.get("1.0", tk.END).split(" ")) / elapsed_time
        wpm = wps * 60
        self.stats_textvar.set(f"Stats: \n{cpm:.2f} CPM\n{wpm:.2f} WPM")

    def save_stats(self) -> None:
        stats = self.stats_textvar.get()[7:]
        if not os.path.exists(STATS_DIR):
            os.makedirs(STATS_DIR)
        with open(STATS_FILE, 'a') as file:
            file.write(f'ROUND {self.round}' + stats + '\n' + f"{self.mistakes} mistake(s)" + '\n' + '\n')

    def update_stats(self) -> None:
        self.calculate_stats()
        if self.timer.is_running():
            self.after(100, self.update_stats)

    def reset(self) -> None:
        self.mistakes = 0
        self.timer.stop()
        self.screen_ix = 1
        self.show()

    @staticmethod
    def cleanup() -> None:
        if os.path.exists(STATS_FILE):
            os.remove(STATS_FILE)
            os.rmdir(STATS_DIR)
