# # Importing required libraries
# from tabulate import tabulate
from operator import attrgetter

#========The beginning of the class==========
# This is the shoe class, storing information about shoes in stock
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    # Method to update the quantity in the re_stock() function later on in this program
    def upd_quantity(self):
        self.quantity = self.quantity + 50
        return self.quantity

    def __str__(self):
        return f'''
        ** Nike {self.product} **
        Made in:\t {self.country}
        Product code:\t {self.code}
        Price:\t\t {self.cost}
        In stock:\t {self.quantity}\n'''

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
# This function reads file data, creates class objects, appends those to shoe list
def read_shoes_data():

    # Opening and reading the text file
    # Try-except used in case the file would not be found
    try: 
        with open('inventory.txt', 'r') as f:
            for shoe in f:
                if shoe.startswith('Country'):
                    pass # Skipping the first line
                else:
                    shoe_info = shoe.strip().split(',')
                    shoe_list.append(Shoe(shoe_info[0],shoe_info[1], shoe_info[2], float(shoe_info[3]), int(shoe_info[4])))
    
    except Exception:
        print("Error! File 'inventory.txt' was not found.")

    return shoe_list

def capture_shoes():

    # Asking user for input to capture shoe data
    country = input("\nType production country: ")
    code = input('Type model code: SKU')
    product = input('Type model name: ')

    # Making sure that cost & quantity are numbers
    while True:
        try: 
            cost = float(input('Type cost: '))
            break
        except Exception:
            print('Please enter a number for the cost.')

    while True:
        try: 
            quantity = int(input('Type in-stock quantity: '))
            break
        except Exception:
            print('Please enter a number for the quantity.')

    # Creating a new Shoe object and appending to the shoe list
    shoe_list.append(Shoe(country, 'SKU'+code, product, cost, quantity))
    print('\nThe product was added to the inventory!')

    return shoe_list

# This function prints out all the available shoes' information
def view_all():
    print()
    for shoe in shoe_list:
        print(shoe)

# This function finds the item with the lowest quantity
# It asks the user if they wish to restock it and restocks if desired
def re_stock():

    # Finding the min quantity by using min() and attrgetter() from the operatpr module
    # https://docs.python.org/3/library/operator.html#operator.attrgetter 
    min_quantity = min(shoe_list,key=attrgetter('quantity'))
    print('\nThe following product has the lowest stock:')
    print(min_quantity)

    # Updating the stock upon request
    choice = input('Increase stock by 50? (Y or N): ')
    if choice[0].lower() == 'y':
        min_quantity.upd_quantity()
        print(min_quantity)
    
    else:
        print('\tNo change was applied.')

        # Writing the changes to the file
        with open('inventory.txt', 'w') as f:
            f.write('Country,Code,Product,Cost,Quantity\n')
            for shoe in shoe_list:
                f.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n')
                
# This function searches for the object in the object list by the product code
def search_shoe():
    search = input('\nEnter the product code: ')
    for shoe in shoe_list:
        if search == shoe.code:
            print(shoe)
        
    if search not in shoe_list:
        print('\nWrong code. Please try again.')

# This function calculates the total value for each item
def value_per_item():
    print()
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f'Nike {shoe.product} value: {value}')


# This function determines the product with highest quantity
# Print this shoe as being for sale
def highest_qty():
    max_quantity = max(shoe_list,key=attrgetter('quantity'))
    print('\nThis product is for sale:')
    print(max_quantity)
    pass

read_shoes_data()
highest_qty()

#==========Inventory Tracking & Menu=============

while True:
    read_shoes_data()

    menu = input('''\nSelect one of the following options below:
    l - Load the inventory information onto the program
    a - Add a new product to the inventory
    va - View all the current products in the inventory
    r - Restock the product of lowest quantity (add 50)
    s - Search a specific product using its code (SKU)
    v - Find the inventory value (cost*quantity) for every product
    p - Put the product of the highest quantity for sale
    q - Quit
    : ''').lower()

    if menu[0].lower() == 'l':
        read_shoes_data()
        print('\nThe inventory list has been updated with the latest information!')

    elif menu[0].lower() == 'a':
        capture_shoes()

    elif menu[0].lower() == 'va':
        view_all()

    elif menu[0].lower() == 'r':
        re_stock()

    elif menu[0].lower() == 's':
        search_shoe()

    elif menu[0].lower() == 'v':
        value_per_item()

    elif menu[0].lower() == 'p':
        highest_qty()

    elif menu[0].lower() == 'q':
        print('\nGoodbye!')
        break

    else:
        print('\nYou have made a wrong choice. Please try again.')