"""
DESCRIPTION:
The following functions represent an advanced knowledge Python.
Each function or group of functions is seperated by a single line comment of X's.
Each function or group of functions begin with a multi-line comment describing the functions purpose.
These functions are the result of self-teaching as well as practice exercises found through W3resource.
"""


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Fibonacci
The function 'fib' interprets the input 'length' to return a fibonacci sequence of the given length.
"""

def fib(length):
    fib_list = [1 , 1]
    frame_list = list(range(length - 2))
    if length <= 0:
        return "Invalid Parameters"
    elif length == 1:
        return [1]
    elif length == 2:
        return fib_list
    else:
        for i in frame_list:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Chalkboard
The following functions print a phrase a specified number of times.
"""

def chalkboard(phrase , num):
    for i in list(range(num)):
        print(phrase)

chalkboard('I will not chew gum in class.' , 5)

def chalkboard2(phrase , num):
    print phrase * num

chalkboard2('I will not chew gum in class.' , 10)




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Greatest Common Divisor (GCD)
The following function returns the greatest common divisor of two integers.
"""

def gcd(integer1 , integer2):
    max_int = max(integer1 , integer2)
    frame_list = list(range(max_int))
    divisors_int1 = []
    divisors_int2 = []
    for i in frame_list:
        if i == 0:
            continue
        if integer1 % i == 0:
            divisors_int1.append(i)
        if integer2 % i == 0:
            divisors_int2.append(i)
    common_divisors = []
    for i in divisors_int1:
        if i in divisors_int2:
            common_divisors.append(i)
    return max(common_divisors)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Least Common Multiple (LCM)
The following function returns the least common multiple (LCM) of two integers.
"""
def lcm(integer1 , integer2):
    max_multiple = integer1 * integer2
    frame_list = list(range(max_multiple))
    multiples_int1 = []
    multiples_int2 = []
    for i in frame_list:
        if i == 0:
            continue
        else:
            multiples_int1.append(i * integer1)
            multiples_int2.append(i * integer2)
    common_multiples = []
    for i in multiples_int1:
        if i in multiples_int2:
            common_multiples.append(i)
    return min(common_multiples)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Height Conversion
The following function returns a height (in feet and inches) converted to centimeters.
"""

def height_convert(feet , inches):
    feet_in_inches = feet * 12
    total_inches = inches + feet_in_inches
    height_in_cm = total_inches * 2.54
    return "Height in cm is " + str(height_in_cm)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Distance Conversion
The following function takes an input of distance in feet and returns a distance as
a string of miles, yards, feet, and inches.
"""

def imperial(distance_in_feet):
    inches = distance_in_feet * 12
    miles = round(inches / 63360)
    remaining_inches_after_miles = inches % 63360
    yards = round(remaining_inches_after_miles / 36)
    remaining_inches_after_yards = remaining_inches_after_miles % 36
    feet = round(remaining_inches_after_yards / 12)
    remaining_inches_after_feet = remaining_inches_after_yards % 12
    return "Distance is " + str(miles) + " miles " + str(yards) + " yards " + \
        str(feet) + " feet and " + str(round(remaining_inches_after_feet , 2)) + " inches"



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Body Mass Index (BMI)
The following function returns the BMI based on a height in inches and a weight in pounds.
"""

def bmi(height_in_inches , weight_in_lbs):
    body_mass_index = 703 * (weight_in_lbs / ((height_in_inches) ** 2))
    return body_mass_index



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Organize Integers (Knowledge Exercise)
The following function sorts three integers from largest to smallest WITHOUT using conditional statements or loops.
"""

def organize_integers(num1 , num2 , num3):
    list_of_integers = [num1 , num2 , num3]
    first_highest = max(list_of_integers)
    list_of_integers.remove(first_highest)
    second_highest = max(list_of_integers)
    list_of_integers.remove(second_highest)
    third_highest = max(list_of_integers)
    final_list = [first_highest , second_highest , third_highest]
    return final_list



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
All Greater Than
The following function returns a string showing whether all numbers in a list are greater than 25.
"""

def greaterthan_25(list_of_numbers):
   test_list = []
   for i in list_of_numbers:
        if i >= 25:
            test_list.append(1)
        else:
            test_list.append(0)
   if max(test_list) == 0:
       return "All numbers less than 25"
   else:
       return "Atleast one number greater than or equal to 25"



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Divisible by 15
The following function takes an input list of numbers and returns a sublist of numbers divisible by 15.
"""

test_list = [10, 26, 69, 47, 15, 38, 50, 30, 29, 45, 77]

def div_by_15(list1):
    final_list= []
    for i in list1:
        if i % 15 == 0:
            final_list.append(i)
        else:
            continue
    return final_list

#print(div_by_15(test_list))



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
List All Files in a Directory, Search Directory
The following program lists all files in a folder on the desktop allowing for files to be searched.
"""

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('/Users/Nayeem/Desktop/WORKING'):
        f.append(filenames)

searchlist = []

for i1 in f:
    for i2 in i1:
        if i2 == 'testfile.csv':
            searchlist.append(i2)

print(searchlist)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#THE END
