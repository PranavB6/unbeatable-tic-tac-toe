import random, time, copy
# import only system from os
from os import system
from computer import Computer

def clear(): _ = system('cls')

class GameGrid():

    def __init__(self):

        self.game_over = False
        self.filled = False
        self.winning_letter = ''

        self.positions = []
        for i in range(9): self.positions.append(' ')

        self.winning_configs = [[1,2,3], [4,5,6], [7,8,9],
                    [1,4,7], [2,5,8], [3,6,9],
                    [1,5,9], [3,5,7]                   
                    ]
        # nothing
        # print(self.positions)

    def draw(self):
        print('1    |2    |3    ')
        print('  {}  |  {}  |  {} '.format( self.positions[0], self.positions[1], self.positions[2]))
        print('_____|_____|_____')
        print('4    |5    |6    ')
        print('  {}  |  {}  |  {}   '.format(self.positions[3], self.positions[4], self.positions[5]))
        print('_____|_____|_____')
        print('7    |8    |9    ')
        print('  {}  |  {}  |  {}   '.format( self.positions[6], self.positions[7], self.positions[8]))
        print('     |     |      ')

    def make_move(self, position, letter):
        position_idx = position - 1
        self.positions[position_idx] = letter
        return

    def check_board(self):

        if not self.empty_spots(): 
            self.winning_letter = ''
            self.game_over = True

        for config in self.winning_configs:
            x,y,z = config
            if self.positions[x-1] != ' ':
                if self.positions[x-1] == self.positions[y-1] == self.positions[z-1]:
                    self.winning_letter = self.positions[x-1]
                    self.game_over = True

    def empty_spots(self):
        empty_spots = []
        for position_idx, val in enumerate(self.positions):
            if val == ' ': empty_spots.append(position_idx+1)
        
        # print('Empty Spots:', empty_spots)
        return empty_spots

    def get_positions(self):
        return copy.deepcopy(self.positions)


class Player():
    def __init__(self, letter):

        if letter not in ['X', 'O']:  
            raise ValueError('Invalid Letter:', letter)

        self.letter = letter

    def choose_move(self, positions):
        while True:
            position = int(input('Position: '))
            if self.valid(position, positions):
                break

        return position

    def valid(self, position, positions):
        position_idx = position - 1

        if not (0 <= position_idx <= 8): 
            print('Invalid Position:', position)
            return False

        if positions[position_idx] != ' ': 
            print('Position', position, 'already filled')
            return False

        return True

    

def choose_letters():
    
    while True:
        player_letter = input('Choose X or O: ').upper()
        if player_letter in ['X', 'O']: break
    
    if player_letter == 'X': AI_letter = 'O'
    else: AI_letter = 'X'

    return player_letter, AI_letter


def main():
    player_letter, AI_letter = choose_letters()

    grid = GameGrid()
    AI = Computer(AI_letter)
    player = Player(player_letter)

    turn = ''
    next_turn = random.choice([player.letter, AI.letter])


    while not grid.game_over:
        clear()        
        turn = next_turn

        # print('Turn: ', turn)
        grid.draw()
        if turn == player.letter:

            letter = player.letter
            position = player.choose_move(grid.get_positions())
            next_turn = AI.letter
        else:
            letter = AI.letter
            position = AI.choose_move(grid.get_positions())
            next_turn = player.letter
                
        grid.make_move(position, letter)
        grid.check_board()
    
    # clear()  
    grid.draw()
    if grid.winning_letter: print(grid.winning_letter, "Wins!")
    else: print('Tie')


    
    # grid.draw()

    # letter = 'X'
    # while True:
        
    #     position = int(input('Position: '))
    #     clear()
    #     grid.make_move(position, letter)
    #     grid.draw()
    #     grid.check_board()
        
    # pass


if __name__ == '__main__':
    main()
