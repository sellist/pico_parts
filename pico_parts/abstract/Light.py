from abc import ABC, abstractmethod


class AbstractLight(ABC):
    @abstractmethod
    def on(self, *args):
        pass

    @abstractmethod
    def off(self, *args):
        pass

    @abstractmethod
    def toggle(self, *args):
        pass
