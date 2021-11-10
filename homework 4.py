class Car:
    count = 0

    def __init__(self, price, colour, model):
        self.price = price
        self.colour = colour
        self.model = model
        Car.count += 1

    @staticmethod
    def print_hello():
        print("hello world")

    @classmethod
    def print_car_counter(cls):
        print(f"Car:{cls.count}")


    def getprice(self):
        return self.price
    def getcolour(self):
        return self.colour
    def getmodel(self):
        return self.model

car1 = Car(10000, "black", "bmw")
car2 = Car(5000, "red", "audi")
car3 = Car(30000, "silver", "gelik")
car4 = Car(8000, "wight", "kia")

print("цена: ", car1.price,"цвет: ", car1.colour,"модель: ", car1.model)
print("цена: ", car2.price,"цвет: ", car2.colour,"модель: ", car2.model)
print("цена: ", car3.price,"цвет: ", car3.colour,"модель: ", car3.model)
print("цена: ", car4.price,"цвет: ", car4.colour,"модель: ", car4.model)

print(Car.print_hello())
print(Car.print_car_counter())

