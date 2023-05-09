"""
Trying out some chess engine stuff
"""


#defining the piece integer representation
e, P, N, B, R, Q, K, p, n, b, r, q, k, o = range(14)

white, black = range(2)

Castling = {'KC': 1, 'QC': 2, 'kc': 4, 'qc': 8}

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

square_representation = [
    'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'i8', 'j8', 'k8', 'l8', 'm8', 'n8', 'o8', 'p8',
    'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'i7', 'j7', 'k7', 'l7', 'm7', 'n7', 'o7', 'p7',
    'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'i6', 'j6', 'k6', 'l6', 'm6', 'n6', 'o6', 'p6',
    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'i5', 'j5', 'k5', 'l5', 'm5', 'n5', 'o5', 'p5',
    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'i4', 'j4', 'k4', 'l4', 'm4', 'n4', 'o4', 'p4',
    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'i3', 'j3', 'k3', 'l3', 'm3', 'n3', 'o3', 'p3',
    'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'i2', 'j2', 'k2', 'l2', 'm2', 'n2', 'o2', 'p2',
    'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j1', 'k1', 'l1', 'm1', 'n1', 'o1', 'p1'
]


char_ascii = '.PNBRQKpnbrqk'
char_sides = 'wb'


#from ascii to normal chars
char_pieces = {'P': P, 'N': N, 'B': B, 'R': R, 'Q': Q, 'K': K, 'p': p, 'n': n, 'b': b, 'r': r, 'q': q, 'k': k}


start_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
fen = 'r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1'


#0 = white and 1 = black
side = white

#castling rights in bit representation, where 15 is 1111, meaning both sides can castle both on the queen and king side
can_castle = 0

#piece movement offsets
knight_movement = [33, 31, 18, 14, -33, -31, -18, -14]
bishop_movement = [15, 17, -15, -17]
rook_movement = [16, -16, 1, -1]
king_movement = [16, -16, 1, -1, 15, 17, -15, -17]



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
                print(8 - rank, end='   ')
            position = file + rank * 16
            #check if the piece is on the field
            if not position & 0x88:
                print(char_ascii[board[position]], end=' ')
        print(end='\n')
    print("\n    A B C D E F G H")


def is_position_attacked(position, side):


    #attacked by pawn
    if not side:
        if not ((position + 17) & 0x88) and board[position + 17] == P:
            return True
        elif not ((position + 15) & 0x88) and board[position + 15] == P:
            return True
    else:
        if not ((position - 17) & 0x88) and board[position - 17] == p:
            return True
        elif not ((position - 15) & 0x88) and board[position - 15] == p:
            return True
        
    #attacked by knight
    if not side:
        for move in knight_movement:
            if not ((position + move) & 0x88) and board[position + move] == N:
                return True
    else:
        for move in knight_movement:
            if not ((position + move) & 0x88) and board[position + move] == n:
                return True
            
    #attacked by king
    if not side:
        for move in king_movement:
            if not ((position + move) & 0x88) and board[position + move] == K:
                return True
    else:
        for move in king_movement:
            if not ((position + move) & 0x88) and board[position + move] == k:
                return True
            
    #attacked by Bishop and Queen
    for move in bishop_movement:
        #creates new temp position
        new_position = position + move

        #loop through all the available positions for one move
        while not ((new_position) & 0x88):

            #grabs the piece at current position
            target = board[new_position]

            #checks if the position is attacked by B
            if (target == B or target == Q) if not side else (target == b or target == q):
                return True
            
            #breaks if it hits a piece
            elif target != 0:
                break

            #increment to new next position
            new_position += move

    #attacked by Rook and Queen
    for move in rook_movement:
        new_position = position + move

        while not ((new_position) & 0x88):
            target = board[new_position]

            if (target == R or target == Q) if not side else (target == r or target == q):
                return True
            
            elif target != 0:
                break

            new_position += move


def print_attack():
    #loop over column
    for rank in range(8):
        #loop over row
        for file in range(16):
            if file == 0:
                print(rank + 1, end='   ')
            position = file + rank * 16
            #check if the piece is on the field
            if not position & 0x88:
                print('x' if is_position_attacked(position, side) else '.', end=' ')
        print(end='\n')
    print("\n    A B C D E F G H")


