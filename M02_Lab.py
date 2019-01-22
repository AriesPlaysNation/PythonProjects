# Author: Brad W. Botteron
# Date Written: 1/29/19
# Script: M02_Lab.py
# Description: Gets user input from various items bought and displays,
# sales tax, avg item price, subtotal of items, and amount of sales tax

# Assigns Sales Tax
# Math for sales tax (total * (tax/100))
SALES_TAX = .085
SALES_TAX_DISPLAY = '8.5%'

# Gets user input for items
# DON'T FORGET TO FORMAT!!
item1 = float(input('What is the price of the first item? '))
item2 = float(input('What is the price of the second item? '))
item3 = float(input('What is the price of the third item? '))
item4 = float(input('What is the price of the fourth item? '))
item5 = float(input('What is the price of the fifth item? '))
item6 = float(input('What is the price of the sixth item? '))

# Finds average of all items
avg = (item1 + item2 + item3 + item4 + item5 + item6) / 6

# Finds the subtotal of all items
subTotal = (item1 + item2 + item3 + item4 + item5 + item6)

# Finds the total amount of sales tax
salesTax = (item1 + item2 + item3 + item4 + item5 + item6) * SALES_TAX

# Can't remember how to add a normal $ sign without space xD

# Displays SALES_TAX
print('The sales tax for you community is:', SALES_TAX_DISPLAY)

# Displays average amount of all items
print('The average of all your items is', format(avg, '.2f'), sep=' $')

# Displays the subtotal of all items before sales tax is applied
print('The subtotal amount of all your items is', format(subTotal, '.2f'), sep=' $')

# Displays the total sales tax for your order
print('The total sales tax for your order is', format(salesTax, '.2f'), sep=' $')

# Displays the subtotal of all items after sales tax is applied
print('The subotal amount of all your items, including sales tax, is', format(subTotal + salesTax, '.2f'), sep=' $')


