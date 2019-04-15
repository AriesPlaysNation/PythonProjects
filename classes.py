# Author:           Brad W. Botteron
# Date Written:     4/12/19
# Script:           classes
# Description:      Creating classes for Person and Student

# Define Superclass
class Person:
    # __init__ for Person Information
    def __init__(self, first, last, address, number):
        self.__first = first
        self.__last = last
        self.__address = address
        self.__number = number

    # Getters for superclass
    def setFirst(self, first):
        self.__first = first

    def setLast(self, last):
        self.__last = last

    def setAddress(self, address):
        self.__address = address

    def setNumber(self, number):
        self.__number = number

    # Setters for superclass
    def getFirst(self):
        return self.__first

    def getLast(self):
        return self.__last

    def getAddress(self):
        return self.__address

    def getNumber(self):
        return self.__number

# Define SubClass
class Student(Person):
    
    # Define Superclass properties while adding subclass properties to it
    def __init__(self, first, last, address, number, ID, creds, enroll):
        Person.__init__(self, first, last, address, number)

        self.__ID = ID
        self.__creds = creds
        self.__enroll = enroll
        
    # Setters for subclass Properties
    def setID(self, ID):
        self.__ID = ID

    def setCreds(self, creds):
        self.__creds = creds

    def setEnroll(self, enroll):
        self.__enroll = enroll
        
    # Getters for subclass properties
    def getID(self):
        return self.__ID

    def getCreds(self):
        return self.__creds

    def getEnroll(self):
        return self.__enroll

    # DisplayInfo() passing arguements into function and printing output
    def displayInfo(firstN, lastN, add, num, sID, sCreds, stEnroll):
        print('First Name: ', firstN)
        print('Last Name: ', lastN)
        print('Address: ', add)
        print('Phone Number: ', num)
        print('Student ID: ', sID)
        print('Student Credits: ', sCreds)
        print('Student Enrolled: ', stEnroll)
