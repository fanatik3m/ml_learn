"""
Tic Tac Toe Player
"""

import math
import copy
from typing import Optional, Union

from exceptions import InvalidMove

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: list[list[Optional[str]]]) -> str:
    """
    Returns player who has the next turn on a board.
    """
    o_moves_count: int = 0
    x_moves_count: int = 0
    for row in board:
        o_moves_count += row.count(O)
        x_moves_count += row.count(X)

    if x_moves_count > o_moves_count:
        return O
    return X


def actions(board: list[list[Optional[str]]]) -> set:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions: set[tuple[int, int]] = set()
    for index_i, i in enumerate(board):
        for index_j in range(len(i)):
            if board[index_i][index_j] == EMPTY:
                available_actions.add((index_i, index_j))
    return available_actions


def result(board: list[list[Optional[str]]], action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i >= len(board):
        raise InvalidMove
    if j >= len(board[i]):
        raise InvalidMove
    if board[i][j] != EMPTY:
        raise InvalidMove

    new_board: list[list[Optional[str]]] = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board: list[list[Optional[str]]]) -> Optional[str]:
    """
    Returns the winner of the game, if there is one.
    """
    first_element: Optional[str]
    for row in board:
        first_element = row[0]
        if first_element == row[1] == row[2] and first_element:
            return first_element
    for i in range(len(board)):
        first_element = board[0][i]
        if first_element == board[1][i] == board[2][i] and first_element:
            return first_element

    middle_element: Optional[str] = board[1][1]
    if middle_element:
        if middle_element and (
                middle_element == board[0][0] == board[2][2] or middle_element == board[0][2] == board[2][0]):
            return middle_element
    return None


def terminal(board: list[list[Optional[str]]]) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    if not sum(row.count(EMPTY) for row in board) or winner(board):
        return True
    return False


def utility(board: list[list[Optional[str]]]) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner: str = winner(board)
    if game_winner == X:
        return 1
    if game_winner == O:
        return -1
    return 0


def minimax(board: list[list[Optional[str]]]) -> Optional[tuple[int, int]]:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_to_move: str = player(board)

    move: tuple[int, int]
    moves: dict[int, list[tuple[int, int]]] = {}
    for action in actions(board):
        if player_to_move == X:
            value = max_value(result(board, action))
        else:
            value = min_value(result(board, action))

        if value not in moves:
            moves[value] = [action]
        else:
            moves[value].append(action)

    return moves.get(max(moves.keys()))[0] if player_to_move == X else moves.get(min(moves.keys()))[0]


def min_value(board: list[list[Optional[str]]]) -> int:
    value: Union[float, int] = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


def max_value(board: list[list[Optional[str]]]) -> int:
    value: Union[float, int] = -float('inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value