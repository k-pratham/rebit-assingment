# ques 1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def display(self):
        print(
            f"Vehicle Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}"
        )


car1 = Vehicle("hyundai", "I20", "2024")
print(car1)

# ques2
print("--")
print("Answer for Ques 2")
car1.display()

# Ques3
print("--")
print("Answer for Ques 3")


class Car(Vehicle):
    def __init__(self, make, model, year, doors, engine_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.engine_type = engine_type

    def display_info(self):
        print(
            f"Vehicle Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\ndoors: {self.doors}\nengine_type: {self.engine_type}"
        )

    def start_engine(self):
        print(f"{self.engine_type} is starting.")


car2 = Car("hyundai", "I20", 2024, 4, "BS6")
car2.display_info()

# ques 4
print("--")
print("Answer for ques 4: ")
car2.start_engine()

# ques 5
print("--")
print("Answer for ques 5: ")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count, bicycle_type):
        super().__init__(make, model, year)
        self.gear_count = gear_count
        self.bicycle_type = bicycle_type

    def display_bicycle_info(self):
        print(
            f"bicyle type:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\ngear_count : {self.gear_count}\nbicycle_type : {self.bicycle_type} "
        )


bicycle1 = Bicycle("firefox", "mountain bike", 2023, 21, "ranger")
bicycle1.display_bicycle_info()
