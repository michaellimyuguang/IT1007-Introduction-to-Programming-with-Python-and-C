# Lecture 1
# Import packages
'''from math import pi, cos #import certain elements from math
print(cos(pi))

#Another way to import packages
import math
print(math.cos(math.pi)) #import the whole math package

#Shortform of writing math
import math as m #it can be m or any other variables
print(m.cos(m.pi))


# Lecture 2
# Function types
print(type(123)) #int
print(type('123')) #str
print(type(None)) #NoneType
print(type(True)) #bool
print(type(45.2)) #float

#Type conversion
print(str(123)) #123
print(float(45.2222)) #45.2222
print(int(25.444)) #25

# Assignments
x = 10
x = 2
x = 4

print(x) #Output will be 4. The x value reassign to the newest value

a, b, c = 1, 2, 3
a, b, c = c, b, a

print(a, b, c) #3 2 1

# Arithmetic
a = 2 * 3
print(a) #6

b = 2 ** 3
print(b) #8

c = 11 / 3
print (c) #3.666666

d = 11 // 3
print (d) #3 (take the whole number)

e = 11 % 3
print (e) #2 (remainder)

# Truth Values
print(2 > 1) #True
print(5 < 3) #False

# Operators
print(2 != 3) #True( != means not equal to)
print('1' == 1) #False
print(True = True) #Error (must use ==)
print(True != True) #False 

# Strings
s = 'ba'
t = 'na'
print(s+t) #bana
print(s+(t*2)) #banana

u = s + t
print('z' in u) #False (alphabet z is not in u)
print('ba' > u) #False
print('bana' <= u)  #True 

#String slicing
s = 'abcdef'
print(s[0]) #a
print(s[2]) #c
print(s[0:2]) #ab
print(s[1:2]) #b
print(s[:2]) #ab (blank means 0)
print(s[1:5:3]) #be (include the start number then skip 3 including the start number)
print(s[::2]) #ace (include the start number then skip 2 including the start number)
print(s[::-1]) #fedcba
print(s[::-2]) #fdb
print(s[-4:-1:-1]) #no output
print(s[-1:-4:-1]) #fed
print(s[::0]) #error because step cannot be zero

#Lecture 3

#Writing a function
def square(x):
    return x * x

#>>square(3)
#9
#>>square(square(2))
#16
#>>square(3, 4)
#Error

#Input function
def addTwoNumbers():
    a = int(input('Enter an integer:'))
    b = int(input('Enter an integer:'))
    print(a+b) 

#Factorial using while loop
def factorial(n):
    ans = 1
    i = 1
    while i <= n: #this will keep on producing i which is 1 1 1 1 1 1 1 1
        ans = ans * i # ans = 1 * 1
        i = i + 1 #i is no longer 1. It is 1,2,3,4,5,...n # 2,3,4,5,...n will be placed into ans to generate new ans until n
    return ans

def factorial2(n):
    ans = 1
    i = 1
    while i <= n:
        i = i + 1 #this is wrong because the first i will be 2 and the last i will be 4 if n = 3
        ans = ans * i     
    return ans


#def sigma(n):
    ans = 0
    i = 1
    while i <= n: #this will keep on producing i which is 1 1 1 1 1 1
        ans = ans + i**2 # ans = 0 + 1**2
        i = i + 1 #i is no longer 1. It is 1,2,3,4,5,....n will be placed into the ans to generate new ans until n
    return ans

#Factorial using for loop
def factorial3(n):
    ans = 1
    for i in range(1, n+1): # i is 1,2,3,4,5,...n
        ans = ans * i # ans = 1*2*3*4*5...*n
    return ans

#Sigma using for loop
def sigma2(n):
    ans = 0
    for i in range(1, n+1): #i is 1,2,3,4,5,...,n
        ans = ans + i**2 # ans = 0 + 1**2, 2**2,..., n**2
    return ans

#If, else
a = 4
if a < 10: #Satisfy
    if a < 1:  #Did not satisfy
        print(a) #No output
b = 4
if b > 0:
    print('Hi') #Satisfy
elif b == 2:
    print('Bye')
elif b == 4: #Satisfy, but since the first if is already pass, python will not continue checking
    print('Goodnight')
else:
    print('Haha') #Hi

#Guess a number
import random
def guessANum():
    secret = random.randint(0,99) # 0 <= secret <= 99
    print('I have a number in mind between 0 and 99')
    guess = -1 # It must not be within 0 to 99 because if the secret happens to be the guess. The game will not start
    while guess != secret: #Game will start as secret can never be -1
        guess = int(input('Guess a number:'))
        if guess == secret:
            print('Bingo!! You got it!')
        elif guess < secret:
            print('Your number is too small')
        else:
            print('Your number is too big')

#String format
def declareAge(name, age):
    print('My name is {} and my age is {}.'.format(name,age))

#Different in indentation
x = 10

def foo():
    if x > 15: #Since x is less than 15, nothing is printed
        if x > 6:
            print(1)
        else:
            print(2)

def foo2():
    if x > 15: #Since x is less than 15, else print(2) (This can be seem as nested if)
        if x > 6:
            print(1)
    else:
        print(2)

#Lecture 4
# Adding of 2 numbers
import random

def add2Num():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    
    print( 'What is', num1, '+', num2, '?')
    answer = int(input()) #Must include 'int'. It is to tell python that you are only accepting int
    if answer == num1 + num2:
        print('Correct!')
    else:
        print('Nope! The answer is', num1+num2)
        
add2Num() 


#Lecture 5
#Pass by values
x = 0

def changeValue(n):
    n = 999
    print(n)

changeValue(x) #999
print(x) #0 

#Print vs Return
def foo_print3():
    print(3) # x = foo_print3() will give 3

def foo_return3():
    return(3) #y = foo_return3() will not give 3. foo_return3() must be type alone to get 3

#The stack
def p1(x):
    output = p2(x) # x = 3, p2(3)
    return output #return p2(3)

def p2(x): #p2(3)
    output = p3(x) # x = 3, p3(3)
    return output #return p3(3)

def p3(x): #p3(3)
    output = x * x # x =3, 3 * 3
    return output #return 9

#Recursion
def factorial(n):
    if n == 1: #Recurrsion must have a terminal condition. Must have if else
        return 1 #Only can use return
    else:
        return n * factorial(n-1) #Only can use return. factorial(n) will give n * (n-1)
def sigma(n):
    if n == 1:
        return 1
    else:
        return n**2 + sigma(n-1) #sigma(n) will give n**2 + (n-1)**2
#Global vs Local variable
x = 0

def foo_printx():
    x = 999
    print(x)


foo_printx() #999. Local variable
print(x) #0. Global variable

#Modifying the global variable
x = 1

def foo_printx():
    global x #keyword is global
    x = 5
    print(x)

foo_printx()
print(x)

#Lecture 6
#Managing complexity. Compare the 2 codes
import math
def hypotenuse(a,b):
    return math.sqrt((a**2) + (b**2))

def hypotenuse2(a,b):
    return math.sqrt(sum_of_square(a,b))
def sum_of_square(x,y):
    return square(x) + square(y)
def square(x):
    return x * x 

#Capture common patterns. Eg binomial coefficient
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
def binomial_coefficient(n, k):
    a = factorial(n)
    b = factorial(k)
    c = factorial(n-k)
    return a / (b * c) 
#Allow for code reuse
from math import pi

def square(x):
    return x * x

def area_of_circle(r):
    return pi * square(r) #Making use of the square definition to calculate area

#ceil rounds up its argument
from math import ceil

print(ceil(1.5)) #2
print(ceil(2.3)) #3 

#Lecture 7

#All indexed sequences (str,list and tuple) can...
# a[i] return i-th element of a
# a{i:j:k] return elements i up to j-1 and step k
# len(a) return number of elements in sequence
# min(a) return smallest value in sequence
# max(a) return largest value in sequence
# x in (a) return True if x is part of a
# a + b concatenates a and b
# n * a return n copies of sequence in 1 str, 1 list or 1 tuple

#String example
s = 'Minions like bananas'
print(s[5]) #n
print(s[0:6]) #Minion
print(len(s)) #20
print(max(s)) #s. Because s is rank highest in the alphabetical order
print(min(s)) # ' ' Space is rank lowest in the alphabetical order
print('o' in s) #True
print( s + ' Hello') #Minions like bananas Hello
print(3 * s) #Minions like bananasMinions like bananasMinions like bananas

#List example. List can do everything that string can do and....
a = [1,2,3,4]
b = [1,2,3,4,5]

print(a+b) #[1,2,3,4,1,2,3,4,5]

#append and remove
a.append(5)
print(a) # [1,2,3,4,5] append is always at the end of the list

a.remove(1)
print(a) # [2,3,4]

a.remove('Hello')
print(a) #Error because Hello in not in the list of a

c = [1,2,3,4,5,1,2,3,4,5]
c.remove(2)
print(c) #only the first 2 is being removed. The second 2 still remain

my_good_friends = ['Peter', 'Mary', 'John']
even_numbers_10 = [2,4,6,8,10]

my_good_friends.append(even_numbers_10)
print(my_good_friends) #['Peter', 'Mary', 'John', [2, 4, 6, 8, 10]]
print(my_good_friends + even_numbers_10) #['Peter', 'Mary', 'John', 2, 4, 6, 8, 10]

#List comprehension
a_list = []
for i in range(1,101):
    a_list.append(i) # a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

b_list = [i for i in range(1, 101)] #same answer as a_list

#List of odd number less than 100. Range can also use step
c_list = [i for i in range(1, 101, 2)] #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]


#List of even number less than 100
d_list = [i for i in range(0, 101, 2)] #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

d_list2 = [i for i in range(1, 101) if i not in c_list] #Complement of c_list

#List of first 10 squared numbers

e_list = [ i*i for i in range(1,11)] 

#Plotting graph with matplot
import matplotlib.pyplot as plt

x = [i for i in range(0,101)]
y = [i**2 for i in range(0,101)]

plt.plot(x, y) #plot the graph
plt.show() #show the graph in another screen

#Generate prime numbers <50

nonprime = [j for i in range(2,8) for j in range(i*2, 50, i)] #(2,8) is the range to detect all composite number. Step i to find all the common factor
prime = [x for x in range(1,50) if x not in nonprime] #Complement of composite number

#Tuple. Tuple is a list but cannot be modified. That means cannot use append and remove
a = (12, 13, 'dog')
print(a[0]) #12
print(a.append('cat')) #error 

#Tuple with only 1 element
a = (1)
b = (1,)

print(type(a)) #Integer
print(type(b)) #Tuple

#List is mutable
a = [1,2,3]
def changeSec(a):
    a[1] = 'changed!'
    print(a)

changeSec(a) 
print(a) #The global variable has been changed by the function

#Sets
a = {1,2,3,4,5,6,7,1,2,3} #{1,} is a set
print(a) #{1,2,3,4,5,6,7} The duplicates of 1,2,3 at the end is automatically removed

#Sets is similar to str, list and tuple except for
b = {1,2,3,4}
print(a[1]) #error
print(a[1:3]) #error
print(a + b) #error
print(5 * a) #error 

#Usual set operations
setA = {1,2,3,4}
setB = {3,4,5,6}

print(setA | setB) # {1,2,3,4,5,6}. Union
print(setA & setB) # {3,4,}. Intersection
print(setA - setB) # {1,2}. Elements in A only
print(setA ^ setB) # {1,2,5,6}. Complement of intersection

#remove in sets
setA.remove(4)
print(setA) # {1,2,3}
#setA.remove(5) # error because 5 is not an element of setA
setA.discard(5) # works the same as remove. No error even when 5 is not an element of setA 

#Dictionary
locations = {(10,30):'Macdonald', (30,99):'Burger King', (22,33): 'Pizza hut'}
print(locations[(10,30)]) #Macdonald

#Lecture 8
#Opening a txt file
with open('student_marks.txt') as f:
    data = f.read() #read the file as a string. If you type data in python shell, the string will appear
#In python shell
#>>>data
#'John 70\nMary 50\nJoe 67\nFrank 90\nGru 99\nKiki 63'

#data.split() #str is seperated and become a list. Split by \n and empty space since split()
#['John', '70', 'Mary', '50', 'Joe', '67', 'Frank', '90', 'Gru', '99', 'Kiki', '63']

#Ploting out the scores
import matplotlib.pyplot as plt
all_score = [int(i) for i in data.split()[1::2]]


plt.plot(all_score) #This does not have to be coordinates because this is a list
plt.show() 

#Opening a csv file
with open('crudebirthrate.csv') as f:
    line1 = f.readline() #read the entire first row
    line2 = f.readline() #read the entire second row
    line3 = f.readline() #read the entire third row
    print(line1)
    print(line2)
    print(line3)

#Output in python shell
year,level_1,value

1960,Crude Birth Rate,37.5

1961,Crude Birth Rate,35.2

with open('crudebirthrate.csv') as f:
    data = f.read()
    print(data)

# Output in shell
year,level_1,value
1960,Crude Birth Rate,37.5
1961,Crude Birth Rate,35.2
1962,Crude Birth Rate,33.7

with open('crudebirthrate.csv') as f:
    line1 = f.readline().rstrip('\n') #removes the character from the right
    line2 = f.readline().rstrip('\n')
    line3 = f.readline().rstrip('\n')
    print(line1)
    print(line2)
    print(line3)
#Output in python shell
year,level_1,value
1960,Crude Birth Rate,37.5
1961,Crude Birth Rate,35.2

#Ploting graph
import matplotlib.pyplot as plt
def plot_birth_rate():
    with open('crudebirthrate.csv') as f:
        f.readline() #this will discard the first line. The category of the table
        year = []
        num_birth = []
        for line in f: #the csv file will be read as row of strings
            list_form = line.rstrip('\n').split(',') #remove \n from each line and split each line by ,
            year.append(int(list_form[0])) 
            num_birth.append((float(list_form[2]) * 1000)) # Value of birth rate is x per thousand
        plt.plot(year, num_birth)
        plt.title('Number of Birth') #Show title on graph
        plt.show()
plot_birth_rate()

#Writing a file

def write_something1(
    ):
    with open('my_file.txt', 'w') as f:
        f.write('I love python')
        f.write('I love C')
write_something1() #I love pythonI love C

def write_something2():
    with open('my_file.txt', 'w') as f:
        f.write('I love python\n')
        f.write('I love C')
write_something2() #I love python
                   #I love C



#Lecture 9
#Numpy
import numpy as np
x1 = np.arange(0, 3.14, 0.1) #Get values between 0 and 3.14 by interval of 0.1. arange not arrange 

>>>x1
array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,
        1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9,  2. ,  2.1,
        2.2,  2.3,  2.4,  2.5,  2.6,  2.7,  2.8,  2.9,  3. ,  3.1])

import numpy as np
x2 = np.linspace(0 , 3.14, 100) #Get values between 0 and 3.14 by dividing the range into 100 results

>>>x2
array([ 0.        ,  0.03171717,  0.06343434,  0.09515152,  0.12686869,
        0.15858586,  0.19030303,  0.2220202 ,  0.25373737,  0.28545455,
        0.31717172,  0.34888889,  0.38060606,  0.41232323,  0.4440404 ,
        0.47575758,  0.50747475,  0.53919192,  0.57090909,  0.60262626,
        0.63434343,  0.66606061,  0.69777778,  0.72949495,  0.76121212,
        0.79292929,  0.82464646,  0.85636364,  0.88808081,  0.91979798,
        0.95151515,  0.98323232,  1.01494949,  1.04666667,  1.07838384,
        1.11010101,  1.14181818,  1.17353535,  1.20525253,  1.2369697 ,
        1.26868687,  1.30040404,  1.33212121,  1.36383838,  1.39555556,
        1.42727273,  1.4589899 ,  1.49070707,  1.52242424,  1.55414141,
        1.58585859,  1.61757576,  1.64929293,  1.6810101 ,  1.71272727,
        1.74444444,  1.77616162,  1.80787879,  1.83959596,  1.87131313,
        1.9030303 ,  1.93474747,  1.96646465,  1.99818182,  2.02989899,
        2.06161616,  2.09333333,  2.12505051,  2.15676768,  2.18848485,
        2.22020202,  2.25191919,  2.28363636,  2.31535354,  2.34707071,
        2.37878788,  2.41050505,  2.44222222,  2.47393939,  2.50565657,
        2.53737374,  2.56909091,  2.60080808,  2.63252525,  2.66424242,
        2.6959596 ,  2.72767677,  2.75939394,  2.79111111,  2.82282828,
        2.85454545,  2.88626263,  2.9179798 ,  2.94969697,  2.98141414,
        3.01313131,  3.04484848,  3.07656566,  3.10828283,  3.14      ])


#Plotting cos(x)
import numpy as np
import matplotlib.pyplot as plt
from math import cos

x = np.arange(0, 3.14, 0.1)
y = np.cos(x) #Do not have to write y = [cos(i) for i in x]

plt.plot(x, y)
plt.show()

#More curves
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin

x = np.arange(0,3.14, 0.1) #0 to pi difference by 0.1 interval
y1 = np.cos(x) 
y2 = np.sin(x)

plt.plot(x, y1, '-g', label = 'cosine') #green colour
plt.plot(x, y2, '-b', label = 'sine') #blue colour

plt.legend(loc = "upper right") #legend location
plt.title('Sine and Cosine Curves') #graph title
plt.ylim(-1.5, 1.5) #set y axis limit
plt.show()

#Plot 2 seperate curve in 1 window
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin

x = np.arange(0,3.14, 0.1) #0 to pi divided by 0.1 interval
y1 = np.cos(x) 
y2 = np.sin(x)

plt.subplot(2,1,1) #(no. of row, no. of column, position 1 count from left to right)
plt.plot(x, y1, 'xg', label = 'cosine') #green colour
plt.title('Cosine Curves')

plt.subplot(2,1,2) #(no. of row, no. of column, position 2 count from left to right)
plt.plot(x, y2, 'ob', label = 'sine') #blue colour
plt.title('Sine Curves') #graph title

plt.show() 

#Split into 2 graph into 2 window
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin

x = np.arange(0,3.14, 0.1) #0 to pi divided by 0.1 interval
y1 = np.cos(x) 
y2 = np.sin(x)

plt.figure(1) #figure 1
plt.subplot(2,1,1) #(no. of row, no. of column, position 1 count from left to right)
plt.plot(x, y1, 'xg', label = 'cosine') #green colour
plt.title('Cosine Curves')

plt.figure(2) #figure 2
plt.subplot(2,1,2) #(no. of row, no. of column, position 2 count from left to right)
plt.plot(x, y2, 'ob', label = 'sine') #blue colour
plt.title('Sine Curves') #graph title

plt.show() 

#Bar chart
#plt.bar(x,y) vertical bar chart
#plt.barh(x,y) horizontal bar chart

#Histogram
#a_list = []
#plt.hist(a_list,no. of bins)

#Pie chart
import matplotlib.pyplot as plt
labels = ['Python', 'Java', 'C']
size = [22, 23, 50]

plt.pie(size, startangle=90, shadow = True) #the sequence does not matter
plt.legend(labels, loc='best')

plt.axis('equal')
plt.title('Programming Language')
plt.show()

#Saving a graph
#fig.savefig('plot.png')
#for.savefig('plot.pdf') 

#Create an array that is like a list
import numpy as np
a = np.array([1,2,3]) #array([1, 2, 3])
a[0] = 999 #array([999,   2,   3])
print(type(a)) #numpy.ndarray 

#Array broadcasting
import numpy as np
a = np.array([1,2,3])
#>>>a+1
#array([2,3,4])
#>>>a*3
#array([3,6,9])
#>>>a<3
#array([True,True,False)

#Array Math
import numpy as np
v1 = np.array([1,2,3])
v2 = np.array([4,9,16])
print(v1+v2) #array([5,11,19])
print(v1*v2) #array([4,18,48])
print(v2.sum()) #29 

#Locating an entry
import numpy as np
c = np.zeros((3,5)) #3 rows and 5 columns with zeros in every box
c[1][4] = 999 #row 1 and column 4 has a value of 999 now
c[2,4] = 999 #row 2 and column 4 has a value of 999 now
'''
#Sub-array
import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[1:3,2:4]) #[row range, column range]
#[[ 7  8]
#[11 12]]

