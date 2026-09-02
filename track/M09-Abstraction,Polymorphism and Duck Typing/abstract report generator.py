from abc import ABC,abstractmethod
class ReportGenerator(ABC):     #creating abstract class and inherting from ABC(abstraction base class)
    @abstractmethod
    def generate_report(self):      #abstract method
        pass
    
class StudentReport(ReportGenerator):
    def __init__(self,name):       
        self.name = name
    def generate_report(self):      #overriding the abstract method
        print("Generating student report for {self.name}")

name = input()
report = StudentReport(name)
report.generate_report()

#summary : here i created abstract class ReportGenerator and i used it to create one object and display the object using print(report.generate_report())