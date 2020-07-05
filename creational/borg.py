

class Device:
    __state = {}

    def __init__(self):
        self.__dict__ = self.__state
        self.state = 'on'

    def get_state(self) -> str:
        return self.state
    
    def change_off(self) -> None:
        self.state = 'off'

    def __str__(self):
        return f'State: {self.get_state()}'

if __name__ == '__main__':
    d1 = Device()
    d2 = Device()
    print(d1) # State: on
    print(d2) # State: on

    d1.change_off()
    print(d1) # State: off
    print(d2) # State: off

