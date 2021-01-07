import random
import time
import os

class TicTacToe():
    def __init__(self):
        # self.board = [str(i) for i in range(10)]
        self.board = [' '] * 10
        self.turn = 0  # random.randint(0,1)
        self.players = ['Player 1', 'Player 2']
        self.symbols = ['X', 'O']
        self.winner = ''
        self.verbose = True

    def ask_name(self):
        name = ''
        while not name.isalpha():
            name = input('\nBitte nenne mir deinen Namen: ')
        self.players[0] = name.title()

    def ask_symbol(self):
        symbol = ''
        while symbol not in ('X', 'x', 'O', 'o'):
            symbol = input('\nMoechtest du mit X oder O spielen? ')
        if symbol.upper() == 'X':
            self.symbols = ['X', 'O']
        else:
            self.symbols = ['O', 'X']

    def print_board(self):
        board = self.board[:]
        slices = []
        for row in range(3):
            temp = []
            for square in range(3):
                temp.append(board.pop())
            temp.reverse()
            slices.append(temp)
        for index, row in enumerate(slices):
            print(' ' + ' | '.join(row))
            if index in (0, 1):
                print('---+---+---')
        print()

    def square_is_free(self, index):
        return self.board[index] == ' '

    def board_is_full(self):
        result = True
        for square in self.board[1:]:
            if square == ' ':
                result = False
        return result

    def fill_square(self, index, symbol):
        self.board[index] = symbol

    def make_random_move(self, symbol):

        pool = list(range(1, 10))
        random.shuffle(pool)
        while pool:
            index = pool.pop()
            if self.square_is_free(index):
                self.fill_square(index, symbol)
                # self.board[index] = symbol
                self.turn += 1
                break

    def make_smarter_move_sides(self, symbol):
        sides = [2, 4, 6, 8, ]
        while sides:
            side = sides.pop()
            if self.square_is_free(side):
                self.fill_square(side, symbol)
                break
        else:
            self.make_random_move(symbol)

    def make_smarter_move_corners(self, symbol):
        corners = [1, 3, 7, 9, ]
        while corners:
            corner = corners.pop()
            if self.square_is_free(corner):
                self.fill_square(corner, symbol)
                break
        else:
            self.make_random_move(symbol)

    def make_smarter_move_csc(self, symbol):
        corners = [1, 3, 7, 9, ]
        center = [5]
        sides = [2, 4, 6, 8, ]

        moves = corners + center + sides

        while moves:
            move = moves.pop(0)
            if self.square_is_free(move):
                self.fill_square(move, symbol)
                break

    def get_number_of_symbols(self, symbol):
        pass

    def check_winner(self):
        index_tuples = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7),
        ]
        slices = []
        for index_tuple in index_tuples:
            temp_list = []
            for index in index_tuple:
                temp_list.append(self.board[index])
            slices.append(temp_list)

        winner = ''
        for symbol in self.symbols:
            result = ''
            for slice_ in slices:
                number = slice_.count(symbol)
                if number == 3:
                    index = self.symbols.index(symbol)
                    winner = self.players[index]
                    self.winner = winner

    def get_player_move(self):
        pass

    def clear_terminal(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def main(self):
        # self = TicTacToe()
        # t.board = [' ', 'O', 'O', 'X', 'X', 'O', 'X', ' ', ' ', 'O', ]
        # t.board = [' ', 'O', 'O', 'X', 'X', 'O', 'X', '0', '0', 'O', ]
        while True:
            if self.verbose:
                self.clear_terminal()
                print(f'Runde: {self.turn}')
            player = self.turn % 2
            symbol = self.symbols[player]
            self.check_winner()
            if self.board_is_full() or self.winner:
                break
            if player == 0:
                self.make_smarter_move_sides(symbol)
            else:
                self.make_smarter_move_sides(symbol)
            if self.verbose:
                self.print_board()
            # time.sleep(1)

        # spiel beenden
        if self.verbose:
            self.print_board()
            print('\nGame Over.')
            if self.winner:
                print(f'\nGewinner: {self.winner}')
            else:
                print('\nUnentschieden')


if __name__ == '__main__':
    iterations = 100000

    wins_p1 = 0
    wins_p2 = 0
    draws = 0

    for iteration in range(iterations):
        t = TicTacToe()
        # t.clear_terminal()
        if iteration % 1000 == 0:
            print(iteration + 1)
        t.main()
        if t.winner == '':
            draws += 1
        elif t.winner == 'Player 1':
            wins_p1 += 1
        else:
            wins_p2 += 1

    sum_ = wins_p1 + wins_p2 + draws
    percentages = lambda x: round(x / sum_ * 100, 1)
    os.system('clear')
    print(f'\n The percentages after {iterations} iterations are:\n')
    print(percentages(wins_p1))
    print(percentages(wins_p2))
    print(percentages(draws))

    if t.verbose:
        time.sleep(1)
