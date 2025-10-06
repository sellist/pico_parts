import sys
import types

from pico_parts.mock import MockPin, MockTimer, MockButton


def mock_time():
    import time
    if not hasattr(time, "sleep_us"):
        def sleep_us(us):  # us: microseconds
            import time as _time
            _time.sleep(us / 1_000_000)

        time.sleep_us = sleep_us

    if not hasattr(time, "ticks_ms"):
        def ticks_ms():
            import time as _time
            return int(_time.time() * 1000)

        time.ticks_ms = ticks_ms

    if not hasattr(time, "sleep_us"):
        def sleep_us(us):  # us: microseconds
            import time as _time
            _time.sleep(us / 1_000_000)

        time.sleep_us = sleep_us

    if not hasattr(time, "sleep_ms"):
        def sleep_ms(ms):  # ms: milliseconds
            import time as _time
            _time.sleep(ms / 1000)

        time.sleep_ms = sleep_ms

    sys.modules['time'] = time

def mock_machine():
    machine = types.SimpleNamespace(
        Pin=MockPin,
        Timer=MockTimer,
        Button=MockButton,
        disable_irq=lambda: 0,
        enable_irq=lambda x: None
    )
    micropython = types.SimpleNamespace(const=lambda x: x)
    sys.modules['machine'] = machine
    sys.modules['micropython'] = micropython

def setup_mocks():
    mock_machine()
    mock_time()


setup_mocks()

# Now import modules that depend on machine/micropython
# from pico_parts import abstract, simple

if __name__ == '__main__':
    import pico_parts.simple as simple
    led = simple.LED(led_pin=25)
    button = simple.Button(button_pin=15, callback=lambda: print("Button callback executed!"))

    led.on()

    led.off()

    led.toggle()

    button.press()

