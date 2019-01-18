import pytest
from donkeycar.parts.controller import LogitechJoystick, LogitechJoystickController


def test_logitech_joystick():
    js = LogitechJoystick()
    assert js is not None
    js.init()

def test_logitech_joystick_controller():
    js = LogitechJoystickController()
    assert js is not None
    js.init_js()
    js.run_threaded(None)
    js.print_controls()
    def test_fn():
        pass
    js.set_button_down_trigger("x", test_fn)
    js.erase_last_N_records()
    js.on_throttle_changes()
    js.emergency_stop()
    #js.update()
    js.set_steering(0.0)
    js.set_throttle(0.0)
    js.toggle_manual_recording()
    js.increase_max_throttle()
    js.decrease_max_throttle()
    js.toggle_constant_throttle()
    js.toggle_mode()
    js.chaos_monkey_on_left()
    js.chaos_monkey_on_right()
    js.chaos_monkey_off()