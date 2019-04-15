# Author:           Brad W. Botteron
# Date Written:     4/12/19
# Script:           M12_Lab
# Description:      Instantiates a Person/Student and displays back to user

# import classes module
import classes

# Define Main()
def Main():
    # Try block for exception handling
    try:
        # While statments for GIGO
        firstName = input('Enter Students First Name: ')
        while firstName == '':
            print('Error: Cannot be blank')
            firstName = input('Enter Students First Name: ')
            
        lastName = input('Enter Students Last Name: ')
        while lastName == '':
            print('Error: Cannot be blank')
            lastName = input('Enter Students Last Name: ')
            
        addressInfo = input('Enter Students Address: ')
        while addressInfo == '':
            print('Error: Cannot be blank')
            addressInfo = input('Enter Students Address: ')
            
        print('Please use format \'xxx-xx-xxxx\'')
        phoneNumber = input('Enter Students Phone Number: ')
        while phoneNumber == '':
            print('Error: Cannot be blank')
            phoneNumber = input('Enter Students Phone Number: ')
            
        studentID = input('Enter Students ID Number: ')
        while studentID == '':
            print('Error: Cannot be blank')
            studentID = input('Enter Students ID Number: ')

        # While statement for ensuring credits between 1 and 16 (should 0 be included?)
        studentCreds = int(input('Enter Students Credits This Term: '))
        while studentCreds < 1 or studentCreds > 16:
            print('Error: Student Cannot have less than 1 credit or more than 16 credits per semester!')
            studentCreds = int(input('Enter Students Credits This Term: '))

        print('Enter Yes or No')
        inputEnroll = input('Is Student Enrolled Next Term? ')
        # While block to ensure user can only input certain values
        while inputEnroll not in ('Yes', 'No', 'yes', 'no'):
            print('Error: Yes and No input only')
            inputEnroll = input('Is Student Enrolled Next Term? ')
        # Evaulates and assigns boolean value based on user input
        if inputEnroll == 'Yes':
            studentEnroll = True
        elif inputEnroll == 'yes':
            studentEnroll = True
        elif inputEnroll == 'No':
            studentEnroll = False
        elif inputEnroll == 'no':
            studentEnroll = False
        # print header
        print()
        print('STUDENT INFORMATION')
        print('-------------------')
        # passes info to classes and getters/setters assigns values
        studentInfo = classes.Student(firstName, lastName, addressInfo, phoneNumber, studentID, studentCreds, studentEnroll)
        # calls DisplayInfo() to print information to screen
        classes.Student.displayInfo(firstName, lastName, addressInfo, phoneNumber, studentID, studentCreds, studentEnroll)
    # Catches non-integer numbers
    except ValueError:
        print('Error: Credits needs to be an Integer')
    # general exception
    except Exception as err:
        print('Error: ', err)
        


# Call Main()
Main()
