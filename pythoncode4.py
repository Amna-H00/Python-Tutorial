#Dictionary in python: --> used to store data values in pairs
#they are unordered , mutable(changeable) , dont allow duplicate keys
"""info = {
    "name" : "BAzil shah",
    "subjects" : ["python" , "C" , "C++"],#list
    "topics" : ("dic" , "set"), #tuple
    "is_adult" : True ,
    12 : 99.9  #key values can be a number
}"""
#print(info)
#print(info["topics"])  #can acess any point in dict
"""info["name"] = "Shadow girl"
print(info) #can change any point in dict
info["surname"] = "shah"
print(info)""" #can add any term in dict

"""null_dict = {}
null_dict["name"] = "estern"
print(null_dict)""" # we can create null dictionary

"""student = {
    "name" : "ninja girl" ,
    "subject" : {
        "phy" : 45,
        "maths" : 67,
        "urdu" :78
    }
    
} 
print (student["subject"]["urdu"])"""#nested dictionary
#methods in dict --> 
"""print(list(info.keys())) #returns all keys

print(list(info.values()))#return all values

pairs = (list(info.items())) #return all items(key,val) pairs as tuple
print(pairs[0])""" #print pairs

"""print(student["name2"])""" #error
"""print(student.get("name2"))""" #get name by these 2 methods

#.update() --> updates dictionary
"""new_dict = {"name": "BoynaGalava","city":"pakistan", "lang": "URDU" ,"age" : 21
}
student.update(new_dict)
print(student) """

#SET in python --> collecton of unordered pairs
#eah item is unique and)
#list & dict cant store in sets
#set ignores duplicate items
#set --> mutable
#set --> elements --> immutable
"""collection = {1,2,2,3,4 , "hello" ,"world" , "world"}
print(collection)
print(type(collection))
print(len(collection))"""

collection1 = set()#empty set
print(collection1)

#SET MEthods --
"""collection1.add(9)
collection1.add(4)
collection1.add("bazil")
collection1.add((18,8))""" #cant add list its unhashable but can add tuple
#collection1.remove(9)
#collection1.clear() #clears all values
"""print(collection1)""" #add element

#union and intersection in sets
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))








