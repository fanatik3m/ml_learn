class InvalidMove(Exception):
    def __init__(self):
        message: str = 'Invalid move on the current board'
        super().__init__(message)