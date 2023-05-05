"""
Trying out some chess engine stuff
"""


#defining the piece integer representation
e, P, N, B, R, Q, K, p, n, b, r, q, k, o = range(14)

board = [
    r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
    p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
    P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
    R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o
]

char_ascii = '.PNBRQKpnbrqk'

#from ascii to normal chars
char_pieces = {'P': P, 'N': N, 'B': B, 'R': R, 'Q': Q, 'K': K, 'p': p, 'n': n, 'b': b, 'r': r, 'q': q, 'k': k}

fen = 'r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1'


def clear_board():
    #loop over column
    for rank in range(8):
        #loop over row
        for file in range(16):
            position = file + rank * 16
            #check if the piece is on the field
            if not position & 0x88:
                #clears the board
                board[position] = e


def print_board():
    #loop over column
    for rank in range(8):
        #loop over row
        for file in range(16):
            if file == 0:
                print(rank + 1, end='   ')
            position = file + rank * 16
            #check if the piece is on the field
            if not position & 0x88:
                print(char_ascii[board[position]], end=' ')
        print(end='\n')
    print("\n    A B C D E F G H")


def load_fen(fen):
    fen_position = 0

    # reset board
    clear_board()

    # loop over column
    for rank in range(8):
        # loop over row
        file = 0
        while file <= 16:
            print(str(rank) + ' + ' + str(file))
            position = file + rank * 16
            # check if the piece is on the field
            if not position & 0x88:
                if (fen[fen_position] > 'a' and fen[fen_position] < 'z') or (fen[fen_position] > 'A' and fen[fen_position] < 'Z'):
                    # set current board position to fen piece
                    board[position] = char_pieces[fen[fen_position]]

                    # increase fen position
                    fen_position += 1

                elif fen[fen_position] > '0' and fen[fen_position] < '9':
                    file += int(fen[fen_position]) - 1

                    # increase fen position
                    fen_position += 1

                elif fen[fen_position] == '/':
                    # increase fen position
                    fen_position += 1

            file += 1





def main():
    load_fen(fen)
    print_board()

if __name__ == '__main__':
    main()