def print_stats():
    print("Side to move: " + char_sides[side])
    print("Castling: " + str(bin(can_castle)[2:]).rjust(4, '0'))


def load_fen(fen):
    global side
    global can_castle
    fen_position = 0

    # reset board
    clear_board()

    # loop over column
    for rank in range(8):
        # loop over row
        file = 0
        while file <= 16:
            #calculate current position
            position = file + rank * 16
            # check if the piece is on the field
            if not position & 0x88:
                if (fen[fen_position] > 'a' and fen[fen_position] < 'z') or (fen[fen_position] > 'A' and fen[fen_position] < 'Z'):
                    # set current board position to fen piece
                    board[position] = char_pieces[fen[fen_position]]

                    fen_position += 1

                elif fen[fen_position] > '0' and fen[fen_position] < '9':
                    file += int(fen[fen_position]) - 1

                    fen_position += 1

                elif fen[fen_position] == '/' or fen[fen_position] == ' ':
                    fen_position += 1
            file += 1
    
    #go to side position
    fen_position += 1
    
    #parse side to move
    side = white if fen[fen_position] == 'w' else black

    #go to castling position
    fen_position += 2

    while fen[fen_position] != ' ':
        if fen[fen_position] == 'K':
            can_castle |= Castling['KC']
        elif fen[fen_position] == 'Q':
            can_castle |= Castling['QC']
        elif fen[fen_position] == 'k':
            can_castle |= Castling['kc']
        elif fen[fen_position] == 'q':
            can_castle |= Castling['qc']
        elif fen[fen_position] == '-':
            break
        fen_position += 1


#move generation
def generate_move():
    #loop over all positions on the board
    for position in range(128):
        if not position & 0x88:
            #white moves
            if not side:
                #pawn moves
                if board[position] == P:
                    #move forward
                    if not (position - 16) & 0x88 and not board[position - 16]:
                        #promotion condition
                        if position > 15 and position < 24: 
                            print("P promotes from " + square_representation[position] + " to " + square_representation[position - 16])

                        #other pawn moves
                        else:
                            pass
                            #move one square ahead
                            #print("P moves from " + square_representation[position] + " to " + square_representation[position - 16])

                            #move to squares
                            if(position > 95 and position < 104) and not board[position - 32]:
                                pass
                                #print("P can double move from " + square_representation[position] + " to " + square_representation[position - 32])

                    #pawn capture moves
                    for movement in bishop_movement:
                        if not (position - movement) & 0x88 and board[position - movement] and movement > 0 and board[position - movement] > 6:
                            
                            #look for promotion capture
                            if position > 15 and position < 24: 
                                print("P can promote attack from " + square_representation[position] + " to " + square_representation[position - movement])
                            
                            #casual capture
                            else:
                                print("P can attack from " + square_representation[position] + " to " + square_representation[position - movement])



            #black moves
            else:
                #pawn moves
                if board[position] == p:
                    if not (position + 16) & 0x88 and not board[position + 16]:
                        if position > 95 and position < 104:
                            pass
                            #print("p promotes from " + square_representation[position] + " to " + square_representation[position + 16])

                        else:
                            pass
                            #print("p moves from " + square_representation[position] + " to " + square_representation[position + 16])

                            if(position > 15 and position < 24) and not board[position + 32]:
                                pass
                                #print("p can double move from " + square_representation[position] + " to " + square_representation[position + 32])

                    for movement in bishop_movement:
                        if not (position - movement) & 0x88 and board[position - movement] and movement < 0 and board[position - movement] < 7:
                            
                            if position > 95 and position < 104:
                                print("p can promote attack from " + square_representation[position] + " to " + square_representation[position - movement])
                            
                            else:
                                print("p can attack from " + square_representation[position] + " to " + square_representation[position - movement])


def main():
    load_fen('4k2r/pPppqpb1/bn2Pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPpP/R3K2R b KQkq - 0 1')
    print_stats()
    print_board()
    #print(square_representation.index('a7'))
    generate_move()

if __name__ == '__main__':
    main()