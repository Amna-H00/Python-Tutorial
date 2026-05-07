#File I/O in python :
#python can perform operations on file like read and write

#Types of files:
#--> Text files : .txt , .docx , .log
#--> Binary file : .mp4 , .mov , .Jpeg , .png

#Open , read & close file:
#f = open("file_name" ,"mode"(read,write))
#data = f.read()
#f.close()

"""f = open("demo.txt" , "r")
data = f.read(7)
data = f.readline()
print(data)

print(type(data))
f.close()"""
#read file:
#data = f.read() #read entire file
#data = f.readline() --> reads a line


#Writing to a file :

#f = open("demo.txt" , "w"/"a") --> "w" = overwrite data , "a" = append data at the end
#f.write("this is a new line") 

"""f = open("demo.txt" , "w")
f.write("you shutup looser")
f.close()""" #overwrites all data

"""f = open("demo.txt" ,"a")
f.write ("\n shhhh dont be shy babie \n you silly ")
f.close()""" #appends at the end data

"""f = open("sample.txt" , "a")
f.open()""" #makes file

#r+ -->(no truncates) cursor at the beining and overwrites value from the starting
"""f = open("demo.txt" , "r+")
f.write("chararainrain")
f.close()"""

#w+ --> read +overwrite (truncates)
"""f = open("demo.txt", "w+")
f.write("shhh bc")
f.close()"""

#a+ --> read and append pointer atthe end (no truncates)
"""f = open ("demo.txt" , "a+")
f.write("\n hey me")
f.close()"""

#with Syntax :  as --> alias
"""with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)"""
#with syntax w.r.t "w":
"""with open("demo.txt" , "w") as f :
    f.write("new data")"""

#Deleting a file: using os module 
#Module --> (code library)is file written by another programmer that generally has a func that we can use!

"""import os 
os.remove("demo.txt")""" #deletes file

#Lets practise :
#create a new file "practise.txt" using python . Add the following data in it:
"""f = open("practise.txt", "w")
f.write("Hi everyone \n we are learning File I/O " \
"\n using java. \n I like \n programming in Java.")"""

#WAf that replaces all occurences of "java" with "python" in above file
"""def check_for_word():
    with open("practise.txt" , "r") as f :
     data = f.read()
    new_data = data.replace("Java" , "Python")
    print(new_data)

    with open ("practise.txt" , "w") as f :
        f.write(new_data)

check_for_word()
"""

#Search the word "learning" exists or not :
"""word = "learning"
with open ("practise.txt" , "r") as f :
     data = f.read()
     if(data.find(word) != -1  ):
          print("found")
     else:
          print("not found")"""

#WAF to find in which lone of file does the word "learning" occur first .
#print -1 if word not found

"""def check_for_line():
    word = "python"
    data = True
    line_no = 1
    with open ("practise.txt" , "r") as f :
        while data:
            data = f.readline()
            if(word in data) :
                print (line_no)
                line_no += 1
            else:
                print("-1")

print(check_for_line())
"""
#Form a file containing numbers seprrated by comma , print the cunt of evevn numbers
#count = 0
with open ("num_file" , "r") as f :
   data = f.read()
   print(data)

   nums = data.split(",")
   for val in nums :
      if(int(val)%2 == 0):
         print("even")
      else:
         print("odd")
         #count += 1

#print(count)



      

              











