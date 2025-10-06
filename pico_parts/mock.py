class MockPin:
    OUT = 0
    IN = 1
    IRQ_FALLING = 2

    def __init__(self, pin_number, mode):
        self.pin_number = pin_number
        self.mode = mode
        self.state = 0
        self.irq_handler = None

    def value(self, val=None):
        if val is not None:
            self.state = val
        return self.state

    def on(self):
        print(f"Pin {self.pin_number} set to HIGH")
        self.state = 1

    def off(self):
        print(f"Pin {self.pin_number} set to LOW")
        self.state = 0

    def irq(self, trigger, handler):
        self.irq_handler = handler


class MockTimer:
    ONE_SHOT = 0

    def init(self, mode, period, callback):
        pass

class MockButton:
    def __init__(self, pin_number, callback=None):
        self.pin_number = pin_number
        self.callback = callback
        self.state = 0  # Not pressed

    def is_pressed(self):
        return self.state == 1

    def press(self):
        self.state = 0
        if self.callback:
            self.callback()

    def release(self):
        self.state = 0