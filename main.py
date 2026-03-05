# 1-masala
class OnlineShop:
    shop_name = "Tech Market"

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    @classmethod
    def change_shop_name(cls, new_name):
        if new_name != "":
            cls.shop_name = new_name

    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True

shop = OnlineShop("Tech Market", 100, 100)

print(shop.total_price())

OnlineShop.change_shop_name("Supermarket")
print(OnlineShop.shop_name)
# 2-masala
class Student:
    passing_score = 60

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        if self.score >= self.passing_score:
            return True

    @classmethod
    def change_passing_score(cls, new_score):
        cls.passing_score = new_score

    @staticmethod
    def is_valid_score(score):
        if 0 < score > 100:
            return True
# 3-masala
class BankCard:
    bank_name = "AgroBank"

    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Balans yetarli emas"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_card_number(number):
        return len(str(number)) == 16
# 4-masala
class Employee:
    company_name = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
# 5-masala
class Car:
    max_speed_limit = 180

    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def is_overspeed(self):
        return self.speed > self.max_speed_limit

    @classmethod
    def change_speed_limit(cls, new_limit):
        cls.max_speed_limit = new_limit

    @staticmethod
    def is_valid_speed(speed):
        if speed >= 0:
            return True
