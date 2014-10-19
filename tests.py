"http://content.codersdojo.org/code-kata-catalogue/bowling-game/"

import unittest
from bowling import BowlingGame

# frame, roll, score, total_score
text_data = """
1   1   1   
1   2   4   5
2   1   4   
2   2   5   14
3   1   6   
3   2   4   29
4   1   5   
4   2   5   49
5   1   10  
5   2       60
6   1   0   
6   2   1   61
7   1   7   
7   2   3   77
8   1   6   
8   2   4   97
9   1   10  
9   2       117
10  1   2   
10  2   8   
10  3   6   133
"""

rolls =[
1,
4,
4,
5,
6,
4,
5,
5,
10,
0,
1,
7,
3,
6,
4,
10,
2,
8,
6,
]


class Tests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def do_rolls(self, n):
        for i in rolls[:n]:
            self.game.roll(i)

    def test_no_rolls(self):
        self.assertEqual(0, self.game.score())

    def test_one_roll(self):
        self.do_rolls(1)
        self.assertEqual(1, self.game.score())

    def test_two_rolls(self):
        self.do_rolls(2)
        self.assertEqual(5, self.game.score())

    def test_four_rolls(self):
        self.do_rolls(4)
        self.assertEqual(14, self.game.score())

    def test_rolls_including_spare(self):
        self.do_rolls(7)
        self.assertEqual(34, self.game.score())
    
    def test_full_game(self):
        self.do_rolls(len(rolls))
        self.assertEqual(133, self.game.score())

    def test_perfect_game(self):
        for i in range(22):
            self.game.roll(10)
        self.assertEqual(300, self.game.score())


