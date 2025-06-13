# Problem 1:
# Print your name.
print("My name is Milan Kumar Chaudhary")


# Problem 2:
# Print sum of two integers.
int1 = 32
int2 = 64
print('Sum is', int1 + int2)


# Problem 3:
# Print difference of two floats.
float1 = 3.14
float2 = 66.33
print('Difference is', float1 - float2)


# Problem 4:
# Convert temperature Celsius to Fahrenheit.
temperature = 21
print('Temperature in Fahrenheit is', temperature + 273.15)


# Problem 5:
# Area of circle (πr²).
radius = int(5)
pie = float(3.14)
print('Area of circle is', pie*pow(radius, 2))


# Problem 6:
# Swap two variables.
a = 10
b = 20
a, b = b, a
print(a,b)


# Problem 7:
# Read name + age, print formatted sentence.
a = input('What is your name: ')
b = int(input('What is your age: '))
print(f'Hello, {a}. Your age is {b}!')


# Problem 8:
# Compute BMI (kg/m²)
actual_weight = float(input("Enter your weight (kg): "))
actual_height = float(input("Enter your height (m): "))

bmi = actual_weight / (actual_height ** 2)
bmi = round(bmi, 2)

print(f"Your BMI is {bmi}")


# Problem 9:
# Calculate compound interest.
p = float(input("Enter the principal: "))
r = float(input("Enter Annual Interest Rate: "))
n = float(input("Enter the Number of Times the Interest Compounds per Year: "))
t = float(input("Enter the Total Number of Years: "))
r_final = r/100
a = p*pow(1 + r_final/n, n*t)
print(a)


# Problem 10:
# Convert seconds to hours:minutes:seconds.
user_input = float(input('Enter time in seconds: '))
hours = user_input/3600
minutes = user_input/60
seconds =  user_input
print(f'Time in hr:min:sec = {hours}:{minutes}:{seconds}')


# Problem 11:
# Simple interest calculator.
p = int(input('Enter the principal: '))
r = float(input('Enter the annual intrest rate: '))
t = float(input('Enter the time period(yrs): '))
a = (p*r*t)/100
print(f'The simple intrest = {a}')


# Problem 12:
# Compute average of 5 marks.
user_input = float(input('Enter your total marks to get average: '))
average = user_input/5
print(f'Average of your marks = {average}')


# Problem 13:
# Convert kilometers to miles.
user_input = float(input('Enter the distance in Km: '))
trans = float(user_input-0.378629)
print(f'{user_input} into miles = {trans}')


# Problem 14: (Hard)
# Check if number is even/odd.
user_input = int(input('Write a number: '))
if user_input % 2 != 0:
    print('Your number is odd')
else:
    print('Your number is even')


# Problem 15: 
# Calculate perimeter of rectangle.
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
perimeter = 2 * (length + width)
print(f"15. Perimeter of rectangle = {perimeter}")


# Problem 16:
# Calculate area of triangle.
base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = 0.5 * base * height
print(f"16. Area of triangle = {area}")


# Problem 17:
# Compute square root.
import math
num = float(input("\nEnter number to find square root: "))
square_root = math.sqrt(num)
print(f"17. Square root of {num} = {square_root}")


# Problem 18:
# Compute power (x^y).
x = float(input("\nEnter base (x): "))
y = float(input("Enter exponent (y): "))
power = pow(x, y)
print(f"18. {x}^{y} = {power}")


# Problem 19:
# Calculate remainder of division.
a = int(input("\nEnter dividend: "))
b = int(input("Enter divisor: "))
remainder = a % b
print(f"19. Remainder of {a} divided by {b} = {remainder}")


# Problem 20: 
# Convert age (years) to days.
age = int(input("\nEnter your age in years: "))
days = age * 365
print(f"20. Your age in days = {days}")