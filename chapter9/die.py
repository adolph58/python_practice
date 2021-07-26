from random import randint

class Die:
    """骰子类-模拟一个简单的骰子"""

    def __init__(self, sides=6):
        """初始化属性"""
        self.sides = sides

    def roll_die(self):
        """掷骰子"""
        result = randint(1, self.sides)
        print(f"你掷出的结果是：{result}")
