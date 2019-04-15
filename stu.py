# Author:           Brad W. Botteron
# Date Written:     4/1/19
# Script:           stu
# Description:      Student Class Definition

# Worker Class
class Student:
    # Assign Student1 info
    def __init__(self, firstName, lastName, studentID, major, degree):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__studentID = studentID
        self.__major = major
        self.__degree = degree        

    # Returns info back to main
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def setMajor(self, major):
        self.__major = major

    def setDegree(self, degree):
        self.__degree = degree
    
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getStudentID(self):
        return self.__studentID

    def getMajor(self):
        return self.__major

    def getDegree(self):
        return self.__degree

    def displayInfo(self):
        print('First Name: ', self.__firstName)
        print('Last Name: ', self.__lastName)
        print('Student ID: ', self.__studentID)
        print('Major: ', self.__major)
        print('Degree: ', self.__degree)
        print('---------------')
