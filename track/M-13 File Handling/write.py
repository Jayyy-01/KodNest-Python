file = open("write.txt", "w")   #creates a file and overwrites the existing content of the file
#write mode
file.write("this file has been written using python\n")
file.write("Python is high level programming language\n")
file.write("Python has simple syntax\n")


#append mode
file = open("write.txt", "a")  #adds content to the existing content of the file
file.write("Python is easy to learn\n")
file.write("Thankyou !!!")
file.close()
 
#create mode
with open("create.txt", "x") as file:       #here the file is created using "x" and the content is added to the file in the below line, if the file already exists it will raise an FileExistsError
    file.write("Welcome to file handling.")
    