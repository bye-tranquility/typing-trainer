import tkinter as tk
import atexit
from .widgets import MyButton, MyLabel, MyFrame
from .results_window import ResultsWindow
from .text_box import TextBox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("The typing trainer")
        self.geometry("1000x800")
        self.minsize(width=1000, height=800)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        top_frame = MyFrame(self, tk.TOP)
        center_frame = MyFrame(self, tk.TOP)
        bottom_frame = MyFrame(self, tk.BOTTOM)

        template_textvar = tk.StringVar()
        template_textvar.set("<Some text to type>")
        stats_textvar = tk.StringVar()
        stats_textvar.set("<Your stats will appear here>")

        txt_box = TextBox(center_frame, template_textvar, stats_textvar)

        MyLabel(top_frame, tk.TOP, template_textvar)
        MyLabel(top_frame, tk.TOP, stats_textvar)

        MyButton(bottom_frame, tk.LEFT, "RESET", txt_box.reset)
        MyButton(bottom_frame, tk.RIGHT, "QUIT", self.quit)
        MyButton(bottom_frame, tk.LEFT, "RESULTS", lambda: ResultsWindow(self))
        MyButton(bottom_frame, tk.RIGHT, "LOAD FILE", txt_box.text_manager.load_file)

        atexit.register(TextBox.cleanup)
