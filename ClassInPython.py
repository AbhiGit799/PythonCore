'''

1) pass simply means:

"I don't want to put anything inside the class yet."

We can create an object from this class:

car1 = Car()



3. Creating an object

The basic syntax is:

object_name = ClassName()


4. What is a constructor?

A constructor is a special method that runs automatically when an object is created.

In Python, the constructor-like initializer is:

__init__()


6. What is self?

This is probably the most important new concept for you.

Look at:

class Car:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

self means:

the current object

Suppose:

car1 = Car("Civic", "Honda")

Then:

self

refers to:

car1

So:

self.name = name

means approximately:

car1.name = "Civic"

And:

self.brand = brand

means:

car1.brand = "Honda"


8. Methods inside a class

A function inside a class is generally called a method.

Example:

class Car:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def display(self):
        print(self.name, self.brand)

Create an object:

car1 = Car("Civic", "Honda")

Call the method:

car1.display()

Output:

Civic Honda

Notice:

def display(self):

The method receives self, which represents the current object.

10. Python vs Java

| Concept        | Python               | Java                   |
| -------------- | -------------------- | ---------------------- |
| Class          | `class Car:`         | `class Car { }`        |
| Constructor    | `__init__()`         | `Car()`                |
| Create object  | `car = Car()`        | `Car car = new Car();` |
| Method         | `def display(self):` | `void display() {}`    |
| Current object | `self`               | `this`                 |
| Function       | `def add(a,b):`      | `int add(int a,int b)` |
| Print          | `print()`            | `System.out.println()` |




'''


class Car:
    pass


car1 = Car()
car2 = Car()


print(car1)
print(car2)

class Bike:
    def __init__(self):
        print("A bike is created!")

bike1 = Bike()

print(bike1);


class Truck:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(self.make, self.model)

truck1 = Truck("Ford", "F-150")
print(truck1.make)
print(truck1.model)

truck2 = Truck("Chevrolet", "Silverado")
print(truck2.make)
print(truck2.model)
truck1.display()
truck2.display()


'''

The 5 things to remember

For now, focus on these:

1. def
   ↓
   Creates a function/method

2. class
   ↓
   Creates a blueprint

3. __init__
   ↓
   Runs automatically when an object is created

4. self
   ↓
   Represents the current object

5. object = ClassName()
   ↓
   Creates an object


One important Python detail: __init__ is technically an initializer, not the object allocator itself; 
Python creates the instance first and then calls __init__ to initialize it. For beginner-level Python, 
though, you'll commonly hear __init__ called the constructor.




'''
