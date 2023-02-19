class Station:
    def __init__(self):
        self.size = 100
        self._weight = 2
        self.quiet = 10
        self._model = 5.0


class Joystick:
    def __init__(self):
        super().__init__()
        self.stick = 2
        self._battery = 100
        self.formfactor = 'ATX'
        self._color = 255


class Playstation(Joystick, Station):
    def print_info(self):
        print(self.stick)
        print(self._color)
        print(self._battery)
        print(self.formfactor)
        print(self.quiet)
        print(self._model)
        print(self.size)
        print(self._weight)


PL = Playstation()
PL.print_info()
