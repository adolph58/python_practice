class User:
    """存储用户信息"""

    def __init__(self, first_name, last_name, age):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """用户简介"""
        print(f"Your name is {self.first_name.title()} {self.last_name.title()}")
        print(f"You are {self.age} years old.")

    def greet_user(self):
        """个性化问候"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        """增加登录次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登录次数"""
        self.login_attempts = 0

zhangsan = User('san', 'zhang', 24)
zhangsan.describe_user()
zhangsan.greet_user()

zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()

print(f"登录{zhangsan.login_attempts}次")

zhangsan.reset_login_attempts()

print(f"登录{zhangsan.login_attempts}次")
