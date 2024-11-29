# ques 10
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"

    def add(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def multiply(self, other):
        real_product = self.real * other.real - self.imaginary * other.imaginary
        imaginary_product = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_product, imaginary_product)


num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

sum_result = num1.add(num2)
print(f"Sum: {sum_result}")

product_result = num1.multiply(num2)
print(f"Product: {product_result}")

# ques 11
print("--")


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100) * self.price
        self.price -= discount_amount

    def book_details(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: Rs{self.price:.2f}"


book = Book("What is chat GPT", "Stephen Wolfram", 250.00)

book.apply_discount(10)

print(book.book_details())


# ques 12
print("--")
print("ques 13")


class Flight:
    def __init__(self, airline, flight_number):
        self.airline = airline
        self.flight_number = flight_number
        self.passengers = []

    def add_passenger(self, passenger_name):
        self.passengers.append(passenger_name)

    def remove_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
        else:
            print(f"{passenger_name} is not on this flight.")

    def flight_details(self):
        return f"Airline: {self.airline}\nFlight Number: {self.flight_number}\nPassengers: {', '.join(self.passengers)}"


flight = Flight("Indigo", "IG1234")

flight.add_passenger("Mary")
flight.add_passenger("Lisa")

print(flight.flight_details())

flight.remove_passenger("Mary")

print(flight.flight_details())

# ques14
print("--")


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")


animal = Animal("Dog")
print(f"Species: {animal.species}")
animal.make_sound()


# ques 15
class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def make_sound(self):
        print("Woof")


class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

    def make_sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

print(f"Species: {dog.species}")
dog.make_sound()

print(f"Species: {cat.species}")
cat.make_sound()
