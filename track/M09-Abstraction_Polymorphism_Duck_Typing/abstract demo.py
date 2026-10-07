from abc import ABC,abstractmethod     # importing abstract method and abstraction base class

class Developer(ABC):                   #creating abstract class and inherting from ABC(abstraction base class)
    @abstractmethod
    def work(self):
        pass                            #abstract method

class JavaDeveloper(Developer):         #creating subclass JavaDeveloper and inherting from Developer class
    def work(self):                 #overriding the abstract method
        print("working on java")
        
class PythonDeveloper(Developer):         #creating subclass PythonDeveloper and inherting from Developer class
    def work(self):                 #overriding the abstract method
        print("working on python")


dev1 = JavaDeveloper()     #creating object
dev1.work()                  #calling the work method

dev2 = PythonDeveloper()        #creating object
dev2.work()                   #calling the work method  

#summary: here i created abstract class Developer and i used it to create two objects dev1 and dev2 and i called the work method for each object 