print(a[0:2,2:])
#[[3 4]
#[7 8]]

print(a[:,::2])
#[[ 1  3]
#[ 5  7]
#[ 9 11]] 

#Matrix multiplication
import numpy as np
m1 = np.array([[2,1],[3,10]])
m2 = np.array([[4,0],[0,3]])

print(np.matmul(m1,m2))
#[[ 8  3]
#[12 30]]

#Boolean Array Indexing
import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
bool_idx = a > 5
print(bool_idx)
#[[False False False False]
#[False  True  True  True]
#[ True  True  True  True]]

print(a[bool_idx])
#[ 6  7  8  9 10 11 12]

print(a[a>10])
# [11 12]

#Reading csv file
import csv
import numpy as np
import matplotlib.pyplot as plt
#birth_file = open('crudebirthrate.csv')
#birth_file_reader = csv.reader(birth_file)
#data_list = list(birth_file_reader)

#Plot graph using csv file and numpy array
def plot_birth_rate():
    birth_file = open('crudebirthrate.csv') #open csv file
    birth_file_reader = csv.reader(birth_file) #read csv file in csv mode
    data_list = np.array(list(birth_file_reader)) #make the excel spread sheet into an array
    birth_year = data_list[1:,0] #Remove first row. Take the first column
    birth_rate = data_list[1:,2] #Remove first row. Take the last column
    plt.plot(birth_year,birth_rate) #Plot graph
    plt.show() #Show the graph on screen

