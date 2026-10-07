from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
        pass


class StudentReport(ReportGenerator):
    def generate_report(self):
        return "Generating Student Report"


class PlacementReport(ReportGenerator):
    def generate_report(self):
        return "Generating Placement Report"


class AttendanceReport(ReportGenerator):
    def generate_report(self):
        return "Generating Attendance Report"


def create_report(report_type):
    if report_type == 'STUDENT'.lower():        #checking report_type and creating object if it is equal to STUDENT
        return StudentReport()          #returning object of StudentReport class
    if report_type == 'PLACEMENT'.lower():      #checking report_type and creating object if it is equal to PLACEMENT
        return PlacementReport()        #returning object of PlacementReport class
    return AttendanceReport()         #returning object of AttendanceReport class


n = int(input())        #taking the input from the user
reports = []

for _ in range(n):         #taking the input from the user
    report_type = input().strip()           #taking the input from the user and creating obj
    reports.append(create_report(report_type))      

for report in reports:      #printing the object
    print(report.generate_report())

#summary : here i created abstract class ReportGenerator and i used it to create one object and display the object using print(report.generate_report()) 