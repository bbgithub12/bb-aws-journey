# import requests

#create a class for students of GenUni
#the class should have attributes for the first and lastname of student
#the third attribute sould be for email which is concatenating
#first name, last name and @genuni.co.uk
#print the students first name, last name and email


class Student():
    def __init__(self, fname, lname, email):
        self.fname = "name"
        self.lname = "surname"
        self.email = "name"+"surname","@genuni.co.uk"
student1 = Student("Bola", "Buraimoh", "@genuni.co.uk")
student2 = Student("Funke", "Fosudo", "@genuni.co.uk")

print(student1.email)