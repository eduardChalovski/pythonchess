# im Terminal "pip install pytest-cov"
# (1) source: https://youtu.be/7BJ_BKeeJyM
# (2) src for testing print function: https://youtu.be/dN-pVt7i4Us

import pytest
import main

#helpful features like parameterizing: allows to run multiple variations of the same test
#@pytest.mark.parametrize('num1, num2, result', [
#                                                   (7, 3, 10),
#                                                   ('Hello', 'World', 'Hello World')
#                                                   (2.5, 3.5, 6.0)
#                                                  ])
#def test_add(num1, num2, result):
#   assert main.add(num1,num2) == result
#def setUp(self):
#
#def tearDown(self):

#fixture







# defining some parameters just to make the tests run 
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

knight_movement = [33, 31, 18, 14, -33, -31, -18, -14]
bishop_movement = [15, 17, -15, -17]
rook_movement = [16, -16, 1, -1]
king_movement = [16, -16, 1, -1, 15, 17, -15, -17]

white, black = range(2)

#side=white
can_castle=0

#def setup_module(module):
#    global side
#    global can_castle 
#    can_castle = main.can_castle
#    side = main.side

@pytest.mark.parametrize('fen,board_result,side_result,can_castle_result', [('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
                                                                            [r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
                                                                             p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                                             R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o], white,15),
                                                                             ('rnbqkbnr/8/pppppppp/8/RRRRnnnn/8/PPPPPPPP/RNBQKBNR b Kkq - 0 1',
                                                                            [r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             R, R, R, R, n, n, n, n, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                                             R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o], black,13),
                                                                             ('rnbqkbnr/8/pppppppp/8/RRRRnnnn/8/PPPPPPPP/RNBQKBNR b kq - 0 1',
                                                                            [r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             R, R, R, R, n, n, n, n, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                                             R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o], black,12),
                                                                             ('rnbqkbnr/8/pppppppp/8/RRRRnnnn/8/PPPPPPPP/RNBQKBNR b q - 0 1',
                                                                            [r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             R, R, R, R, n, n, n, n, o, o, o, o, o, o, o, o,
                                                                             e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                                             P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                                             R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o], black,8)])
def test_load_fen(fen,board_result,side_result,can_castle_result):
    main.load_fen(fen)
    assert main.board == board_result
    assert main.side == side_result
    assert main.can_castle == can_castle_result



@pytest.mark.parametrize('char_sides, side, can_castle, result', [
                                                  ('wb', 0, 0, "Side to move: w\nCastling: 0000\n"),
                                                  ('wb', 1, 15, "Side to move: b\nCastling: 1111\n")
                                                 ])
def test_print_stats(capsys, char_sides, side, can_castle, result):
    main.print_stats(char_sides,side,can_castle)
    stdout, stderr = capsys.readouterr()
    assert stdout == result



@pytest.mark.parametrize('board,side,result',[([r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
                                                p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o],white,
"1   . . . . . . . . \n2   . . . . . . . . \n3   . . . . . . . . \n4   . . . . . . . . \n5   . . . . . . . . \n6   x x x x x x x x \n7   x x x x x x x x \n8   . x x x x x x . \n\n    A B C D E F G H\n"),
                                                ([r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o,
                                                p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o],black,
"1   . x x x x x x . \n2   x x x x x x x x \n3   x x x x x x x x \n4   . . . . . . . . \n5   . . . . . . . . \n6   . . . . . . . . \n7   . . . . . . . . \n8   . . . . . . . . \n\n    A B C D E F G H\n")])
def test_print_attack(capsys, board, side, result):
    main.print_attack(board,side)
    stdout, stderr = capsys.readouterr()
    assert stdout == result

#testing positions to check whether is_position_attacked or not will be checked in the upper left corner of the board
#I try to go through every if-branch from top to the bottom of the code
#position = 0
#side, here is meant attacking side
@pytest.mark.parametrize('board,position,side,result', [
                                                          ([e, k, e, e, e, e, e, e, o, o, o, o, o, o, o, o, # in this test check always first two lines of the board
                                                            P, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, # in this test check always first two lines of the board
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],1,white,True), #1
                                                          ([k, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                            e, P, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #2
                                                          ([e, p, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                            K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],16,black,True), #3
                                                          ([p, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                            e, K, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                            e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],17,black,True), #4
                                                            ([k, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, N, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #5
                                                            ([K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, n, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #6
                                                            ([n, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, K, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #7
                                                            ([N, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, k, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #8
                                                            ([k, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, B, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #9
                                                            ([k, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, Q, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #10
                                                            ([K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, Q, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #11
                                                            ([K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, b, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #12
                                                            ([K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, q, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #13
                                                            ([K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, b, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #14
                                                            ([k, R, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #15
                                                            ([k, Q, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #16
                                                            ([k, e, R, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,True), #17
                                                            ([e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, k, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, R, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],33,white,True), #18 to show that function works not only in upper left corner of the board but in other area as well
                                                            ([K, e, r, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #19
                                                            ([K, e, e, e, q, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True), #20
                                                            ([k, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,white,None), #21
                                                            ([K, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,None), #22
                                                            ([e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, N, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],35,white,None), #23
                                                            ([k, r, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                              e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o],0,black,True) #24 

])  
def test_is_position_attacked(board,position,side,result):
    assert main.is_position_attacked(board,position,side) ==result


@pytest.mark.parametrize('board, result', [         #es werden zwei parameter gegeben: das erwartete Resultat und board, das geprinted wird 
                                                 ([r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o, #tupel 1
                                                   p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                   R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o], #unten ist das auf der Konsole erwartete String
"8   r n b q k b n r \n7   p p p p p p p p \n6   . . . . . . . . \n5   . . . . . . . . \n4   . . . . . . . . \n3   . . . . . . . . \n2   P P P P P P P P \n1   R N B Q K B N R \n\n    A B C D E F G H\n"),
                                                   ([r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o, #tupel 2
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o, #das zu printende Board 
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o],
"8   r n b q k b n r \n7   P P P P P P P P \n6   P P P P P P P P \n5   P P P P P P P P \n4   P P P P P P P P \n3   P P P P P P P P \n2   P P P P P P P P \n1   R N B Q K B N R \n\n    A B C D E F G H\n")
                                                ])
def test_print_board(capsys, board, result):        #dieser Test wird zweimal ausgeführt mit den beiden Werten aus den Tupeln
    main.print_board(board)                         #hier printen wir das Board
    stdout, stderr = capsys.readouterr()            #auf der Konsole ausgegeben String wird aufgenommen
    assert stdout == result                 

def test_clear_board():
    main.clear_board(board)
    assert board == [e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o, 
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                     e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o]
 

