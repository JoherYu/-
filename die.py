from random import randint

class Die():
    
    
    def __init__(self, num_sides=6):
        """设置骰子面数"""
        self.num_sides = num_sides
        
    def roll(self):
        """返回骰子得数"""
        return randint(1, self.num_sides)