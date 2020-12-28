import random

class TicTacToe():
    def __init__(self):
        #self.board = [str(i) for i in range(10)]
        self.board = [' '] * 10
        self.turn = random.randint(0,1)
        self.players = ['Player', 'Computer']
        self.symbols = ['X', 'O']

    def ask_name(self):
        name = ''
        while not name.isalpha():
            name = input('\nBitte nenne mir deinen Namen: ')
        self.players[0] = name.title()

    def ask_symbol(self):
        symbol = ''
        while symbol not in ('X', 'x', 'O', 'o'):
            symbol = input('\nMöchtest du mit X oder O spielen? ')
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
            if index in (0,1):
                print('---+---+---')
        print()

    def square_is_free(self, index):
        if self.board[index] != ' ':
            return False
        return True

    def check_winner(self):
        index_tuples = [
            (1,2,3),
            (4,5,6),
            (7,8,9),
            (1,4,7),
            (2,5,8),
            (3,6,9),
            (1,5,9),
            (3,5,7),
        ]
        slices = []
        for index_tuple in index_tuples:
            temp_list = []
            for index in index_tuple:
                temp_list.append(self.board[index])
            slices.append(temp_list)

        for symbol in self.symbols:
            result = ''
            for slice_ in slices:
                number = slice_.count(symbol)
                if number == 3:
                    return symbol


    def get_move(self):
        pass

if __name__ == '__main__':
    t = TicTacToe()
    #print(t.board)
    #t.ask_name()
    #t.ask_symbol()
    #print(t.players)
    #print(t.symbols)
    t.board = [' ', 'O', 'O', 'X', 'X', 'O', 'X', ' ', ' ', 'O', ]
    t.print_board()
    print(t.check_winner())
