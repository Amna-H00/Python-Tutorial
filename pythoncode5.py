# LOOP --> used to repeat instructions
# while loop:
"""count = 1
while count <= 5 :
    print("bazil")
    count += 1

print(count)"""

# print num 1-5
"""i = 5
while i >= 1 :
    print(i)
    i -= 1"""
# WAP to print 1-100
"""i = 1
while i <= 100 :
    print(i)
    i += 1"""
 # WAP to print from 100-1
"""
i = 100
while i >= 1:
    print(i)
    i -= 1
"""

# WAp to print multiplication table of a numver n
"""i = 1
while i <= 10:
    print (3*i)
    i += 1"""

# WAP to print the elements of the following list
# using loop
"""num = [ 1,4,9,16,25,36,49,64,81,100]

i = 0
while i < len(num) :
    print (num[i])
    i += 1"""
# traverse:
"""heros = [ "bazil" , "muscles girl" , "ninja girl", "cyber agency"]
i = 0
while i < len(heros):
    print(heros[i])
    i += 1"""

# WAP to search a number x in the tuple :
"""nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUNDED :" , i)
        break
    else:
        print("Finding....")
    i += 1"""

# Break & continue in loop
"""i = 1
while i<= 5:
    print(i)
    if (i == 3) :
        break #termintes loop
    i += 1
print("end of loop")"""

# continue
"""i = 0
while i<= 10:
#if(i%2 != 0):
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1"""

# loops are used for sequential traversal --> travel of loop in sequence i.e. list , tuple, string
"""nums = ["potato" , "brijat" , "ladyfinger" , "cucumber"]
for val in nums:
    print (val)"""  # list traverse

"""tup = (1,2,3,4,5,6,7,8,9,10)
for val in tup :
    print (val)"""  # tuple traverse

"""str = "bazil shah"
for char in str :
    print(char)"""  # string traverse

# else case in traverse loop:
"""str = " bazil shah"

for char in str:
    if(char == 'i'):
        print("i found")
        break
    print(char)
else:
    print("ENd")    """

 # practise questions:
 # print the elemnents of following by using a loop :
"""ele = [1,4,9,16,25,36,49,64,81,100]
for el in ele:
    print(el)"""

   # search for a number x in this tuple using loop
   # linear search
"""nums =  [1,4,9,16,25,36,49,64,81,100]
x = 25

indx = 0
for el in nums :
    if (el == x):
        print("number found at indx:", indx)
        break
    else :
        print("finding ...")
    indx += 1"""

# Range --> returns sequence numbers , starting from zero by default and increased by 1 by default

"""seq = range(10)  #range (stop)

for i in seq:
    print(i)"""


"""seq = range(2,10)  #range (start , stop)

for i in seq:
    print(i)"""


"""seq = range(2,10,2)  #range (start , stop, step size)

for i in seq:
    print(i)#prints even number"""

"""for i in range(1,100,2):
    print(i)  """  # prints odd number

# WAP to print numbers from 1 to 100
"""for i in range(0,101):
    print(i)"""

# WAP to print numbers from 100 to 1
"""for i in range(100,0,-1):
    print (i)"""

# WAP to print multiplication of number n
"""n = int(input("enter a number:"))

for i in range(1,11):
    print(n * i)"""

# PASS statement --> null statement .. does nothing
"""for i in range(5):
    pass #empty

print("useful work")"""

# WAP to find sum of first natural numbers (using while)
# by use of for loop
"""n = 6

sum = 0
for i in range(1, n+1):
    sum += i

    print("total sum :" , sum )"""
# byuse if while loop
"""n=6
sum = 0
count = 1
while count <= n :
  sum += count
count += 1

print ("total sum :" , sum)"""

# WAP to calculate factorial

"""n = 3
fact = 1
count = 1
while count <= n:
    fact *= count
    count += 1

    print("total factorial:" , fact)"""

# extra pracrise on loops
# Write a program to print the first 10 natural numbers using a while loop.

"""n=0
while n <= 10:
    print (n)
    n+=1"""
# Display numbers from -10 to -1 using a for loop.
"""i=1
for i in range(-10,0) :
    print(i)"""
# Accept a number from the user and print its multiplication table up to 10

"""user = int(input("enter number:"))

i = 0
while i <= 10:
    print(i*5)
    i+=1"""

# Calculate the sum of all numbers from 1 to a given number
"""user = int(input("enter numb:"))
sum = 1
n = 1
for i in range(5):
    sum += n
    n += 1
    print ("total * : " , sum)"""

# factorial of a given number
"""n = 4
fact = 1
count = 1
while count <= n :
    fact*= count
    count += 1

    print ("factorial :" , fact) """


# Write a program to count the total number of digits in an integer using a while loop.
"""i=0
n = [1,2,3,4,7]

while i <= len(n):
  if(i<= len(n)):
   print (len(n))
  i+=1"""

 # Iterate from 1 to 50; print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.
"""i = 50
for i in range(1,50):
  if(i%5 == 0 and i%3==0):
    print("fizzbuzz")
  elif(i%5 ==0):
    print("fizz")
  elif(i%3==0):
    print("buzz")
  else:
    print("none")"""

# Print all numbers from 0 to 6 except 3 and 6 using the continue statement.

"""for i in range(7):
    if (i ==3 or i== 6):
        continue
    print(i)"""
# Write a program to check if a given number is prime.
"""i = 3
if (i % 2 != 0):
        print("prime")
else:
        print("end")"""




