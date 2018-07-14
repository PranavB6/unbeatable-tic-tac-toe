import random, time, copy
# import only system from os
from os import system
from computer import Computer

# clear the terminal
def clear(): _ = system('cls')

# The tic-tac-toe grid
class GameGrid():

    def __init__(self, mode_str):
        self.mode_str = mode_str

        self.game_over = False
        self.filled = False
        self.winner = None

        self.positions = []
        for i in range(9): self.positions.append(' ')

        self.winning_configs = [[1,2,3], [4,5,6], [7,8,9],
                                [1,4,7], [2,5,8], [3,6,9],
                                [1,5,9], [3,5,7]                   
                               ]
        # nothing

    # Draw the grid
    def draw(self):
        print('Mode:', self.mode_str)
        print('1    |2    |3    ')
        print('  {}  |  {}  |  {} '.format( self.positions[0], self.positions[1], self.positions[2]))
        print('_____|_____|_____')
        print('4    |5    |6    ')
        print('  {}  |  {}  |  {}   '.format(self.positions[3], self.positions[4], self.positions[5]))
        print('_____|_____|_____')
        print('7    |8    |9    ')
        print('  {}  |  {}  |  {}   '.format( self.positions[6], self.positions[7], self.positions[8]))
        print('     |     |      ')

    # Makes a move on the grid. Assumes the moves are valid
    def make_move(self, position, letter):
        position_idx = position - 1
        self.positions[position_idx] = letter
        return

    # Check for a tie or a win
    def check_board(self):

        # If there are no empty spots, its a tie
        if not self.empty_spots(): 
            self.winner = None
            self.game_over = True

        # If there is a winning configuration, we have a winner
        for config in self.winning_configs:
            x,y,z = config
            if self.positions[x-1] != ' ':
                if self.positions[x-1] == self.positions[y-1] == self.positions[z-1]:
                    self.winner = self.positions[x-1]
                    self.game_over = True

        # NOTE: By checking for ties first and then winning config, it ensure that there can be a winner even if all positions are filled

    # Checks for empty spots in the grid. It returns a list of all the empty spots (positions)
    def empty_spots(self):
        empty_spots = []
        for position_idx, val in enumerate(self.positions):
            if val == ' ': empty_spots.append(position_idx+1)
        
        # print('Empty Spots:', empty_spots)
        return empty_spots

    # returns a deep copy of the positions on the board
    def get_positions(self):
        return copy.deepcopy(self.positions)


class Player():
    def __init__(self, letter):
        if letter not in ['X', 'O']:  
            raise ValueError('Invalid Letter:', letter)

        self.letter = letter

    # Ask player for a move, keep asking until they enter a valid move
    def choose_move(self, positions):
        while True:
            position = input('Position: ')

            try: position = int(position)
            except: continue

            if self.valid(position, positions):
                break

        return position

    # Check validity of a move
    def valid(self, position, positions):
        position_idx = position - 1

        if not (0 <= position_idx <= 8): 
            print('Invalid Position:', position)
            return False

        if positions[position_idx] != ' ': 
            print('Position', position, 'already filled')
            return False

        return True

    

# Choose who is X and who is O
def choose_letters():
    
    # Make sure to get valid input
    while True:
        player_letter = input('Choose X or O: ').upper()
        if player_letter in ['X', 'O']: break
    
    if player_letter == 'X': AI_letter = 'O'
    else: AI_letter = 'X'

    return player_letter, AI_letter

def choose_mode():

    while True:
        mode = input('Choose Easy (1), Medium (2), Impossible (3): ')
        if mode in ['1', '2', '3']: break

    mode = int(mode)
    
    if mode == 1: mode_str = 'Easy'
    elif mode == 2: mode_str = 'Medium'
    elif mode ==3: mode_str = 'Impossible'

    return mode, mode_str

def main():
    
    mode, mode_str = choose_mode()
    player_letter, AI_letter = choose_letters()  

    grid = GameGrid(mode_str)
    AI = Computer(AI_letter, mode)
    player = Player(player_letter)

    # Randomly choose who goes first
    turn = ''
    next_turn = random.choice([player.letter, AI.letter])

    # While the game is not over, keep playing
    while not grid.game_over:
        clear()        
        turn = next_turn
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
    
    # If game is over, draw the final state of the board
    clear()  
    grid.draw()
    if grid.winner:
        if grid.winner == player.letter:
            # If you win
            print('Fucking Bastard') 
        else:
            # If you lose
            print('Fucking loser')
            
    else: print('Tie')

if __name__ == '__main__':
    main()
