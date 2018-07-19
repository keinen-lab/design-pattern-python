
class Switch(object):
    """The Invoker class"""
    def __init__(self, flip_up_cmd, flip_down_cmd):
        self.flip_up = flip_up_cmd
        self.flip_down = flip_down_cmd


class Light(object):
    """The Receiver class"""
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")


class LightSwitch(object):
    """The client class"""
    def __init__(self):
        lamp = Light()
        self._switch = Switch(lamp.turn_on, lamp.turn_off)

    def swich(self, cmd):
        cmd = cmd.strip().upper()
        if cmd == "ON":
            self._switch.flip_up()
        elif cmd == "OFF":
            self._switch.flip_down()
        else:
            print("Argument 'ON' of 'OFF' is required")


if __name__ == "__main__":
    light_switch = LightSwitch()
    print("Switch ON test")
    light_switch.swich("ON")
    print("Switch OFF test")
    light_switch.swich("OFF")
    print("Invalid Command test")
    light_switch.swich("****")