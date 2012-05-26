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
        
class DragonBall():
    def __init__(self, arg1, arg2):
        self.columns = arg1
        self.lines = arg2

    def output(self):
        if self.lines == 1:
            return '.'*self.columns
        elif self.lines == 2:
            return '.'*self.columns+'\n'+'.'*self.columns

if __name__ == '__main__':
    unittest.main()
