"""Module to record mouse events."""
from datetime import datetime
from enum import Enum

from pynput.mouse import Listener


class RecordMouseEvents:
    """Class to record mouse events.

    Methods:
        time(): Calculate time from start record to event.
        on_move(*args): Is called when mouse is moved.
        on_click(*args): Is called when mouse button is clicked.
        on_scroll(args): Is called when mouse scroll is moved.
        record(): Start record mouse events.

    """
    def __init__(self):
        """Record class constructor."""
        self.button_is_pressed = False
        self.events = []
        self.listener = None
        self.start_time = datetime.now()

    def time(self) -> float:
        """Calculate time from start record to event.

        Returns (float): Calculate time from start record to event.

        """
        return (datetime.now() - self.start_time).total_seconds()

    def on_move(self, coordinate_x, coordinate_y) -> dict:
        """Is called when mouse is moved.

        Args:
            coordinate_x (): vertical mouse cursor coordinate.
            coordinate_y (): horizontal mouse cursor coordinate.

        Returns (dict): with event type, coordinates and time.

        """

        return {
            'mouse_move': (
                {
                    'coordinate_x': coordinate_x,
                    'coordinate_y': coordinate_y,
                },
                {'time': self.time()},
            ),
        }

    def on_click(self, *_, button: Enum, pressed: bool) -> dict:
        """Is called when button mouse is clicked.

        Args:
            pressed (Enum): pressed key.
            button (bool): True while key is pressed, False while key is released.

        Returns (dict): with event type, coordinates, button, status and time.

        """

        return {
            'mouse_click': (
                {'button': str(button),
                 'pressed': pressed},
                {'time': self.time()},
            ),
        }

    def on_scroll(self, *_, vector_dx: int, vector_dy: int) -> dict:
        """Is called when mouse scroll is moved.

        Args:
           vector_dx (int): vertical scroll vector.
           vector_dy (int): horizontal scroll vector.

        Returns (dict): with event type, coordinates, scroll vector and time.

        """
        return {
            'mouse_scroll': (
                {
                    'vector_dx': vector_dx,
                    'vector_dy': vector_dy,
                },
                {'time': self.time()},
            ),
        }

    def record(self) -> list:
        """Start record mouse events.

        Returns (list): with recorded mouse events.

        """
        with Listener(
                on_move=self.events.append(self.on_move),
                on_click=self.events.append(self.on_click),
                on_scroll=self.events.append(self.on_scroll),
        ) as self.listener:
            self.listener.join()

        return self.events




