#Store following word meanings in python dict:
"""dictionary = {
    "cat" : "a small animal",
    "table" : ("a piece of furiture" , "list of facts and figures")

}
print(dictionary)"""

#you are given a list of subj for students . Assume one classroom is required for 1 subject . how many classrooms are needed by all students
set ={"java" , "python" , "C++","python" ,"JS" , "java" , "python",
      "java" , "C++" , "C"}
print(len(set))

#WAP to enter marks of  3 subjects from user and store them in dictionary
#start with an empty dictionary & add one by one. use subject name as key &marks as value
"""dict = {}
x = int(input("enter phy marks : "))
dict.update({"physics" :x })

x = int(input("enter chemistry marks : "))
dict.update({"chemistry" :x} )

x = int(input("enter math marks : "))
dict.update({"math" :x })
print(dict)"""


#WAP to store 9 and 9.0 in set
#method 1
"""values = {9,"9.0"}
print(values)"""
#method 2 --> usage of pairs of tuples
values = {
("float" , 9.0),
("int" , 9)
}
print(values)