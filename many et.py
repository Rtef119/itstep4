class Pc:
    def __init__(self):
        super().__init__()
        self.memory = 128

class Display:
    def __init__(self):
        super().__init__()
        self.reso = "4k"

class SmartPhone(Display, Pc):
    def print_info(self):
        print(self.reso)
        print(self.memory)

iphone = SmartPhone()
iphone.print_info()