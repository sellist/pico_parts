from machine import Timer, Pin, disable_irq, enable_irq
import abstract


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

