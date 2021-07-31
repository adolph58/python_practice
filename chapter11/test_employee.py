import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试。"""

    def setUp(self):
        """创建一个雇员，供使用的测试方法使用"""
        self.my_employee = Employee('Jack', 'Lee', 10000)
        
    def test_give_default_raise(self):
        """测试默认增加年薪方法"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 15000)

    def test_give_custom_raise(self):
        """测试自定义增加年薪方法"""
        self.my_employee.give_raise(6000)
        self.assertEqual(self.my_employee.annual_salary, 16000)

if __name__ == '__main__':
    unittest.main()
