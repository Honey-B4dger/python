class Connect4():
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.players = ['', '']
        self.game_over = False
        self.player_1_wins = False
        self.player_2_wins = False
        self.current_setup = []
        self.topped = [False for i in range(self.columns)]
        self.create_initial_state()
        self.slices = ['' for i in range(self.columns)]
        self.four_in_a_row = False
        self.topped_off = False

    def create_initial_state(self):
        setup = []

        for row in range(self.rows):
            setup.append(['.' for i in range(self.columns)])

        self.current_setup = setup

    def print_current_setup(self):
        for row in self.current_setup:
            print(''.join(row))

    def drop(self,column, symbol):
        row = self.rows - 1

        if self.topped[column]:
            print(f"Spalte {column + 1} is schon voll!")

        while row >= 0 and self.topped[column] != True:
            if self.current_setup[row][column] == '.':
                self.current_setup[row][column] = symbol
                if row == 0:
                    self.topped[column] = True
                break
            else:
                row -= 1

    def create_slices(self):
# horizontal
        for columns in range(self.columns):
            for rows in range(self.rows):
                self.slices[columns] += self.current_setup[rows][columns]

# vertikal
        for rows in self.current_setup:
            self.slices.append(''.join(rows))
# nach rechts unten
# 

    def check_slices(self):
        for slices in self.slices:
            if 'XXXX' in slices:
                self.player_1_wins = True
                self.game_over = True
                self.four_in_a_row = True
            elif 'OOOO' in slices:
                self.player_2_wins = True
                self.game_over = True
                self.four_in_a_row = True

    def check_tops(self):
        if False not in self.topped:
            self.topped_off = True
            self.game_over = True

    def get_names(self):
        pass

    def print_status(self):
        print(f"Game Over : {self.game_over}")
        print(f"Players : {self.players}")
        print(f"Player 1 wins : {self.player_1_wins}")
        print(f"Player 2 wins : {self.player_2_wins}")
        print(f"Topped : {self.topped}")

        for element in self.slices:
            print(element)

    def print_playfield(self):
        print('+=============================+')
        for row in range(self.rows):
            print('+| ' + ' | '.join(self.current_setup[row]) + ' |+')
            if row != -self.rows:
                print('+-----------------------------+')
            else:
                print('+=============================+')


