# WAP to ask user to enter names of 3 favorite movies and store them in list
"""movies = []
m1 = input("Enter ur first movie name:")
m2 = input("Enter ur sec movie name:")
m3 = input("Enter ur third movie name:")
movies.append(m1)
movies.append(m2)
movies.append(m3)

print(movies)"""
#2nd method:
"""movies = []
movies.append(input("enter ur first movie name:"))
movies.append(input("enter ur second movie name:"))
movies.append(input("enter ur third movie name:"))
print(movies)"""

#WAP to check if a list contains a palindrome of elements .
#palindrome means that hve same pronounciation as forward and backward

"""list1 = [1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1 ):
    print("its a palindrome")
else:
    print("not a palindrome")""" # output: this is a [palindrome]

"""list2 = [1,2,3]
copy = list2.copy()
copy.reverse()
if(copy == list2):
    print("palindrome")
else:
    print("not a palindrome")""" #not a palindrome

""" li = ["ama"]
    copy = li.copy()
    copy.reverse()
    if(copy == li):
        print ("a pal") #palindrome
    else:
        print("not a pal")


"""


#WAP to count& sort the number of students with Grade 'A' in the following tuple:
tuple = ["C" , "D" , "A" , 'A' , 'B' , 'A']
print(tuple.count('A'))
tuple.sort()
print(tuple)