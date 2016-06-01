class SuDoku(object):
    def __init__(self):
        self.matrix = []
        self.grid = []

    def add_row(self, line):
        self.matrix.append(line)

    def get_grid_nr(self, row, column):
        grid = 0
        if row < 3:
            grid += 0
        elif row < 6:
            grid += 1
        else:
            grid += 2

        if column < 3:
            grid += 0
        elif row < 6:
            column += 1
        else:
            column += 2

        return grid

    def check_grid(self, grid_number):
        pass


class Number(object):
    def __init__(self, number):
        self.possible_numbers = []

        if number == 0:
            self.possible_numbers = list(range(1, 10))
        else:
            self.possible_numbers = [number]

    def remove_number(self, number):
        self.possible_numbers.remove(number)

    def exists(self, number):
        return number in self.possible_numbers


def string_line_to_list(string):
    a = []
    for number in string:
        if number != "\n":
            # _number = Number(int(float(number)))
            a.append(number)
    return a


def load_su_doku(file_name):
    b = []
    with open(file_name) as file:

        for index, line in enumerate(file):
            # skip name row
            if index % 10 == 0:
                m = SuDoku()
                b.append(m)
            else:
                m.add_row(string_line_to_list(line))

    return b


if __name__ == '__main__':
    all_su = load_su_doku('Problem96.txt')



