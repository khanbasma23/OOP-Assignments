# 1. Student class with self assignment
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")


# Test
s1 = Student("Ali", 85)
s1.display()


# 2. Counter class with class variable
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")


# Test
c1 = Counter()
c2 = Counter()
Counter.display_count()


# 3. Car with public variable and method
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")


# Test
car1 = Car("Toyota")
car1.start()
print("Brand:", car1.brand)


# 4. Bank class with class method
class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# Test
print("Before change:", Bank.bank_name)
Bank.change_bank_name("MyBank")
print("After change:", Bank.bank_name)


# 5. MathUtils with static method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# Test
print("Sum is:", MathUtils.add(10, 5))


# 6. Logger with constructor and destructor
class Logger:
    def __init__(self):
        print("Logger created.")

    def __del__(self):
        print("Logger destroyed.")


# Test
logger = Logger()
del logger


# 7. Access modifiers
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_private_ssn(self):
        return self.__ssn


# Test
emp = Employee("Ayesha", 50000, "123-45-6789")
print("Name:", emp.name)
print("Salary (protected):", emp._salary)
# print(emp.__ssn)  # Error: cannot access private directly
print("SSN (via method):", emp.get_private_ssn())


# 8. super() usage
class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# Test
t = Teacher("Ms. Fatima", "Math")
print("Teacher Name:", t.name)
print("Subject:", t.subject)


# 9. Abstract class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Test
rect = Rectangle(5, 4)
print("Area of Rectangle:", rect.area())


# 10. Dog instance method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


# Test
dog = Dog("Buddy", "Labrador")
dog.bark()


# 11. Book with class method
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# Test
Book.increment_book_count()
Book.increment_book_count()
print("Total Books:", Book.total_books)


# 12. TemperatureConverter static method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# Test
print("37°C =", TemperatureConverter.celsius_to_fahrenheit(37), "°F")


# 13. Composition
class Engine:
    def start(self):
        return "Engine started."


class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        return self.engine.start()


# Test
engine = Engine()
car = CarWithEngine(engine)
print(car.start_engine())


# 14. Aggregation
class Department:
    def __init__(self, employee):
        self.employee = employee


class EmployeeBasic:
    def __init__(self, name):
        self.name = name


# Test
e = EmployeeBasic("Usman")
d = Department(e)
print("Department has employee:", d.employee.name)


# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        return "A"


class B(A):
    def show(self):
        return "B"


class C(A):
    def show(self):
        return "C"


class D(B, C):
    pass


# Test
d = D()
print("MRO Output:", d.show())  # B will be called because of MRO


# 16. Function decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper


@log_function_call
def say_hello():
    return "Hello!"


# Test
print(say_hello())


# 17. Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls


@add_greeting
class DecoratedPerson:
    pass


# Test
p = DecoratedPerson()
print(p.greet())


# 18. Property decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


# Test
product = Product(100)
print("Price:", product.price)
product.price = 150
print("Updated Price:", product.price)
del product.price


# 19. callable class
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# Test
m = Multiplier(3)
print("Result:", m(5))
print("Is callable?", callable(m))


# 20. Custom exception
class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    return "Age is valid."


# Test
try:
    print(check_age(16))
except InvalidAgeError as e:
    print("Error:", e)


# 21. Custom iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# Test
print("Countdown:")
for num in Countdown(5):
    print(num)