******************************************************************************

#Lecture 10
#Looping through a 1D array
import numpy as np
data = np.array([1,2,3,4,5,6])
for i in data:
    print(i)
#1
#2
#3
#4
#5
#6

#Lopping through a 2D array
data2 = np.array([[1,2,3],[4,5,6]])
for i in data2:
    print(i)
#[1 2 3]
#[4 5 6]

for i in range(2):
    for j in range(3):
        print(data2[i][j]) #data2[row][column]. It cannot be data2[column][row]
#1
#2
#3
#4
#5
#6
for j in range(data2.shape[0]): #shape[0] is number of row
    for i in range(data2.shape[1]): #shape[1] is number of column.  #data2.shape gives (2,3) (no. of rows, no. of columns) 


        print(data2[j][i]) #data2[row][column]. for j....: (row) for i.....: column must be in this sequence
#1
#2
#3
#4
#5
#6

#Load an image
from scipy import misc, ndimage
import matplotlib.pyplot as plt

cat_pic = misc.imread('cute cat.jpg') #read the file

plt.imshow(cat_pic) #plot on the graph
plt.show() #show on the screen


#>>> type(cat_pic)
#<class 'numpy.ndarray'>

#>>> cat_pic.shape
#(600, 600, 3) (row, column, RGB) 
#0 <= R,G,B <=255

cat_pic2 = cat_pic[150:400, 150:400, :] #restricting the row and column
plt.imshow(cat_pic2)
plt.show()

#Rotating an image
rotate_cat = ndimage.rotate(cat_pic, -45) #45 degree is anti-clockwise rotation -45 degree is clockwise rotation

plt.imshow(rotate_cat)
plt.show()

rotate_cat_noreshape = ndimage.rotate(cat_pic, 45, reshape= False) #No reshape. Picture just rotate, with some parts not seen
plt.imshow(rotate_cat_noreshape)
plt.show()

#Broadcasting
cat_pic3 = cat_pic * [0, 1, 0] #[R G B] [R x 0, G x 1, B x 0]  
plt.imshow(cat_pic3)
plt.show()

#Negative image 
cat_negative = 255 - cat_pic
plt.imshow(cat_negative)
plt.show()

'''









    








        























        













