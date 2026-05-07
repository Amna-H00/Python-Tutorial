# Strings & Conditionals Statements
str1 = 'casino'
str2 = """ cocubine"""
str3 = "narcissist"
# Escape sequence characters : provides formatting (tab , nextln)
# \n ---> moves characters on next line
str4 = "This is string. \n we are creating python."
# concatenation :
a = 'helo'
b = 'world'
print(a + " " + b)
# len(str):
print(len(str1))

# indexing : position number
str = "bazil shah"
print(str[0])
# slicing : accessing parts of str
print(str[3:])
print(str[6:10])
print(str[:6])
# negative slicing---> backward slicing
print(str[-9:-7])
print(str.endswith("ah"))  # returns end str
print(str.capitalize())  # capitalize 1st char
print(str.replace("a", "o"))  # replaces all old occurences
print(str.find("shah"))  # returns 1st index of number
print(str.find("q"))  # gives -1
print(str.count("a"))  # counts the value


# WAP to input users first name & print its length
name = input("Enter your name :")
print("length of ur name is :", len(name))

# WAP to find occurence of '$' in a string
str = "i hve 30$ of ysl heal + 100$+40$"
print(str.count('$'))

# conditional statements---> if-elif-else(syntax)
# we use indentation in python instead of curly braces{}
"""num = 1
if (num > 2):
    print("greater than 2")
elif (num > 3):
    print("greater than 3")
else:
    print("All false ")"""

 # WAP of grade of students
marks = int( input("enter marks of students = "))
if(marks >= 90 ):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"

print("grade of student : " , grade)

#nesting 
age = 95
if(age >= 18):
    if(age >= 80):
        print ("cant drive ")
    else:
        print("can drive")
else:
    print("out from drive") 
    
           
