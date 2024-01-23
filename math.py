import math

a = int(input("Enter a number: "))  # taking the number as an integer.
b = int(input("Enter a second number: "))  # taking the second number as an integer.

p = math.pow(a, b)  # math.pow = power fuction, raises value a to power b (a^b).
print(p)

s = math.sqrt(
    a
)  # math.sqrt = square root, does the square root to any value inside ().
print(s)

var = math.floor(27.15)  # math.floor = flooring the number, essentially roudning down.
varTwo = math.ceil(15.29)  # math.ceil = rounding the number up (ceiling is up).
varThree = math.fabs(-27)  # math.fabs = absolute value.
varFour = math.pi  # math.pi = prints the value of pi.
print(var)
print(varTwo)
print(varThree)
print(varFour)
