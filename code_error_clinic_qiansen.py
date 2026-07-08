#Snippet 1 
x = 10
y = 5
result = x / y
print("Result:", result)
#1: I predict that there will be a ZeroDivisionError because you can't divide by ze
#Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i - 1])
#1: I predict that there will be an IndexError 
#Snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))
#1: I predict that there will be a SyntaxError
#Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
#1: i predict that there will be a type error and an indentation error
#Snippet 5
for i in range(5):
    print(i)
#1: I predict that there will be a syntax error and and indentation error
#Snippet 6
def greet(name):
    return "Hello, " + name
print(greet("Alice"))
#1: I predict that there will be a type error and an indentation error
#Snippet 7
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)
#1: I predict that there'll be an indentation error
#Snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#1: I predict that there will be an infinite loope and an indenrtation error
#Snippet 9
name = input("Enter your name: ")
if name == "Alice" or name =="Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
#1: I predict that there will be a logic error and an indentation error 
#Snippet 10
def divide_numbers(x, y):
    result = x / y
    return result
    num1 = 10
    num2 = 0
    if num2 != 0:
         print(divide_numbers(num1, num2))
    else: 
        print("can't divide by zero")
#1: I predict that there will be a zero division error 