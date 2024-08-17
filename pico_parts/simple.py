from machine import Timer, Pin, disable_irq, enable_irq
import abstract as abstract
from pico_parts.drivers import tm1637


class LED(abstract.Light):

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


class Button(abstract.Button):

    def __repr__(self):
        return f"Button({self.button}, {self.button.value() == 0})"

    def __init__(self, button_pin: int, callback=lambda: print("No callback set!")):
        self.button = Pin(button_pin, Pin.IN)
        self.callback = callback
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.on_press)
        self.button_bounces = 0
        self.cooling_down = False
        self.timer = Timer()

    def on_press(self, *args):
        irq_state = disable_irq()
        if self.cooling_down:
            enable_irq(irq_state)
            return
        enable_irq(irq_state)
        self.__debounce()
        print("Button pressed!")
        self.callback()

    def is_pressed(self, *args):
        return self.button.value() == 0

    def is_released(self, *args):
        return self.button.value() == 1

    def __reset_cooldown(self, *args):
        self.cooling_down = False

    def __debounce(self):
        print("Debouncing!")
        self.cooling_down = True
        self.timer.init(mode=Timer.ONE_SHOT, period=350, callback=self.__reset_cooldown)


class TM1637NumberDisplay(abstract.SevenSegmentDisplay):

    def __repr__(self):
        return f"SevenSegmentDisplay({self.display})"

    def __init__(self, clk_pin: int, dio_pin: int):
        self.display = tm1637.TM1637(clk=Pin(clk_pin), dio=Pin(dio_pin))

    @staticmethod
    def __zfl(s, width):
        return '{:0>{w}}'.format(s, w=width)

    def update(self, digits: str):
        self.display.show(self.__zfl(digits, 4))

    def update_time(self, hours: int, minutes: int):
        self.display.numbers(self.__zfl(str(hours), 2), self.__zfl(str(minutes), 2), colon=True)

    def clear(self, *args):
        self.display.show("0000")
