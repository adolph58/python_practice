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

class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name, age):
        """初始化父类及自有属性"""
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示管理员权限"""
        print("管理员权限：")
        for privilege in self.privileges:
            print(f"{privilege}")


zhangsan = User('san', 'zhang', 24)
zhangsan.describe_user()
zhangsan.greet_user()

lisi = User('si', 'li', 39)
lisi.describe_user()
lisi.greet_user()

hanmeimei = User('meimei', 'han', 18)
hanmeimei.describe_user()
hanmeimei.greet_user()

admin = Admin('arte', 'cheng', 40)
admin.show_privileges()
