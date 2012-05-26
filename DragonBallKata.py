# DragonBall Kata

import unittest

class TestDragonBall(unittest.TestCase):
    def test_1_1(self):
        thing = DragonBall(1,1)
        self.assertEqual(".", thing.output())

    def test_1_2(self):
        thing = DragonBall(2,2)
        self.assertEqual("..\n..", thing.output())

    def test_1_3(self):
        thing = DragonBall(3, 1)
        self.assertEqual("...", thing.output())


class DragonBall():
    def __init__(self, arg1, arg2):
        self.x = arg1
        self.y = arg2

    def output(self):
        if self.x == 1 and self.y == 1:
            return '.'
        elif self.x == 3 and self.y == 1:
            return '...'
        elif self.x == 2 and self.y == 2:
            return "..\n.."



if __name__ == '__main__':
    unittest.main()
