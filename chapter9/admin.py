from user import User

class Privileges:
    """权限"""

    def __init__(self):
        """初始化属性"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        """显示管理员权限"""
        print("管理员权限：")
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name, age):
        """初始化父类及自有属性"""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

