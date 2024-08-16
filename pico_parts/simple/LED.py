from machine import Pin
from pico_parts.abstract import AbstractLight


class LED(AbstractLight):

    def __repr__(self):
        return f"LED({self.led}, {self.led.value() == 1})"

    def __init__(self, led_pin: int):
        self.led = Pin(led_pin, Pin.OUT)

    def on(self, *args):
        self.led.on()

    def off(self, *args):
        self.led.off()

    def toggle(self, *args):
        self.led.value(not self.led.value())
