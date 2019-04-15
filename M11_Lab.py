# Author:           Brad W. Botteron
# Date Written:     4/1/19
# Script:           M11_Lab
# Description:      Student Main()

# Import student class
import stu

# Main()
def Main():
    student1 = stu.Student('Sandra', 'Markle', 'C099847', 'SDEV', 'AS')
    student2 = stu.Student('John', 'Rogers', 'C091939', 'CSCI', 'AS')
    student3 = stu.Student('Roger', 'Jones', 'C047718', 'SDEV', 'AAS')

    student1.displayInfo()
    student2.displayInfo()
    student3.displayInfo()


   
Main()
