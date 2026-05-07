#OOP in python:
#to map with real world scenarios , we started using objects in code
# this is called OOP 
#due to functions --> redundancy decreases, reuseability increases
#we moved from procedural programaming --> functional --> OOP

#Class and Object in Python :
#class is a blue print for creating object
#Object is also called instances

"""class Student :
    name = "Bazil" #clss

s1 = Student()
print(s1.name)""" #object


"""class Car :
    color = "blue"
    brand = "mercedes" #class

car1 = Car()
print(car1.color)
print(car1.brand)""" #obj

#_ _init_ _() Function --> is a constructor when object invokes(executes) there automatically exists init func


"""class Student:
     college_name = "ABC college"  #class attribute

    #default constructor
      def __init__(self):
         pass 
         
    #parametrized constructor:
     def  __init__(self , name , marks):
         self.name = name  #object attr
         self.marks = marks 

     def welcome(self):
        print("welcome students" , self.name)

     def get_marks(self):
         print(self.marks)

s1 = Student("BAzil" , 98) #object
s1.welcome() 
print(s1.get_marks())
"""

#Create student class that takes name nd marks & marks of 3 subj as arguments in constructor then create 
#a method to print avrg

"""class Student():
    def __init__(self , name , marks):
      self.name = name
      self.marks = marks

    def get_avrg(self):
       sum = 0
       for val in self.marks:
          sum += val
       print("Shh" , self.name  "your avrg score is :" , sum/3)

s1 = Student("Hey Bazil" , [56,89,99])
s1.get_avrg()

s1.name = "tonny"
s1.get_avrg()"""

#Static method: that dont use self parameters (works at class level) 
#we use decorators in this --> and they allow to wrap up a func

class Student() :
    def hello():
        print("hello")


s1 = Student()
s1.hello()