class Restaurant:
    """这是一家餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐厅简介"""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"It's a {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """餐馆营业状态"""
        print("The restaurant is opening")

    def describe_number_served(self):
        """打印有多少人在这家餐厅就餐过"""
        print(f"There are {self.number_served} people have eaten in this restaurant")

    def set_number_served(self, number):
        """设置餐厅就餐人数"""
        self.number_served = number

    def increment_number_served(self, number):
        """
        增加就餐人数
        不能为负数
        """
        if number > 0:
            self.number_served += number
        else:
            print("You can'n roll back the number served!")

