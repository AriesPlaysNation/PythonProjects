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
            if ch.isspace():
                noWords += 1
            if ch.endswith('.'):
                noSent += 1

        infile.close

    except IOError:
        print('Cannot open file.')
    except Exception as err:
        print(err)
    else:
        # Have to -1 because of last sentence reading a false sentence count.
    
        noSent -= 1

        # Calculate average words per line
    
        average = noWords / noSent
        
        print('The total number of words in this document is: ', noWords)
        print('The total number of sentences in this document is: ', noSent)
        print('The average number of words per line is: ', format(average, '.2f'))

main()
