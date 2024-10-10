from tictactoe import winner, X, O, EMPTY


board = [
    [X, O, EMPTY],
    [X, EMPTY, O],
    [X, EMPTY, EMPTY]
]
print(winner(board))