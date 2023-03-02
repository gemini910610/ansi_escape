from .__ansi_escape import ANSIEscape


class Cursor(ANSIEscape):
    def show(self):
        self.exec('?25h')

    def hide(self):
        self.exec('?25l')

    def save_position(self):
        self.exec('s')

    def restore_position(self):
        self.exec('u')

    def to(self, x: int, y: int):
        self.exec(f'{y};{x}H')

    def up(self, n: int):
        self.exec(f'{n}A')

    def down(self, n: int):
        self.exec(f'{n}B')

    def right(self, n: int):
        self.exec(f'{n}C')

    def left(self, n: int):
        self.exec(f'{n}D')

    def down_start(self, n: int):
        self.exec(f'{n}E')

    def up_start(self, n: int):
        self.exec(f'{n}F')

    def to_column(self, n: int):
        self.exec(f'{n}G')

    def erase_to_screen_end(self):
        self.exec('0J')

    def erase_to_screen_start(self):
        self.exec('1J')

    def erase_screen(self):
        self.exec('2J')

    def erase_to_line_end(self):
        self.exec('0K')

    def erase_to_line_start(self):
        self.exec('1K')

    def erase_line(self):
        self.exec('2K')
