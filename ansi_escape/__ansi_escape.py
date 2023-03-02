import os


class ANSIEscape:
    def __init__(self):
        os.system('')
        self.__ESC = '\033['

    def write(self, string=''):
        print(string, end='')

    def writeln(self, string=''):
        print(string)

    def exec(self, code):
        self.write(self.__ESC + code)
