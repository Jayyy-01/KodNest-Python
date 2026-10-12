file = open("write.txt", "w")
#write mode
file.write("this file has been written using python\n")
file.write("Python is high level programming language\n")
file.write("Python has simple syntax\n")


#append mode
file = open("write.txt", "a")
file.write("Python is easy to learn\n")
file.write("Thankyou !!!")
file.close()
 