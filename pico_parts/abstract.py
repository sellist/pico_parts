class Light:

    def on(self, *args):
        pass

    def off(self, *args):
        pass

    def toggle(self, *args):
        pass


class Button:

    def is_pressed(self, *args):
        pass

    def on_press(self, *args):
        pass

    def is_released(self, *args):
        pass

    def __debounce(self):
        pass

    def get_callback(self):
        return self.callback

    def set_callback(self, callback):
        self.callback = callback

    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        self.pin = pin


class SevenSegmentDisplay:

    def update(self, *args):
        pass

    def clear(self, *args):
        pass
