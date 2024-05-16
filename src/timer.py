import time


class Timer:
    """
    Таймер, используемый для отслеживания прошедшего времени во время сессий печати.
    """
    def __init__(self):
        """
        Инициализирует таймер.
        """
        self.start_time: int = 0
        self.is_running: bool = False

    def start(self) -> None:
        """
        Запускает таймер.
        """
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()

    def stop(self) -> None:
        """
        Останавливает таймер.
        """
        self.is_running = False

    def elapsed_time(self) -> float:
        """
        Возвращает прошедшее время с момента запуска таймера.
        """
        return time.time() - self.start_time

    def running(self) -> bool:
        """
        Проверяет, работает ли в данный момент таймер.
        """
        return self.is_running
