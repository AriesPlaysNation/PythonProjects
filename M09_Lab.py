# Author:           Brad W. Botteron
# Date Written:     3/24/19
# Script:           M09_Lab
# Description:      Counts how many times a team (that the user enters) has won the superbowl

# Define main()
def main():

    # Initialize variables/constants
    
    teamCount = 0

    try:
        # Open SuperBowlWinners.txt
        infile = open('SuperBowlWinners.txt', 'r')
        # Assigns the file "content" to teams
        teams = infile.readlines()

        # Close file
        infile.close

        # While statement to strip new lines and assigns content of file/teams to a list
        i = 0
        while i < len(teams):
            teams[i] = teams[i].rstrip('\n')
            i += 1

        # print statement to test and make sure it's working
        # print(teams, i)

        userTeam = str(input('Enter the team you would like to search for: '))
        
    except IOError:
        print('File not found')
    except ValueError:
        print('Please enter a valid Football Team')
    except Exception as err:
        print(err)
    else:
        for winners in teams:
            if winners == userTeam:
                teamCount += 1
        print('The team', userTeam, 'won the SuperBowl', teamCount, 'times!')
        
main()
