from aoc2021.four.bingo_board import BingoBoard
from aoc2021.four.bingo_game import BingoGame


EXAMPLE_INPUT = \
    """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7


"""


def test_one_cell_bingo_board_lost():
    board = BingoBoard("1")

    board.mark(2)
    assert not board.has_won()


def test_one_cell_bingo_board_won():
    board = BingoBoard("1")

    board.mark(1)
    assert board.has_won()


def test_two_by_two_board():
    board = BingoBoard("1 2\n3 4\n")

    assert len(board.cols[0]) == 2
    assert len(board.cols) == 2
    assert len(board.rows[0]) == 2
    assert len(board.rows) == 2
    assert len(board.cells) == 4


def test_split_example_input():
    bingo = BingoGame(EXAMPLE_INPUT)

    assert len(bingo.boards) == 3
    assert len(bingo.calls) == 27
    assert len(bingo.boards[2].cells) == 25
    assert len(bingo.boards[2].rows) == 5
    assert len(bingo.boards[2].rows[0]) == 5
    assert len(bingo.boards[2].cols) == 5
    assert len(bingo.boards[2].cols[0]) == 5


def test_full_example_part_one():
    bingo = BingoGame(EXAMPLE_INPUT)
    bingo.play_until_win()

    assert bingo.winners[0].sum_unmarked_cells() == 188
    assert bingo.last_call == 24


def test_full_example_part_two():
    bingo = BingoGame(EXAMPLE_INPUT)
    bingo.play_until_last_win()

    assert bingo.last_call == 13
    assert bingo.winners[-1].sum_unmarked_cells() == 148
