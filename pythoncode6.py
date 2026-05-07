#functions in python --> block of statement t0 perform a specific task 
#function for sum:
"""def calc_sum(a,b):
    return a + b 
sum = calc_sum(1,2)
print(sum)"""
# function for *:
"""def mult_func(a,b): #parameters
    return a*b
mul = mult_func(5,8)#func call , arguments
print(mul)"""

#func average of 3 numbers
"""def av_rge(a,b,c):
    sum = a+b+c
    avg = sum /3
    print(avg)
    return avg

av_rge(1,2,2)  """

#Built in functions --> print(),len(),type(),range()
#user-defined functions --> 
"""def cal_prod(b,a=2):
    print(a*b)
    return(a*b)

cal_prod(2)"""

#WAP to print the lenght of  a list (list is the parameter)
"""list1 = ["d","j","k","l","t","g"]
list2 = ["1","2","3","4","5","6","7"]

def list_val(list):
    print(len(list))

list_val(list1)
list_val (list2)"""
#WAP to print elements of list ina single line .
"""list1 = ["d","j","k","l","t","g"]
def li_st(list):
    for item in list:
        print(item,end="")

li_st(list1)   """ 

#WAP to find factorial of n.

"""def fact_orial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)

fact_orial(4)"""

#convert USD to PAK 
"""def converter(usd_val):
    pak_val = usd_val
    pak_val = usd_val * 270
    print(usd_val , "USD =" , pak_val , "pak-val")

converter(100)   """

# Recursion --> version of loops --> when afunction calls
#two main things in python : (i): kaam 
#(ii): base case
"""def show (n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(3)"""

#recursive func for factorial(n):

"""def fact(n):
    if(n == 0 or n ==1):
        return 1
    return fact(n-1)*n

print(fact(4))"""

#write a func to print 1 to n numbers:

"""def num(n):
    #base case
    if(n==0):
        return 0
    #kaam
    return num(n-1)+n

print(num(7))"""

#Write a recusrion function to print all elements in alist
def num (list , idx=0):
    #base case
    if(idx == len(list)):
        return
    #kaam
    print(list(idx))
    num(list, idx +1)

gang = ["bail","bloody","shit"]

num(gang)


    
