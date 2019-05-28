from itertools import islice

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.row_width = self.row_cells(matrix_string)

    def row_cells(self, matrix_string):
        eol = 0
        if matrix_string.find("\n") == -1:
            eol = len(matrix_string)
        else:
            eol = matrix_string.find("\n")

        width = list(matrix_string[0:eol].split())
        return len(width)

    def row(self, index):
        return list(map(int, islice(self.matrix_string.split(),
                    self.row_width * (index-1), self.row_width * (index), 1)))

    def column(self, index):
        return list(map(int, islice(self.matrix_string.split(),
                    index - 1, None, self.row_width)))

