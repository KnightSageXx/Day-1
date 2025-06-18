# Problem 1:
# Calculate the perimeter 
# and area of a rectangle given its length and width.
user_input_0 = float(input('Enter the lenght: '))
user_input_1 = float(input('Enter the bredth: '))
user_input_2 = input('Enter if wanna find area or perimeter: ')
area = user_input_0*user_input_1
perimeter = 2*(user_input_0 + user_input_1)
if user_input_2 == 'area':
    print(area)
else:
    print(perimeter)


# Problem 2:
# Convert a number of days into years, weeks, and days.
user_input = int(input('Enter the number of days: '))
y = user_input/365
w = user_input/52
d = user_input
print(f"Number of days into years:weeks:days = {y}:{w}:{d}")


# Problem 3:
# Given two numbers, 
# calculate their average, difference, product, and quotient.
user_input_0 = float(input('Enter the first number(max. or  largest number or divident): '))
user_input_1 = float(input('Enter the second number(min. or smallest number or divisor): '))
user_input_2 = input("What is the operation you want to have(average, difference, product, quotient: ")
if user_input_2 == 'difference':
    print(user_input_0 - user_input_1)
elif user_input_2 == 'average':
    print(user_input_0/user_input_1)
elif user_input_2 == 'product':
    print(user_input_0*user_input_1)
elif user_input_2 == 'quotient':
    print(user_input_0/user_input_1)
else:
    print('Enter a valid operation from above!')


# Problem 4:
# Given a temperature in Fahrenheit, convert it to Celsius.
user_input = float(input('Enyer the temperature in Fahrenheit: '))
converstion = user_input-273.15
print(f'The {user_input} in celcius = {converstion}')


# Problem 5:
# Convert meters to centimeters, inches, and feet.
user_input = float(input('Enter the lenght of anything in meters: '))
c = user_input/100
i = user_input/39.37
f = user_input/3.28
print(f'Converstion of {user_input}m into centimeter:inches:feets = {c}:{i}:{f}')


# Problem 6:
# Compute simple interest (P, R, T given).
p = float(input('Enter the principal: '))
i = float(input('Enter the annual intrest: '))
t = float(input('Enter the time period(yrs): '))
a = (p*i*t)/100
print(f"The simple intrest = {a}")


# Problem 7:
# Given distance (in km) and time (in hours), calculate speed.
user_input_0 = float(input('Enter the distance(km): ')) 
user_input_1 = float(input('Enter the time(hr): '))
ans = user_input_0/user_input_1
print(f"The speed is equal to {ans}")


# Problem 8:
# Given total marks and marks obtained, 
# calculate percentage and grade (grade = A, B, C based on %).
total_marks = int(input('Enter the total marks in exam: '))
marks_obtained = float(input('Enter the marks obtained: '))
percentage = (marks_obtained/total_marks)*100
print(f'You obtained a percentage of {percentage}')
if percentage >= 80:
    print('You got A')
elif  percentage < 80 and percentage > 50:
    print('You got B')
elif percentage < 50 and percentage > 33:
    print('You got C')
else:
    print('FAIL')


# Problem 9:
# Convert given seconds into days, hours, minutes, and seconds.
user_input = int(input('Enter the time in seconds: '))
days = user_input/86400
hours = user_input/3600
minutes = user_input/60
print(f'{user_input}s = {days}:{hours}:{minutes}:{user_input}')


# Problem 10:
# Calculate area and circumference of a circle (given radius).
user_input = int(input('Enter the radius of the circle: '))
area = 3.14*pow(user_input, 2)
perimeter = 2*(3.14*user_input)
print(f'Area and Perimeter of circle with radius of {user_input} = {area}  area, {perimeter} perimeter')


# Problem 11:
# Given base and height, calculate area of triangle.
user_input_0 = int(input('Enter the length of base of triangle: '))
user_input_1 = int(input('Enter the height of triangle: '))
area = 1/2*user_input_0*user_input_1
print(f'Area of triangle = {area}')


# Problem 12:
# Swap three variables without using any extra variable.
a = 10
b = 20
c = 30
a, b, c = c, b, a
print('The swap =', a, b, c)


# Problem 13:
# Calculate electricity bill with simple slab rules 
# (e.g., first 100 units = 5 Rs/unit, next 100 units = 8 Rs/unit, rest 10 Rs/unit).
units = int(input('Enter the number of units consumed: '))
if units <= 100:
    bill = units*5
    print(f'You electricity bill is {bill}')
elif units > 100 and units <= 200:
    bill = units*8
    print(f'You electricity bill is {bill}')
elif units > 200:
    bill = units*10
    print(f'You electricity bill is {bill}')
else:
    print('ERROR')