Object oriented Concept:
    1.INHERITANCE(Sharing of Information)
    2.ENCAPSULATION(Grouping of Information)
    3.ABSTRACTION(Hiding of Information)
    4.POLYMORPHISM(Redifing of Information)
#example
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_address(self):
        print(self.address.city, self.address.pin, self.address.state)
class Address:
    def __init__(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state
add1 = Address('Lucknow', '226011', 'Uttar Pradesh')
cust = Customer('Prashant Pandey', 'Male', add1)
cust.print_address()
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a Phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
s = SmartPhone(65000, "Samsung", "A37")
s.buy()
#SUPER KEYWORD
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a Phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
    #syntax to call parent by method
        super().buy()
s = SmartPhone(65000, "Samsung", "A37")
s.buy()
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a Phone")
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print("Inside SmartPhone constructor")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside SmartPhone constructor")
    #syntax to call parent by method
s = SmartPhone(65000, "Samsung", "A37","Android",2)
print(s.os)
print(s.brand)
