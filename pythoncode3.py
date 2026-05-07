#list in python : --> can store diff types
# (int, float,string)
#string --> immutable in python(cant changed)
#list --> mutable in python(changed)
"""marks = [94.4, 87.5, 78.3, 89.0]
print(marks )
print (type(marks))
print(marks[1])

student = ["bazil" , 95.4 , 19 , "delhi"]
print(student)
student[0] = "shah" 
print(student)"""#list

#list-slicing --> gives sublist
"""num = [45 ,34 ,56 ,88 ,90 ]
print(num[1:4])
print(num[-3:-1])
"""
#list methods :
list = [2,1,3,3]
"""list.append(4)  #adds element at the end  (called mutation --> cahnging in lists)
print(list)
list.sort()   # sorts in ascending order
print(list)
list.sort(reverse=True)  #descending order sorting
print(list)
list.reverse()   #reverses the list 
print(list)
list.insert(4,6) #insert element at the index
print(list)
"""
"""list.remove(1)
print (list)""" #removes the first occurence
"""list.pop(3)
print(list)""" #removes the index element


"""list = [ 2,5,9]
print(list.append(4))
print(list.sort(reverse=True))
print(list)

lis = ["banana" , "litchi" , "apple"]
print(lis.sort())
print(lis)""" #strings can sorted by alphabetic characters


"""str = "hello"
print(str[0])
str[0] = "y""" #gives err in str


#TUPLE ==> same as list , but we cant assign value nor can change
"""tup = (2,4,6,5)
print(type(tup))
tupl = (1)
print(type(tupl))""" #int

"""tu = ("String value in tupl",)
print(type(tu)) #tuple type
print(tu[1:3])"""

#tuple methods:
tup = (1,2,3,4,4,5,4,4)
print(tup.index(1)) #shows occurence
print(tup.count(4 ))

