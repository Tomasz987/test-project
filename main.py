# pip install pynput
from pynput.mouse import Listener


class RecordMouseEvents:

    def __init__(self):
        self.events = []
        self.listener = None

    def on_move(self, *args):
        return args

    def on_click(self, *args):
        return args

    def on_scroll(self, *args):
        return args

    def record(self) -> list:
        """Start record mouse events.

        Returns (list): with recorded mouse events.

        """
        with Listener(
                on_move=lambda *args: self.events.append(self.on_move(*args)),
                on_click=lambda *args: self.events.append(self.on_click(*args)),
                on_scroll=lambda *args: self.events.append(self.on_scroll(*args)),
        ) as self.listener:
            self.listener.join()

        return self.events


if __name__ == "__main__":
    RecordMouseEvents().record()
