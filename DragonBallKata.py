# DragonBall Kata

import unittest

class TestDragonBall(unittest.TestCase):
    def test_1_1(self):
        thing = DragonBall(1,1)
        self.assertEqual(".", thing.output())


if __name__ == '__main__':
    unittest.main()
