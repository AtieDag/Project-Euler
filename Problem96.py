import numpy as np
import pandas as pd


def get_row_col(i):
    row = int(i / 9)
    col = i % 9
    return row, col


class Sudoku():

    def __init__(self, matrix):
        self.matrix = matrix.copy()
        self.hard_ = self.matrix > 0

    def check(self, row, col, value):
        if value in self.on_h_line(row):
            return True
        if value in self.on_v_line(col):
            return True
        if value in self.in_box(row, col):
            return True
        return False

    # In the box
    def in_box(self, row, col):
        pos = np.array([int(row / 3), int(col / 3)]) * 3
        pos_2 = pos + 3
        box = self.matrix[pos[0]:pos_2[0], pos[1]:pos_2[1]]
        return box

    # On the line-hor
    def on_h_line(self, col):
        return self.matrix[col, :]

    # On the line-ver
    def on_v_line(self, row):
        return self.matrix[:, row]

    # Set value
    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def get_possibilities(self, row, col):
        if self.hard_[row][col]:
            return [self.matrix[row][col]]
        list_p = []
        for nr in range(0, 10):
            if not self.check(row, col, nr):
                list_p.append(nr)
        return list_p

    def reset_value(self, row, col):
        if not self.hard_[row][col]:
            self.set_value(row, col, 0)

    def stop_next_step(self, i):
        if i > 0:
            pre_row, pre_col = get_row_col(i - 1)
            if self.matrix[pre_row][pre_col] == 0:
                return True
        return False

    def is_complete(self):
        if np.any(self.matrix == 0):
            return False
        return True

    def get_solution(self):
        self.run(0)

        sum_ = ''
        for sum_i in self.matrix[0][0:3]:
            sum_ += (str(int(sum_i)))

        return int(sum_)

    def run(self, i):
        if self.stop_next_step(i):
            return False

        if i == (9 * 9):
            if self.is_complete():
                return True
            else:
                return False

        row, col = get_row_col(i)
        try_possibilities = self.get_possibilities(row, col)
        for value in try_possibilities:
            self.set_value(row, col, value)
            if self.run(i + 1):
                return True
            else:
                self.reset_value(row, col)

        if not try_possibilities:
            if self.run(i + 1):
                return True
        return False


if __name__ == "__main__":
    data = pd.read_table('p096_sudoku.txt')
    aaa = 0
    sum_list = []
    for i in range(50):
        row = 0
        matrix = np.zeros(shape=(9, 9))
        for i in data.iloc[aaa:aaa + 9].values:
            column = 0
            for j in i[0]:
                matrix[row, column] = j
                column += 1
            row += 1
        a = Sudoku(matrix)
        sum_ = a.get_solution()
        sum_list.append(sum_)
        aaa += 10
    print(sum(sum_list))
