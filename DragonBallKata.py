# DragonBall Kata

import unittest

class TestDragonBall(unittest.TestCase):
    def test_1_1(self):
        thing = DragonBall(1,1)
        self.assertEqual(".", thing.output())


class DragonBall():
    def __init__(self, arg1, arg2):
        pass

    def output(self):
        return('.')



if __name__ == '__main__':
    unittest.main()
