from .__ansi_escape import ANSIEscape


class Text(ANSIEscape):
    class Foreground:
        BLACK = '30'
        RED = '31'
        GREEN = '32'
        YELLOW = '33'
        BLUE = '34'
        MAGENTA = '35'
        CYAN = '36'
        WHITE = '37'
        DEFAULT = '39'

        class Bright:
            BLACK = '90'
            RED = '91'
            GREEN = '92'
            YELLOW = '93'
            BLUE = '94'
            MAGENTA = '95'
            CYAN = '96'
            WHITE = '97'

    class Background:
        BLACK = '40'
        RED = '41'
        GREEN = '42'
        YELLOW = '43'
        BLUE = '44'
        MAGENTA = '45'
        CYAN = '46'
        WHITE = '47'
        DEFAULT = '49'

        class Bright:
            BLACK = '100'
            RED = '101'
            GREEN = '102'
            YELLOW = '103'
            BLUE = '104'
            MAGENTA = '105'
            CYAN = '106'
            WHITE = '107'

    def set_color(self, *, foreground: str = None, background: str = None):
        colors = [color for color in [foreground, background] if color is not None]
        self.exec(';'.join(colors) + 'm')

    def __get_rgb(self, r: int, g: int, b: int, foreground: bool):
        code = 38 if foreground else 48
        return f'{code};2;{r};{g};{b}'

    def get_rgb_foreground(self, r: int, g: int, b: int):
        return self.__get_rgb(r, g, b, True)

    def get_rgb_background(self, r: int, g: int, b: int):
        return self.__get_rgb(r, g, b, False)

    def __get_256(self, id: int, foreground: bool):
        code = 38 if foreground else 48
        return f'{code};5;{id}'

    def get_256_foreground(self, id: int):
        return self.__get_256(id, True)

    def get_256_background(self, id: int):
        return self.__get_256(id, False)

    def reset(self):
        self.exec('0m')

    def output_colored(self, string, function, *, foreground: str = None, background: str = None):
        self.set_color(foreground=foreground, background=background)
        function(string)
        self.reset()

    def set_underline(self):
        self.exec('4m')

    def reset_underline(self):
        self.exec('24m')

    def output_underlined(self, string, function):
        self.set_underline()
        function(string)
        self.reset_underline()

    def set_invert(self):
        self.exec('7m')

    def reset_invert(self):
        self.exec('27m')

    def output_inverted(self, string, function):
        self.set_invert()
        function(string)
        self.reset_invert()
