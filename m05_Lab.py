# Author:           Brad W. Botteron
# Date Written:     2/13/19
# Script:           M05 Lab
# Description:      Income Calculations

# Initialize Constants

CLASSA = 42
CLASSB = 27
CLASSC = 18
CLASSD = 12

# Define Main() program

def main():
    aSeat = int(input('Enter how many seats were sold for Class A : '))
    if (aSeat > 200):
        print('Error, there is not that many seats in the Coliseum Class A!')
        aSeat = int(input('Enter how many seats were sold for Class A : '))
    bSeat = int(input('Enter how many seats were sold for Class B : '))
    if (bSeat > 150):
        print('Error, there is not that many seats in the Coliseum Class B!')
        bSeat = int(input('Enter how many seats were sold for Class B : '))
    cSeat = int(input('Enter how many seats were sold for Class C : '))
    if (cSeat > 100):
        print('Error, there is not that many seats in the Coliseum Class C!')
        cSeat = int(input('Enter how many seats were sold for Class C : '))
    dSeat = int(input('Enter how many seats were sold for Class D : '))
    if (dSeat > 50):
        print('Error, there is not that many seats in the Coliseum Class D!')
        dSeat = int(input('Enter how many seats were sold for Class D : '))

    # Send user input variables to proper class with parameters
    calculateClassIncome(aSeat, bSeat, cSeat, dSeat)

# Define calculateClassIncome() program

def calculateClassIncome(aSeat, bSeat, cSeat, dSeat):
    aTotal = aSeat * CLASSA
    bTotal = bSeat * CLASSB
    cTotal = cSeat * CLASSC
    dTotal = dSeat * CLASSD

    # Send class totals to show method with proper parameters
    showTotalIncome(aTotal, bTotal, cTotal, dTotal)
    
# Define showTotalIncome() program

def showTotalIncome(aTotal, bTotal, cTotal, dTotal):
    totalIncome = aTotal + bTotal + cTotal + dTotal
    print('Your total for Class A seats is $', format(aTotal, '.2f'), sep='')
    print('Your total for Class B seats is $', format(bTotal, '.2f'), sep='')
    print('Your total for Class C seats is $', format(cTotal, '.2f'), sep='')
    print('Your total for Class D seats is $', format(dTotal, '.2f'), sep='')
    print('Your total income for the entire Coliseum is $', format(totalIncome, '.2f'), sep='')


main()

print('Thank you for calculating your income for each Class of seats and the total Coliseum!')
