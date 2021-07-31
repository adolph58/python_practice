class Employee:
    """雇员类"""

    def __init__(self, first_name, last_name, annual_salary):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, add_salary=5000):
        """增加年薪"""
        self.annual_salary += add_salary
