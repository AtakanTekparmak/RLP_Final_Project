import chess 
import numpy as np

EMPTY_BOARD_FEN = '8/8/8/8/8/8/8/8 w - - 0 1' # FEN for an empty board
PIECE_TO_INT = {
    # White pieces
    'P': 1,'N': 2,'B': 3,'R': 4,'Q': 5,'K': 6,
    # Black pieces
    'p': 7,'n': 8,'b': 9,'r': 10,'q': 11,'k': 12,
    # Empty squares
    '.': 0
}

def load_fen(fen_file):
    '''Loads a chess.Board object from a FEN file.'''
    with open(fen_file, 'r') as f:
        fen = f.read()
        return chess.Board(fen)
    
def invert_dict(d):
    return {v: k for k, v in d.items()}
    
def board_to_numpy(board):
    '''Converts a chess.Board object to a numpy array.'''
    board_array = np.zeros((8, 8), dtype=np.int8)
    for i, row in enumerate(board.fen().split()[0].split('/')):
        j = 0
        for piece in row:
            if piece.isdigit():
                j += int(piece)
            else:
                board_array[i, j] = PIECE_TO_INT[piece]
                j += 1

    return board_array.astype(np.float32)

def numpy_to_board(board_array):
    '''Converts a numpy array to a chess.Board object.'''
    fen = ''
    for i in range(8):
        empty_squares = 0
        for j in range(8):
            piece = board_array[i, j]
            if piece == 0:
                empty_squares += 1
            else:
                if empty_squares > 0:
                    fen += str(empty_squares)
                    empty_squares = 0
                fen += invert_dict(PIECE_TO_INT)[piece]
        if empty_squares > 0:
            fen += str(empty_squares)
        if i < 7:
            fen += '/'
    fen += ' w - - 0 1'
    return chess.Board(fen)
   


def test_board_to_numpy():
    board = load_fen('static/endgame1.fen')
    print(board)
    board_array = board_to_numpy(board)
    board_from_array = numpy_to_board(board_array)
    print(board_from_array)


def main():
    test_board_to_numpy()

if __name__ == '__main__':
    main()