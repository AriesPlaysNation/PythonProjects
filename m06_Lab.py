# Author:           Brad Botteron
# Date Written:     2/21/19
# Description:      M06_Lab

# Define main()

def main():
    # Initialize variables
    total = 0.0
    number = 0.0
    counter = 0

    try:
        # Open file
        infile = open('numbers.txt', 'r')

        # Reads file per line and adds 1 to each total and figures average of numbers.    
        for line in infile:
            counter = counter + 1
            number = float(line)
            total += number

        

    except IOError:
        print('File name numbers.txt could not be opened for reading.')

    except ValueError:
        print('Cannot convert characters to numeric value.')

    except ZeroDivisionError:
        print('The file is empty.')

    except:
        print('Error: See IT.')

    else:

        # Close File
        infile.close()
        
        # Calculate average
        average = total / counter
        
        # Print average
        print('Average: ', average)

        print('Processing complete. No errors detected.')

# Call the main function.
main()
