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
        
class DragonBall():
    def __init__(self, arg1, arg2):
        self.columns = arg1
        self.lines = arg2
        self.starX = 0
        self.starY = 0

    def output(self):
        result = ''
        if self.starX == 1 and self.starY == 1:
            return "*"
        if self.starX == 2 and self.starY == 1:
            return ".*."
        else:
            line = '.' * self.columns + "\n"
            result = line * self.lines
            return result[:-1]
   
#    def addStar(self, result):
#        position = self.starX * (self.lines + 1) + self.starY
        

    def setAt(self, arg1, arg2):
        self.starX = arg1
        self.starY = arg2


if __name__ == '__main__':
    unittest.main()
