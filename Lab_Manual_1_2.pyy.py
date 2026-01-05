#####1.1
# Ask the user to enter weight in kilograms
kilograms = float(input("Enter weight in kilograms: "))

# Convert kilograms to pounds
pounds = kilograms * 2.2

# Display the result
print(f"{kilograms} kilograms is equal to {pounds} pounds.")



####1.2
# Start from 8, go up to 89, increment by 3
for num in range(8, 90, 3):
    print(num, end=', ' if num != 89 else '\n')

###1.3
s = "hello"
char_list = list(s)
print(char_list)

###1.4
# List of numbers
numbers = [12, 45, 7, 89, 23, 56]

# Method 1: Using max() function
largest = max(numbers)
print(f"The largest number is: {largest}")

# Method 2: Using a for loop
largest_number = numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"The largest number (using loop) is: {largest_number}")

###1.5
# Function to calculate nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# Input from user
n = int(input("Enter the position (n) of Fibonacci number: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

###2.1
# Define the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False  # To track the state of the car

    # Method to start the car
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} ({self.year}) has started.")
        else:
            print(f"{self.make} {self.model} is already running.")

    # Method to stop the car
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.make} {self.model} ({self.year}) has stopped.")
        else:
            print(f"{self.make} {self.model} is already stopped.")

    # Optional: Method to display car info
    def display_info(self):
        print(f"Car Info: {self.make} {self.model}, Year: {self.year}")

# Example usage
my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info()
my_car.start()
my_car.start()  # Trying to start again
my_car.stop()
my_car.stop()   # Trying to stop again


###2.2

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

# Derived class Dog
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Derived class Cat
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

    def scratch(self):
        print(f"{se

###2.3

# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Derived class Dog
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# Derived class Cat
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

# Derived class Bird
class Bird(Animal):
    def make_sound(self):
        print("Chirp! Chirp!")

# Demonstrate polymorphism
def main():
    animals = [Dog(), Cat(), Bird()]

    for animal in animals:
        animal.make_sound()  # Same method behaves differently depending on object

if __name__ == "__main__":
    main()




###2.4
# Program to demonstrate division with error handling

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    result = numerator / denominator
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers.")

finally:
    print("Program execution completed.")

























