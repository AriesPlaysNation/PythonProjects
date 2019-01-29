# Author:           Brad W. Botteron
# Date Written:     1/28/19
# Script:           M03_Lab.py
# Description:      Calculating shipping cost per package weight


# Initializing variables
weight = 0

# Ask user how heavy their package is
weight = float(input('Enter how many pounds your package is: '))

# Calculate and Display the weight of the package
print('Your package weights ',format(weight, '.2F'))

# Calculate shipping cost and display back to user
if weight <= 0:
    print('I\'m sorry but this isn\'t possible! Please restart and enter a valid weight.')
elif weight <= 3:
    print('Your shipping cost will be $1.25')
elif weight <= 7:
    print('Your shipping cost will be $3.13')
elif weight <= 12:
    print('Your shipping cost will be $5.47')
else:
    print('Your shipping cost will be $8.20')

# Thank user for using the program
print('Thank you for using my shipping cost projector!')
