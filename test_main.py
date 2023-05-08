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



