The code for this part was copied and modified from [Tawn Kramer's](https://github.com/tawnkramer/donkey) fork of donkeycar.

# Logitech Joystick Controller

The default web controller may be replaced with a one line change to use a physical joystick part for input. This uses
the OS device /dev/input/js0 by default. In theory, any joystick device that the OS mounts like this can be used. In
practice, the behavior will change depending on the model of joystick ( Sony, or knockoff ), or XBox controller
and the Bluetooth driver used to support it. The default code has been written and tested with
 a [Logitech F710 controller](https://www.amazon.com/Logitech-940-000117-Gamepad-F710/dp/B0041RR0TW/ref=sr_1_1?keywords=logitech+f710&qid=1548047395&sr=8-1).
 Other controllers may work, but will require alternative Bluetooth installs, and tweaks to the software for correct
 axis and buttons.

To make this work, you need only to plug in the USB receiver that came with your controller. The Rpi should already have drivers to read the inputs.

## Install

1. Plug the bluetooth reciever into an open usb port on the raspberry pi.

2. Install the parts python package.
    ```bash
    pip install git+https://github.com/kevkruemp/donkeypart_logitech_controller.git
    ```

3. Import the part at the top of your manage.py script. If you are using a PS4 controller, import `PS4JoystickController` instead. Same applies in the next step.
    ```python
    from donkeypart_logitech_controller import LogitechJoystickController
    ```   

4. Replace the controller part of your manage.py to use the JoysticController part.
    ```python
    ctr = LogitechJoystickController(
       throttle_scale=cfg.JOYSTICK_MAX_THROTTLE,
       steering_scale=cfg.JOYSTICK_STEERING_SCALE,
       auto_record_on_throttle=cfg.AUTO_RECORD_ON_THROTTLE
    )

     V.add(ctr,
          inputs=['cam/image_array'],
          outputs=['user/angle', 'user/throttle', 'user/mode', 'recording'],
          threaded=True)
    ```

5. Add the required config paramters to your config.py file. It should look something like this.
    ```python
    #JOYSTICK
    JOYSTICK_STEERING_SCALE = 1.0
    AUTO_RECORD_ON_THROTTLE = True
    ```

6. Now you're ready to run the `python manage.py drive --js` command to start your car.

### Joystick Controls

* Left analog stick - Left and right to adjust steering
* Right analog stick - Forward to increase forward throttle
* Pull back twice on right analog to reverse

> Whenever the throttle is not zero, driving data will be recorded - as long as you are in User mode!

* Start button switches modes - "User, Local Angle, Local(angle and throttle)"
* Y - Increase max throttle
* X - Decrease max throttle
* B - Erases last 100 tagged pictures
* Right bumper - Toggle recording (auto-record with non-zero throttle on by default)
* Left bumper - Toggle constant throttle. Sets to max throttle (modified by X and Y).
* Logitech button - Emergency Stop

### Driving tips
Hit the Start button to toggle between three modes - User, Local Angle, and Local Throttle & Angle.
You can select which pilot to use by using the start command: `python manage.py drive --js --model ./models/<pilot_name_here>`

* User - User controls both steering and throttle with joystick
* Local Angle - Ai controls steering, user controls throttle
* Local Throttle & Angle - Ai controls both steering and throttle

When the car is in Local Angle mode, the NN will steer. You must provide throttle. (generally using the left bumper constant throttle is advised)
