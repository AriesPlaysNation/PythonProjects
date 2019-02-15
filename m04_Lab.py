# Author:           Brad W. Botteron
# Date Written:     2/5/19
# Script:           M04_Lab
# Description:      Organism Spawn Rate Per Day With Linear Growth

# Initialize constants
MAXINCREASE = 2.0
MAXDAYS = 90

# Initialize variables
maxDays = 0
startingOrgs = 0
dailyIncrease = 0
days = 1
totalOrgs = 0.0

# User Input for starting organisms and while loop to ensure a positive number
startingOrgs = int(input('How many organisms are you starting with on day 1? '))
while startingOrgs <= 0:
    print('I\'m sorry, but it isn\'t possible to start with a negative amount of organisms!')
    startingOrgs = int(input('How many organizms are you starting with on day 1? '))

# User input for daily increase and while loop to keep under 2.0
dailyIncrease = float(input('What is the average daily increase percentage? '))
while dailyIncrease > MAXINCREASE:
    print('An average daily increase of above 2.0 is unrealistic, try again')
    dailyIncrease = float(input('What is the average daily increase percentage? '))

# User Input for days the project is going on and while loop to no go above 90 days
maxDays = int(input('How many days would you like to watch your organisms? '))
while maxDays > MAXDAYS:
    print('I\'m sorry, but this is designed for the short term experiement!')
    maxDays = int(input('How many days would you like to watch your organisms? '))

# Print Report Header
print('Day\tApproximate Population')
print('------------------------------')

# Settings initial totalOrgs for first run.
totalOrgs = startingOrgs

# For loop for starting at user inputed days to max days plus 1 to include the last day.
for days in range(days, maxDays+1):
    print(days, '\t\t', format(totalOrgs, '2.6f'))
    totalOrgs = totalOrgs * dailyIncrease + totalOrgs
    days + 1
    

print('------------------------------')
