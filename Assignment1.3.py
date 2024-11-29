# ques 16
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


calculator = Calculator()

print("Addition:", calculator.add(10, 5))

print("Subtraction:", calculator.subtract(10, 5))

print("Multiplication:", calculator.multiply(10, 5))

print("Division:", calculator.divide(10, 5))
print("Division by zero:", calculator.divide(10, 0))

# ques 17
print("--")


class WeatherForecast:
    def __init__(self):
        self.temperatures = []

    def add_temperature(self, temperature):
        self.temperatures.append(temperature)

    def get_average_temperature(self):
        if not self.temperatures:
            return "No temperature readings available."
        return sum(self.temperatures) / len(self.temperatures)


forecast = WeatherForecast()

forecast.add_temperature(72)
forecast.add_temperature(75)
forecast.add_temperature(68)

average_temp = forecast.get_average_temperature()
print(f"Average Temperature: {average_temp}")


# ques18,19,20
class Polygon:
    def perimeter(self):
        print("used by subclass")

    def area(self):
        print("Used by subclass")


class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side**2


triangle = Triangle(3, 4, 5)
print("Triangle Perimeter:", triangle.perimeter())
print("Triangle Area:", triangle.area())

square = Square(4)
print("Square Perimeter:", square.perimeter())
print("Square Area:", square.area())


# Q21
import time


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            print("not started")
            return None
        return time.time() - self.start_time


timer = Timer()

timer.start()
print("Timer started. Performing a task...")


time.sleep(2)

elapsed_time = timer.stop()
print(f"Elapsed Time: {elapsed_time:.2f} seconds")


# Q22:-
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue is empty"

    def view_queue(self):
        return self.queue


queue = Queue()


queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Queue after enqueueing:", queue.view_queue())

print("Dequeued:", queue.dequeue())
print("Queue after dequeueing:", queue.view_queue())
queue.dequeue()
queue.dequeue()
print("Dequeued from empty queue:", queue.dequeue())


# Q23:-
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def size(self):
        return len(self.stack)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushing:", stack.size())


print("Popped item:", stack.pop())
print("Stack after popping:", stack.size())

# Check stack size
print("Stack size:", stack.size())

# Pop until empty
stack.pop()
stack.pop()
print("Popped from empty stack:", stack.pop())


# Q24:-
class MusicPlayer:
    def __init__(self):
        self.current_track = None

    def load_track(self, track):
        self.current_track = track
        print(f"Loaded track: {track}")

    def play(self):
        if self.current_track:
            print(f"Playing track: {self.current_track}")
        else:
            print("No track loaded")

    def stop(self):
        print("Music stopped")


player = MusicPlayer()


player.play()

player.load_track("Imagine - John Lennon")
player.play()
player.stop()
player.load_track("Thriller - Michael Jackson")
player.play()


# Q25:-
class database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connect = False

    def db_connect(self):
        if not self.connect:
            self.connect = True
            print("Connected to{self.db_name}")
        else:
            print("Not connected")

    def db_disconnect(self):
        if self.connect:
            print("Disconnected")
        else:
            print("Not connected")

    def execute_query(self, query):
        if not self.connect:
            print("Executing {query}")
        else:
            print("Wrong")


db = database("TestDB")


db.db_connect()

db.execute_query("SELECT * FROM users")
db.db_disconnect()
db.execute_query("SELECT * FROM users")
