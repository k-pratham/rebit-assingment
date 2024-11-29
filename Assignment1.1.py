import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def display_info_circle(self):
        area = self.calculate_area()
        print(f"Circle Information:\nRadius: {self.radius}\nArea: {area:.2f}")


my_circle = Circle(8)
my_circle.display_info_circle()

# ques7
print("--")
print("Answer for ques 7:")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info_rectangle(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(
            f"Rectangle Information:\nLength: {self.length}\nWidth: {self.width}\nArea: {area}\nPerimeter: {perimeter}"
        )


my_rectangle = Rectangle(15, 8)
my_rectangle.display_info_rectangle()

# ques8
print("--")
print("Answer for ques 8:")


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def print_email(self):
        email = f"{self.employee_id}@company.com"
        print(f"Email Address: {email}")

    def display_info_emp(self):
        print(
            f"Employee Information:\nName: {self.name}\nEmployee ID: {self.employee_id}"
        )
        self.print_email()


# Example usage:
employee = Employee("Johnson fernandes", "johnson.fernandes")
employee.print_email()
employee.display_info_emp()

# ques9
print("--")
print("Answer for ques 9:")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def print_department_details(self):
        print(f"Department: {self.department}")

    def display_info(self):
        # super().display_info_manager()
        self.print_department_details()


manager = Manager("ram kumar", "ram.kumar", "Data Engineering")
manager.display_info()
