class User:
    """存储用户信息"""

    def __init__(self, first_name, last_name, age):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """用户简介"""
        print(f"Your name is {self.first_name.title()} {self.last_name.title()}")
        print(f"You are {self.age} years old.")

    def greet_user(self):
        """个性化问候"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")

