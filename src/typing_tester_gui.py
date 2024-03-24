import tkinter as tk
from timer import Timer
from text_manager import TextManager

TITLE = "This is my typing trainer"
DEFAULT_STATS = "Stats \n0.00 CPM\n0.00 WPM"
FONT = 'Monospace'
FILENAME = '../assets/texts.txt'


class TypingTesterGUI:
    def __init__(self):
        self.timer = Timer()
        self.text_manager = TextManager(filename=FILENAME)

        self.window = tk.Tk()
        self.window.title(TITLE)
        self.window.geometry("800x400")
        self.window.minsize(width=800, height=400)
        self.frame = tk.Frame(self.window)
        self.create_widgets()
        self.frame.pack(expand=True)

        self.window.mainloop()

    def create_widgets(self) -> None:
        self.template_label = tk.Label(self.frame, text=self.text_manager.get_random_text(), font=(FONT, 24), fg="grey")
        self.template_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=(FONT, 24), highlightthickness=0)
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.handle_typing)
        self.input_entry.config(bg=self.frame.cget('bg'))

        self.speed_label = tk.Label(self.frame, text=DEFAULT_STATS, font=(FONT, 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="RESET", font=(FONT, 18), command=self.reset)
        self.reset_button.grid(row=3, column=0, padx=7, pady=10, sticky="e")

        self.quit_button = tk.Button(self.frame, text="QUIT", font=(FONT, 18), command=self.window.quit)
        self.quit_button.grid(row=3, column=1, padx=5, pady=10, sticky="w")

    def handle_typing(self, event):
        if not self.timer.is_running():
            self.timer.start()
            self.update_stats()

        if not self.template_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.template_label.cget('text') == self.input_entry.get():
            self.timer.stop()
            self.input_entry.config(fg="green")

    def reset(self):
        self.timer.stop()
        self.speed_label.config(text=DEFAULT_STATS)
        self.template_label.config(text=self.text_manager.get_random_text())
        self.input_entry.delete(0, tk.END)

    def calculate_stats(self):
        elapsed_time = self.timer.elapsed_time()
        cps = len(self.input_entry.get()) / elapsed_time
        cpm = cps * 60
        wps = len(self.input_entry.get().split(" ")) / elapsed_time
        wpm = wps * 60
        self.speed_label.config(text=f" Stats: \n{cpm:.2f} CPM\n{wpm:.2f} WPM")

    def update_stats(self):
        self.calculate_stats()
        if self.timer.is_running():
            self.window.after(100, self.update_stats)
