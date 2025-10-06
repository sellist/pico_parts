# micropython doesn't support ABC module, so have to do it the old-fashioned way

def abstract(doc=""):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            raise NotImplementedError(
                f"Subclasses of {self.__class__.__name__} must implement {func.__name__}()"
            )
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = doc
        return wrapper
    return decorator

class AbstractComponent:
    def __init__(self):
        if self.__class__ is AbstractComponent:
            raise TypeError(f"{self.__class__.__name__} is an abstract base class and cannot be instantiated directly.")
        if self.__class__.__init__ is AbstractComponent.__init__:
            raise NotImplementedError(
                f"Warning: {self.__class__.__name__} does not override __init__. "
                f"Defining an __init__ method in your subclass."
            )

class Board(AbstractComponent):
    pass

class Light(AbstractComponent):
    @abstract("Turn the light on.")
    def on(self, *args):
        pass

    @abstract("Turn the light off.")
    def off(self, *args):
        pass

    @abstract("Toggle the light state.")
    def toggle(self, *args):
        pass

class Button(AbstractComponent):
    @abstract("Return True if the button is currently pressed.")
    def is_pressed(self, *args):
        pass

    @abstract("Callback for when the button is pressed.")
    def on_press(self, *args):
        pass

    @abstract("Return True if the button is currently released.")
    def is_released(self, *args):
        pass

    @abstract("Debounce logic for the button.")
    def __debounce(self):
        pass

    @abstract("Simulate a button release (for testing purposes).")
    def press(self):
        pass

class SevenSegmentDisplay(AbstractComponent):
    @abstract("Update the display with new data.")
    def update(self, *args): pass

    @abstract("Clear the display.")
    def clear(self, *args): pass

class LCDDisplay(AbstractComponent):
    @abstract("Update the display with new data.")
    def update(self, *args): pass

    @abstract("Clear the display.")
    def clear(self): pass

    @abstract("Refresh the display.")
    def refresh(self): pass

class Potentiometer(AbstractComponent):
    @abstract("Read the current value from the potentiometer.")
    def read(self): pass

class MotorizedPotentiometer(Potentiometer):
    @abstract("Set the potentiometer to a specific position.")
    def set_position(self, position): pass

class Sensor(AbstractComponent):
    @abstract("Get information or reading from the sensor.")
    def get_info(self): pass

class Toggle(AbstractComponent):
    @abstract("Read the current state of the toggle switch.")
    def read(self): pass

if __name__ == "__main__":
    # print("abstract.py is an abstract base class module and cannot be run directly.")
    class TestButton(Button):
        pass

    tb = TestButton()
