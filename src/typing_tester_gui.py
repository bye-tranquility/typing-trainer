import tkinter as tk
from timer import Timer
from text_manager import TextManager

TITLE = "This is my typing trainer"
DEFAULT_STATS = "Stats \n0.00 CPM\n0.00 WPM"
FONT = 'Monospace'
FILENAME = '../assets/texts.txt'


class MyLabel(tk.Label):
    def __init__(self, frame, location, textvar):
        super().__init__(frame, textvariable=textvar, font=(FONT, 20), fg="grey")
        self.pack(side=location, padx=10, pady=5)

class TextBox(tk.Entry):
    def __init__(self, frame, template_textvar, stats_textvar):
        super().__init__(frame, width=40, font=(FONT, 24), highlightthickness=0)
        self.pack(side=tk.TOP, padx=10, pady=5)
        self.bind("<KeyRelease>", self.handle_typing)
        self.config(bg=frame.cget('bg'))
        self.timer = Timer()
        self.text_manager = TextManager(filename=FILENAME)

        self.template_textvar = template_textvar
        self.stats_textvar = stats_textvar

        # Устанавливаем значение по умолчанию
        self.template_textvar.set(self.text_manager.get_random_text())
        self.stats_textvar.set(DEFAULT_STATS)

    def handle_typing(self, event):
        if self.screen_ix == 1 and self.cget("state") == tk.NORMAL:
            if not self.timer.is_running():
                self.timer.start()
                self.update_stats()

        if not self.template_textvar.get().startswith(self.get()):
            self.config(fg="red")
        else:
            self.config(fg="black")

        if self.template_textvar.get() == self.get():
            self.timer.stop()
            self.config(fg="green")

    def calculate_stats(self):
        elapsed_time = self.timer.elapsed_time()
        cps = len(self.get()) / elapsed_time
        cpm = cps * 60
        wps = len(self.get().split(" ")) / elapsed_time
        wpm = wps * 60
        self.speed_label.config(text=f" Stats: \n{cpm:.2f} CPM\n{wpm:.2f} WPM")

    def update_stats(self):
        self.calculate_stats()
        if self.timer.is_running():
            self.after(100, self.update_stats)

    def reset(self):
        self.timer.stop()
        self.stats_textvar.set(DEFAULT_STATS)
        self.template_textvar.set(self.text_manager.get_random_text())
        self.delete(0, tk.END)

class MyButton(tk.Button):
    def __init__(self, frame, location, txt, command):
        super().__init__(frame, text=txt, font=(FONT, 12), command=command)
        self.pack(side=location, padx=8, pady=5)

class MyFrame(tk.Frame):
    def __init__(self, window, location):
        super().__init__(window)
        self.pack(side=location, expand=True, fill=tk.BOTH) 
        
class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("This is my typing trainer")
        self.geometry("800x400")
        self.minsize(width=800, height=400)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        # Создаём Frame'ы
        top_frame = MyFrame(self, tk.TOP)
        center_frame = MyFrame(self, tk.TOP)
        bottom_frame = MyFrame(self, tk.BOTTOM)

        # Создаём StringVar'ы для Label'ов
        template_textvar = tk.StringVar()
        stats_textvar = tk.StringVar()

        # Инициализируем TextBox
        txt_box = TextBox(center_frame, template_textvar, stats_textvar)

        # Создаём Label'ы
        MyLabel(top_frame, tk.TOP, template_textvar)
        MyLabel(top_frame, tk.TOP, stats_textvar)

        # Cоздаём Button'ы
        MyButton(bottom_frame, tk.BOTTOM, "RESET", txt_box.reset)
        MyButton(bottom_frame, tk.BOTTOM, "QUIT", self.quit)
