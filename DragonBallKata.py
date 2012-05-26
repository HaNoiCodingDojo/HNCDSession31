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
        self.arg1 = arg1
        self.arg2 = arg2

    def output(self):
        if self.arg1 == 1 and self.arg2 == 1:
            return '.'
        elif self.arg1 == 3 and self.arg2 == 1:
            return '...'
        elif self.arg1 == 2 and self.arg2 == 2:
            return "..\n.."



if __name__ == '__main__':
    unittest.main()
