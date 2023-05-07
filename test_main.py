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


@pytest.fixture(scope='module')
def board():
    return main.board

@pytest.fixture(scope='module')
def char_ascii():
    return main.char_ascii

@pytest.fixture(scope='module')
def char_sides():
    return main.char_sides

@pytest.fixture(scope='module')
def side():
    return main.side

@pytest.fixture(scope='module')
def can_castle():
    return main.can_castle



# problem: there is only one global state and loadfen changes state before any of the tests  
def test_print_stats(capsys, char_sides, side, can_castle):

    main.print_stats(char_sides, side, can_castle)
    stdout, stderr = capsys.readouterr()                    # reading prints before
    assert stdout == "Side to move: w\nCastling: 0000\n"

# 
#main.load_fen("8/8/8/3q4/8/8/8/8 b KQkq g5 0 1")
#
#def test_print_stats1(capsys, char_sides, side, can_castle):
#
#    main.print_stats(char_sides, side, can_castle)
#    stdout, stderr = capsys.readouterr()                   
#    assert stdout == "Side to move: b\nCastling: 1111\n"




# def test_print_board(capsys, board, char_ascii):  # look at reference (2) 
#     main.print_board
#     stdout, stderr = capsys.readouterr()
#     assert 

