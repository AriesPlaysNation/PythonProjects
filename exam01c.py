#	Exam01 Problem C 

#	Author:         Brad W. Botteron
#	Date Written:	3/4/2019
#	Description:	Strange Payroll



# Declare variables

salary = 1.0
weeks = 0
days = 1

# Ask the user for how many weeks to calculate
try:
    weeks = int(input('Enter how many weeks you would like to calculate your salary: '))
    while (weeks < 1 or weeks > 15):
        print('Sorry you can only calculate your salary between 1 and 15 weeks!')
        weeks = int(input('Enter how many weeks you would like to calculate your salary: '))

    print('\nWeek\t\t\t     Dollars')
    print('------------------------------------')

    while (days <= weeks):
        print(days, '\t\t\t ', '$', format(salary, '8.2f'))
        salary = salary * 2
        days = days + 1
    print('------------------------------------')

        
except ValueError:
        print('Error: Only input a valid integer')
    


# 2r04p07 (keep this as the last line in the file)
