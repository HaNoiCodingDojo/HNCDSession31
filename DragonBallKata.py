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
    
    def test_1_4(self):
        thing = DragonBall(1, 2)
        self.assertEqual(".\n.", thing.output())

    def test_2_1(self):
        thing = DragonBall(1, 1)
        thing.setAt(1, 1)
        self.assertEqual("*", thing.output())

    def test_2_2(self):
        thing = DragonBall(3, 1)
        thing.setAt(2, 1)
        self.assertEqual(".*.", thing.output())

    def test_2_4(self):
        thing = DragonBall(1,2)
        thing.setAt(1,2)
        self.assertEqual(".\n*", thing.output())
        
    def test_position1d_1_1(self):
        thing = DragonBall(1,1)
        result = thing.position1d_from_2d(1,1)
        expected = 0
        self.assertEqual(expected, result)

    def test_position1d_2_2(self):
        thing = DragonBall(2,2)
        result = thing.position1d_from_2d(2,1)
        expected = 1
        self.assertEqual(expected, result)

    def test_position1d_1_2(self):
        thing = DragonBall(2,2)
        result = thing.position1d_from_2d(1,2)
        expected = 3
        self.assertEqual(expected, result)

class DragonBall():
    def __init__(self, arg1, arg2):
        self.columns = arg1
        self.lines = arg2
        self.starX = 0
        self.starY = 0
        line = '.' * self.columns + "\n"
        self.result = line * self.lines
        self.result = self.result[:-1]

    def position1d_from_2d(self, posX, posY):
        # ..'
        # *.'
        # 1, 2 -> 3
        # 0, 1 -> 3

        # posX - 1, posY - 1
        # self.lines
        # self.columns + 1
        posX_0 = posX - 1
        posY_0 = posY - 1
        return (self.columns + 1) * posY_0 + posX_0
        
    def output(self):
        if (self.starX != 0):
            self.addStar()
        return self.result

    def addStar(self):
        position = self.position1d_from_2d(self.starX, self.starY)
        self.result = list(self.result)
        self.result[position] = '*'
        self.result = ''.join(self.result)

    def setAt(self, arg1, arg2):
        self.starX = arg1
        self.starY = arg2


if __name__ == '__main__':
    unittest.main()
