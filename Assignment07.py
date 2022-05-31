# ------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Script to show how pickling and error handling works
# ChangeLog (Who,When,What):
# SOrellana,05/30/2022,Created script
# ------------------------------------------------------------------- #

# Declare Variables ------------------------------------------------ #

strMenuChoice = ''  # menu choice
strItem = ''  # grocery item
fltPrice = 0.0  # price of the item
lstItem = []  # list of items
lstGroceries = []  # Grocery list
fileName = 'GroceryList.dat'

# Processing ------------------------------------------------------- #
def add_item(item, price, list):
    """ Adds Data to the list

    :param item: (string) of item name
    :param price: (float) of items price
    :param list: (list) of groceries
    :return: list of rows
    """
    row = [item, price]
    list.append(row)

    return list

def save_file(file_name, list):
    """ Saves Grocery List into a binary file

    :param file_name: (string) of file name
    :param list: (list) of data to save
    :return: string
    """
    import pickle  # imports pickle module

    with open(file_name, 'wb') as file:  # automatically closes file when done
        pickle.dump(list, file)  # pickling data to a file

    return 'Data was saved!'

def load_file(file_name):
    """ Reads binary file
    :param file_name: (string) of file name
    :return: (list) of stored file data
    """
    import pickle    # imports pickle module

    with open(file_name, 'rb') as file:    # automatically closes file when done
        list = pickle.load(file)           # unpickling

    return (list)


# Presenting --------------------------------------------------------- #
def show_menu():
    """ Displays Menu Option to the User

    :return: nothing
    """
    print('''
        Menu of Options
        1) Add a new grocery item
        2) Show current list
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
    print()  # Add an extra line for looks


def input_item_price():
    """ Gets new grocery item and price

    :return: (string) of item name
    :return: (float) of item price
    """
    item = str(input('Please enter a grocery item: ')).strip()
    price = float(input('Please enter its price: ').strip())

    return item, price


def show_list(list):
    """ Shows Current Grocery List
    :param list: (list) of items
    :return: nothing
    """
    print("\n******* The Current Grocery List: *******")
    for row in list:
        print(row[0], row[1], sep=' - ')
    print("*******************************************")

# Custom Exception Class ------------------------------------------------ #
class PriceError(Exception):
    """Price must be valid: no negative or zero values """
    def __str__(self):
        return 'You have to pay for things!'

# Main body of the Script------------------------------------------------ #
while True:
    show_menu()
    strMenuChoice = str(input('Which option would you like to perform?: ').strip())

    if strMenuChoice == '1':  # Adding new item to grocery list
        
        try:
            strItem, fltPrice = input_item_price()
            if fltPrice <= 0.0:                         # custom error condition
                raise PriceError()  # raising custom error
            lstGroceries = add_item(strItem, fltPrice, lstGroceries)

        except ValueError as e:                              # error handling if price entered as string
            print('Use numbers for price!')
        except Exception as e:                               # handling errors in Exception class
            print('Invalid price value')
            print(e, e.__doc__, type(e), sep='\n')


    elif strMenuChoice == '2':  # Showing current list
        show_list(lstGroceries)

    elif strMenuChoice == '3':  # Saving data to binary file/ pickling
        strStatus = save_file(fileName, lstGroceries)
        print(strStatus)

    elif strMenuChoice == '4':     # Unpickling file in load_file
        
        try:
            print('\n******* The Grocery List: *******')
            fileData = load_file(fileName)
            for row in fileData:
                print(row[0], row[1], sep=' - ')
            print('*' * 33)
            
        except FileNotFoundError as e:  # error handling for when file does not exist
            print('File does not exist! Please enter data and save first\n')
            print('Built in Python error info:')
            print(e, e.__doc__, sep='\n')
            print('Python error type:', type(e))

    elif strMenuChoice == '5':
        break

    else:
        print('Please only choose 1 to 5!')
