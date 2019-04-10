# Author:           Brad Botteron
# Date Written:     3/29/19
# Script:           M10_Lab
# Description:      Counts how many times a sentance, word, and average is in text file.

# Define Main()

def main():

    # Initialize Variables

    noWords = 0
    noSent = 0
    average = 0.0

    # Try block to make sure file is there.
    try:
        # Open article.txt
    
        infile = open('m10_article.txt', 'r')

        # Read file into article
    
        article = infile.read()

        for ch in article:
            numWords = article.split()
            numSent = article.split('\n')

        noWords = len(numWords)
        noSent = len(numSent)

        infile.close

    except IOError:
        print('Cannot open file.')
    except Exception as err:
        print(err)
    else:

        # Calculate average words per line
    
        average = noWords / noSent
        
        print('The total number of words in this document is: ', noWords)
        print('The total number of sentences in this document is: ', noSent)
        print('The average number of words per line is: ', format(average, '.2f'))

main()
