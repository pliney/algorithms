from pprint import pprint as pp
from time import time
from random import randint as rng

class board:
    def __init__(self):
        self.board = []
        self.queen_list = []
        self.board_size = 14 #must be even number
        self.init_board()

    def init_board(self):
        self.board = []
        for i in range(0, self.board_size/2):
            row1 = ['-', '#']*(self.board_size/2)
            row2 = ['#', '-']*(self.board_size/2)
            self.board.append(row1)
            self.board.append(row2)
            self.queen_list = []

    def add_queen(self, row, col):
        '''Returns true if queen was added, returns false if queen could not be added
        because board is full or the desired spot is already taken'''

        if len(self.queen_list) >= self.board_size:
            return False
        if self.board[row][col] == 'Q':
            return False
        if self.check_legal_queen(row,col) == False:
            return False

        self.queen_list.append((row,col))
        self.board[row][col] = 'Q'
        return True

    def check_legal_queen(self, row, col):
        for queen in self.queen_list:
            if queen[0] == row:
                return False
            if queen[1] == col:
                return False
            if row - queen[0] == col - queen[1]:
                return False
            if row - queen[0] == -(col-queen[1]):
                return False

        return True

    def back_tracking_rec(self, row, col):
        if col < self.board_size:
            for i in range(col, self.board_size):
                if self.add_queen(row, i):
                    if row == self.board_size-1:
                        return True
                    if self.back_tracking_rec(row + 1, 0):
                        return True
                    else:
                        self.remove_last_queen()
        return False

    def remove_last_queen(self):
        if len(self.queen_list) >= 1:
            r,c = self.queen_list.pop()
            if (r+c)%2 == 0:
                self.board[r][c] = '-'
            else:
                self.board[r][c] = '#'

    def back_tracking_alg(self, starting_col):
        self.init_board()
        self.back_tracking_rec(0, starting_col)

    def back_tracking_rand_start(self, num_queens):
        self.init_board()
        for i in range(0, num_queens):
            while True:
                if self.add_queen(i, rng(0,7)):
                    break
        self.back_tracking_rec(num_queens, 0)

    def check_last_queen_added(self):
        pass

if __name__ == '__main__':
    chess_board = board()
    # pp(chess_board.board)
    # print(chess_board.add_queen(0,0))
    # print (chess_board.add_queen(3,3))
    # print (chess_board.add_queen(3,3))
    # chess_board.add_queen(0, 5)
    # chess_board.add_queen(5, 3)
    # pp(chess_board.board)
    # print(chess_board.check_legal_queen(0, 0))
    # print(chess_board.check_legal_queen(0, 7))
    # print(chess_board.check_legal_queen(3, 3))
    # print(chess_board.check_legal_queen(7, 3))
    bt1 = time()
    chess_board.back_tracking_alg(2)
    bt2 = time()
    # pp(chess_board.board)
    rt1 = time()
    chess_board.back_tracking_rand_start(3)
    rt2 = time()
    print("Backtracking algorithm took %f ms to find solution" % ((bt2 - bt1) * 1000))
    print("Random start algorithm took %f ms to find solution" % ((rt2 - rt1) * 1000))
    # pp(chess_board.board)