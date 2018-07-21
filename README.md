# Unbeatable Tic-Tac-Toe bot

A Human VS bot Tic-Tac-Toe game written in python.
Note: In Impossible mode, this bot is unbeatable. The bot will either win or the game will end in a tie.

## Description
This game of tic-tac-toe has three modes. Easy, Medium, Impossible.
In easy mode, the computer simply chooses a random move to make.
In medium mode, the computer randomly chooses between the best move and a random move.
In impossible mode, the computer chooses the best move can make.


## How does it work?

It uses the **MiniMax algorithm** to choose the best move.

> Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn based games such as Tic-Tac-Toe, Backgamon, Mancala, Chess, etc.

> In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to get the lowest score possible while minimizer tries to do opposite.

> Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.

Source: [GeeksForGeeks](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)