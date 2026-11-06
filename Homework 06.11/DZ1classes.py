class Vehicle: #родительский
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Это {self.brand}, год выпуска {self.year}.")

    def move(self):
        print("Транспорт едет.")


class Car(Vehicle): #дочерний
    def __init__(self, brand, year, max_speed):
        super().__init__(brand, year)
        self.max_speed = max_speed

    def move(self):
        print(f"{self.brand} едет по дороге.")

    def show_speed(self):
        print(f"Максимальная скорость: {self.max_speed} км/ч.")


car = Car("Lada Sport", 2026, 300)
car.info()
car.move()
car.show_speed()