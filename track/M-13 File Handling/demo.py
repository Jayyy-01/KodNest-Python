with open("demo.txt","r") as file:
    # print(file.read())      #reads entire file
    # print(file.readline())  #reads first line
    # print(file.readline())  #reads second line
    # print(file.readline())  #reads third line
    print(file.readlines()) #reads all lines as list of strings
    # file.close()  