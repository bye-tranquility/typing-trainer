import time


class Timer:
    def __init__(self):
        self.start_time: int = 0
        self.running: bool = False

    def start(self) -> None:
        if not self.running:
            self.running = True
            self.start_time = time.time()

    def stop(self) -> None:
        self.running = False

    def elapsed_time(self) -> float:
        return time.time() - self.start_time

    def is_running(self) -> bool:
        return self.running
