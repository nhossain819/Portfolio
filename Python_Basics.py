"""
DESCRIPTION:
The following functions represent a basic knowledge Python.
Each function or group of functions is seperated by a single line comment of X's.
Each function or group of functions begin with a multi-line comment describing the functions purpose.
This is the result of self-teaching as well as practice exercises found through W3resource.
"""

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
List Comparison
The following function returns a list of colors from color_list_1 which are not present in color_list_2.
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def inlist1_notinlist2(list1 , list2):
    new_list = []
    for i in list1:
        if i in list2:
            continue
        else:
            new_list.append(i)
    return new_list


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Calculation
The following function uses an input of base and height to return area of a triangle.
"""

def tri_area(base , height):
    return base * height * (1/2)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Odds or Evens
The following functions determine if an input is an odd or even number.
This function is also written as a lambda function.
"""
#Written as a regular function.
def odd_even(x):
    if x % 2 == 0:
        return "This number is even!"
    else:
        return "This number is odd!"


#Written as a lambda function.
odd_even2 = lambda x: "This number is even!" if x % 2 == 0 else "This number is odd!"


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Distance Between Two Points
The following function returns the distance between two graphical points.
"""
def distance(x1,x2,y1,y2):
    answer = (y2 - y1) / (x2 - x1)
    return answer

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
List Sum
The following function returns the sum of a list.
"""

def full_sum(num):
    framelist = list(range(num + 1))
    return sum(framelist)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Hypotenuse
The following function returns the hypotenuse of a triangle using the lengths of two sides.
"""

def hypotenuse(side_a , side_b):
    return ((side_a ** 2) + (side_b ** 2)) ** (1/2)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Count the number of 4s
This function provides the number of 4s in a list of integers.
"""
list_of_numbers = [1, 5, 8, 4, 8, 3, 6, 4, 7, 9, 4, 3]

count_of_4s = list_of_numbers.count(4)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
A function to get a number of copies of the first 2 characters of a given string.
If the length is less than 2, return the number copies of the whole string.
"""

def two_char(phrase , num):
    if len(phrase) >= 3:
        return phrase[:2] * num
    elif len(phrase) < 3:
        return phrase * num


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Vowels
This function determines if a input letter is a vowel.
"""

def vowel(letter):
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    if letter.lower() in vowels:
        return "This letter is a vowel."
    else:
        return "This is not a vowel."

"""
List to String
This function concatenates all elements of a list into a string.
"""

def big_string(list_of_values):
    return ' '.join(list_of_values)

test_list = ['a' , 'b' , 'c']



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
A function to return all even numbers from a list in the same order, stop the printing
if any numbers that come after 219 in the sequence.
"""
numbers = [
    376, 442, 57, 438, 807, 354, 136, 365, 843, 576, 697, 948, 428, 685, 923, 395,
    299, 142, 728, 219, 978, 337, 432, 536, 829, 238, 766, 951, 636, 948, 677, 227,
    814, 57, 124, 54, 532, 27, 894, 892, 762, 543, 71, 369, 842, 841, 435, 745, 727,
    952, 723, 537
    ]

def evens_until_219(numlist):
    new_list = []
    for i in list(numlist):
        if i % 2 == 0:
            new_list.append(i)
        elif i == 219:
            break
    return new_list

print(evens_until_219(numbers))
