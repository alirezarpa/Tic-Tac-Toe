import pytest
from board import Board, Block

class Board:
    def __init__(self, WIN, width, height, padding, extra_padding) -> None:
        # Get the reference for the window
        self.WIN = WIN
        self.width = width
        self.height = height
        self.padding = padding
        self.extra_padding = extra_padding
        self.board = [[Block(WIN, row, col, width, height, padding, self.extra_padding) for row in range(3)]for col in range(3)]

def checkWin(self, row, col):
        curr_row = []
        curr_col = []
        diag1 = [(0, 0), (2, 2), (1, 1)]
        diag2 = [(2, 0), (0, 2), (1, 1)]
        for i in range(3):
            curr_row.append(self.board[row][i].value)
            curr_col.append(self.board[i][col].value)
        pos = (row, col)
        diag_right = []
        diag_left = []
        if pos in diag2:
            diag_right.append(self.board[2][0].value)
            diag_right.append(self.board[1][1].value)
            diag_right.append(self.board[0][2].value)
        if pos in diag1:
            for i in range(3):
                diag_left.append(self.board[i][i].value)
        if diag_left:
            for i, value in enumerate(diag_left):
                if value != Block.Current[1]:
                    break
                if i == 2:
                    return True
        if diag_right:
            for i, value in enumerate(diag_right):
                if value != Block.Current[1]:
                    break
                if i == 2:
                    return True
        curr_col = set(curr_col)
        curr_row = set(curr_row)
        if len(curr_col) == 1 and Block.Current[1] in curr_col:
            return True
        if len(curr_row) == 1 and Block.Current[1] in curr_row:
            return True
        return False

if __name__ == "__main__":
    main()