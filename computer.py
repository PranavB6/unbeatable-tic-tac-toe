
import random, copy

class Computer():
    def __init__(self, letter):
        if letter not in ['X', 'O']: raise ValueError('Invalid Letter:', letter)

        self.letter = letter
        if self.letter == 'X': self.opp_letter = 'O'
        else: self.opp_letter = 'X'

        self.winning_configs = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9],
            [1,5,9], [3,5,7]                   
            ]
        # nothing
        
    def choose_move(self, positions):

        if len(self.empty_spots(positions)) < 9:
            val, memo = self.minimax(positions)
            print("Best moves for AI:", memo)

            return memo.pop()

        return random.choice(self.empty_spots(positions))

    # SEE THE FUTURE
    def minimax(self, config, memo = None, maxingPlayer = True):

        if memo == None:
            first_lvl = True 
            memo = set()

        else:
            first_lvl = False

        # print(config)
        game_over, winner = self.check_board(config)

        if game_over:
            if winner == self.letter:
                weight = 10
                return weight, memo
            elif winner == self.opp_letter: 
                weight = -10
                return weight, memo
            else: 
                weight = 0
                return weight, memo

        empty_spots = self.empty_spots(config)
        # print('Empty Spots:', empty_spots)

        if maxingPlayer:
            best_val = float('-inf')
            best_spot = empty_spots[0]

            for spot in empty_spots:
                updated_config = self.update_config(config, spot, self.letter)
                val, memo = self.minimax(updated_config, memo, False)

                if (val > best_val):
                    best_val = val
                    best_spot = spot

            if first_lvl == True: memo.add(best_spot)

        if not maxingPlayer:
            best_val = float('inf')
            # best_spot = empty_spots[0]

            for spot in empty_spots:
                updated_config = self.update_config(config, spot, self.opp_letter)
                val, memo = self.minimax(updated_config, memo, True)

                if val < best_val:
                    best_val = val
            
        return best_val, memo



    def update_config(self, config, spot, letter):
        updated_config = copy.deepcopy(config)
        updated_config[spot-1] = letter
        return updated_config

    def empty_spots(self, positions):
        empty_spots = []
        for position_idx, val in enumerate(positions):
            if val == ' ': empty_spots.append(position_idx+1)
        return empty_spots 

    def check_board(self, positions):
        game_over = False
        winner = None

        if not self.empty_spots(positions): 
            winner = None
            game_over = True

        for config in self.winning_configs:
            x,y,z = config
            if positions[x-1] != ' ':
                if positions[x-1] == positions[y-1] == positions[z-1]:
                    winner = positions[x-1]
                    game_over = True        
        return game_over, winner