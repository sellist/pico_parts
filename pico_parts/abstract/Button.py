from abc import ABC, abstractmethod


class Button(ABC):

    def __init__(self):
        self.callback = None

    @abstractmethod
    def is_pressed(self, *args):
        pass

    @abstractmethod
    def on_press(self, *args):
        pass

    @abstractmethod
    def is_released(self, *args):
        pass

    @abstractmethod
    def __debounce(self):
        pass

    @property
    def callback(self):
        return self.callback

    @callback.setter
    def callback(self, callback):
        self.callback = callback

    @property
    def pin(self):
        return self.pin

    @pin.setter
    def pin(self, pin):
        self.pin = pin