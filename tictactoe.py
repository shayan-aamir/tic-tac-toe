"""
Tic Tac Toe game implementation with AI using minimax algorithm.
"""

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

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count X's and O's to determine whose turn it is
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # If there are more X's than O's, it's O's turn
    # If equal, it's X's turn (X goes first)
    return O if x_count > o_count else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy of the board
    new_board = [row[:] for row in board]
    
    # Check if action is valid
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Make the move
    i, j = action
    new_board[i][j] = player(board)
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    
    # Check columns
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        if column.count(X) == 3:
            return X
        if column.count(O) == 3:
            return O
    
    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2-i] for i in range(3)]
    
    if diagonal1.count(X) == 3 or diagonal2.count(X) == 3:
        return X
    if diagonal1.count(O) == 3 or diagonal2.count(O) == 3:
        return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there's a winner, game is over
    if winner(board) is not None:
        return True
    
    # If board is full, game is over
    if all(cell != EMPTY for row in board for cell in row):
        return True
    
    # Otherwise, game is still in progress
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X is maximizing player
        value, action = max_value(board)
    else:
        # O is minimizing player
        value, action = min_value(board)
    
    return action

def max_value(board):
    """
    Helper function for minimax that returns the maximum value and action
    for the maximizing player (X).
    """
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    best_action = None
    
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    
    return v, best_action

def min_value(board):
    """
    Helper function for minimax that returns the minimum value and action
    for the minimizing player (O).
    """
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    best_action = None
    
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    
    return v, best_action 