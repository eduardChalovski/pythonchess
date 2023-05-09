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





@pytest.mark.parametrize('char_sides, side, can_castle, result', [
                                                  ('wb', 0, 0, "Side to move: w\nCastling: 0000\n"),
                                                  ('wb', 1, 15, "Side to move: b\nCastling: 1111\n")
                                                 ])
def test_print_stats(capsys, char_sides, side, can_castle, result):
    main.print_stats(char_sides,side,can_castle)
    stdout, stderr = capsys.readouterr()
    assert stdout == result



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


@pytest.mark.parametrize('board, result', [         #es werden zwei parameter gegeben: das erwartete Resultat und board, das geprinted wird 
                                                 ([r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o, #tupel 1
                                                   p, p, p, p, p, p, p, p, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   e, e, e, e, e, e, e, e, o, o, o, o, o, o, o, o,
                                                   P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                   R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o], #unten ist das auf der Konsole erwartete String
                                                   "1   r n b q k b n r \n2   p p p p p p p p \n3   . . . . . . . . \n4   . . . . . . . . \n5   . . . . . . . . \n6   . . . . . . . . \n7   P P P P P P P P \n8   R N B Q K B N R \n\n    A B C D E F G H\n"),
                                                   ([r, n, b, q, k, b, n, r, o, o, o, o, o, o, o, o, #tupel 2
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o, #das zu printende Board 
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     P, P, P, P, P, P, P, P, o, o, o, o, o, o, o, o,
                                                     R, N, B, Q, K, B, N, R, o, o, o, o, o, o, o, o],
                                                     "1   r n b q k b n r \n2   P P P P P P P P \n3   P P P P P P P P \n4   P P P P P P P P \n5   P P P P P P P P \n6   P P P P P P P P \n7   P P P P P P P P \n8   R N B Q K B N R \n\n    A B C D E F G H\n")
                                                ])
def test_print_board(capsys, board, result):   #dieser Test wird zweimal ausgeführt mit den beiden Werten aus den Tupeln
    main.print_board(board)                 #hier printen wir das Board
    stdout, stderr = capsys.readouterr()    #auf der Konsole ausgegeben String wird aufgenommen
    assert stdout == result                 
