from re import A
from typing import List
#Hi

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

myBoard = [[0]*22]*8
myBoard[0] = list(board[0])
myBoard[1] = list(board[1])
myBoard[2] = list(board[2])
myBoard[3] = list(board[3])
myBoard[4] = list(board[4])
myBoard[5] = list(board[5])
myBoard[6] = list(board[6])
myBoard[7] = list(board[7])


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.

    if x >= 7 or x <= 0 or y >= 21 or y <= 0:
        return

    if myBoard[x][y] == '~':
        return

    if myBoard[x][y] == '#':
        return

    if myBoard[x][y] == old:
        myBoard[x][y] = new

    flood_fill(input_board, old, new, x+1, y)
    flood_fill(input_board, old, new, x-1, y)
    flood_fill(input_board, old, new, x, y+1)
    flood_fill(input_board, old, new, x, y-1)

    return myBoard


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
