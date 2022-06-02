# Assignment 07
###### *SOrellana, 05/31/2022*
###### *Foundations of Programming: Python*

## Introduction
  In this assignment I have written a script, that allows user to enter grocery items and its prices. Once grocery list is complete, the user can save it into a file. Once file is saved, the program can load it back again to display. I have used pickle module to create a file with grocery items in binary format and to display its contents. The script have error handling included to catch invalid user input.

## Starting the Grocery List
  When the program starts running, I want it to display menu options to the user to choose from. I created a custom function called *show_menu():*
```
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
```

 Then I let the user to enter their menu option and capture it as *strMenuChoice* variable. Menu option 1 is to add new grocery item to the list. I assign variables *strItem* and *fltPrice* to value of custom function *input_item_price()*, that collects user input for new data. I want prices to be in numeric values, so I converted *fltPrice* from string input value to float type, when function was defined:

```
    def input_item_price():
    """ Gets new grocery item and price

    :return: (string) of item name
    :return: (float) of item price
    """
    item = str(input('Please enter a grocery item: ')).strip()
    price = float(input('Please enter its price: ').strip())

    return item, price
```
    
  To catch the user entering wrong data, I added *try-except* construct. I want prices to be entered as numbers and to not be zero or negative values. I created a custom class error *PriceError* in Exception base class with a custom message:
```
# Custom Exception Class
class PriceError(Exception):
    """Price must be valid: no negative or zero values """
    def __str__(self):
        return 'You have to pay for things!'
 ```

  Now I can raise it in my main script body. After user input is collected for *strItem* and *strPrice*, I added the *if* statement for when price is zero or negative to raise the above created custom Exception class *PriceError*. Then the *try* block of code ends with custom function *add_item(strItem, fltPrice, lstGroceries)*, that adds new data to the list called *lstGroceries*.
	I added *ValueError* class in the first except statement for when user enters price as a word to show a message that they need to use numbers, as well the *Exception* class. 
```
if strMenuChoice == '1':  # Adding new item to grocery list
    
    try:
        strItem, fltPrice = input_item_price()
        if fltPrice <= 0.0:                         # custom error condition
            raise PriceError()                      # raising custom error
	  lstGroceries = add_item(strItem, fltPrice, lstGroceries)

    except ValueError as e:       # error handling if price entered as string
        print('Use numbers for price!')
    except Exception as e:        # handling errors in Exception class
        print('Invalid price value')
        print(e, e.__doc__, type(e), sep='\n')
```
I tested the program to add ‘apple’ as item and ‘ten’ as its price and received a message showing to use numbers for price, as it recognized error as ValueError type, and it proceeds to display menu options. Figure 01 shows the results.
![/IntroToProg-Python-Mod07/docs/screenshots/Figure 01.png](https://github.com/saglarao/IntroToProg-Python-Mod07/blob/main/docs/screenshots/Figure%2001.png?raw=true)
***Figure 01. Custom Message for ValueError***
    
Then I want to see what the user will get, if they enter price as ‘0’, Figure 02 shows the result.

![***Figure 02.***](https://raw.githubusercontent.com/saglarao/IntroToProg-Python-Mod07/main/docs/screenshots/Figure%2002.png)
***Figure 02. PriceError***

Figure 02 shows, that when the value is ‘0’ (it will work same way, if I enter a negative number), the user gets print message (“Invalid price value”) from Exception class, then it shows my custom message, doc string and its type from derived class PriceError that I defined. 


Next option on the menu is to show current data, I created custom function *show_list(list)*, that shows the data that was entered so far. I unpacked the list and print its values separating them with hyphen:
```
def show_list(list):
    """ Shows Current Grocery List
    :param list: (list) of items
    :return: nothing
    """
    print("\n******* The Current Grocery List: *******")
    for row in list:
        print(row[0], row[1], sep=' - ')
    print("*******************************************")
  ```
  
  The main body of the script looks like this:
  ```
  elif strMenuChoice == '2':  # Showing current list
    show_list(lstGroceries)
  ```
  
  ## Saving Data to a Binary File
  Menu option 3 lets user to save the data into a binary file. I have created a custom function *save_file(file_name, list)* to perform this task. First, I import *pickle* module inside of the function, then I open/create the file to write data and save the data to it by using *pickle.dump()* method. The return is status message, that the data was saved.
  ```
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
   ```
   
   In the main body of the script I assign variable *strStatus* to the string value that is returned from function *save_file*, then display *strStatus* to the user:
```
elif strMenuChoice == '3':  # Saving data to binary file/ pickling
    strStatus = save_file(fileName, lstGroceries)
    print(strStatus)
 ```
 Once I added couple grocery items to the list, I choose option 3 to save it into file and receive a message, that data was saved. 
 ![***Figure 03***](https://raw.githubusercontent.com/saglarao/IntroToProg-Python-Mod07/main/docs/screenshots/Figure%2003.png)
 ***Figure 03. Saving data***
 
 New file *“GroceryList.dat”* appears in the project folder. When I open it, it hold binary type data, which I can’t really read.
 
 ![***Figure 04***](https://raw.githubusercontent.com/saglarao/IntroToProg-Python-Mod07/main/docs/screenshots/Figure%2004.png) 
 ***Figure 04. GroceryList.dat with binary data.***
 
 ## Reading Binary Data From File
Now that my data is saved, I can reload it back from file to display in the program. I have created a custom function *load_file(file_name)*. To run this function, I imported *pickle* module, then opened the file to read and used *pickle.load()* to extract the data, returning the list of data as a result.
```
def load_file(file_name):
    """ Reads binary file
    :param file_name: (string) of file name
    :return: (list) of stored file data
    """
    import pickle    # imports pickle module

    with open(file_name, 'rb') as file:  #automatically closes file when done
        list = pickle.load(file)         #unpickling

    return (list)
 ```
 
 In the main body of the script I want to catch the error for when the user tries to choose menu option 4 to load file data before file is created. I used try-except and *FileNotFoundError* to capture the error and printed my custom messages: one is to say, that file does not exist and the other is to define a header for the following default class messages. I have displayed error messages differently from earlier, just to show different ways, I would most likely be more consistent otherwise.

```
elif strMenuChoice == '4':     # Unpickling file in load_file
    
    try:
        fileData = load_file(fileName)
        for row in fileData:
            print(row[0], row[1], sep=' - ')
        
    except FileNotFoundError as e:  #error handling file does not exist
        print('File does not exist! Please enter data and save first\n')
        print('Built in Python error info:')
        print(e, e.__doc__, sep='\n')
        print('Python error type:', type(e))
 ```
  Since I already had file saved, I tested the unpicking the data first to make sure, it loads and displays correctly. Figure 05 shows the results. 
  ![***Figure 05***](https://github.com/saglarao/IntroToProg-Python-Mod07/blob/main/docs/screenshots/Figure%2005.png?raw=true)
  
  ***Figure 05. Loading data from file.***
  
  Next I deleted the file to see an error message. Figure 06 shows what program does, if the file doesn’t exist and I try to choose option 4 of the menu.
  
  ![***Figure 06***](https://raw.githubusercontent.com/saglarao/IntroToProg-Python-Mod07/main/docs/screenshots/Figure%2006.png)
  
  ***Figure 06. FileNotFoundError.***
  
  ## Running the script in Command shell
  When my script was ready and ran smoothly in PyCharm, I tested it in Terminal as well by calling python3 command and copying the script’s pathway. I started with adding items to the list and purposefully entering second item’s price as 0. Figure 07 shows the result.
  ![***Figure 07***](https://raw.githubusercontent.com/saglarao/IntroToProg-Python-Mod07/main/docs/screenshots/Figure%2007.png)
  
  ***Figure 07. Adding items to the list in Terminal.***
  
  Next, I saved the list to a file by choosing option 3, once saved, the program was able to read it and then display it back to me. Only one item is shown, as the second item had wrong price and it wasn’t added to the list. Figure 08 is the screenshot of how it looks.
  ![***Figure 08***](https://raw.githubusercontent.com/saglarao/IntroToProg-Python-Mod07/main/docs/screenshots/Figure%2008.png)
  
  ***Figure 08. Saving and reading binary file from Terminal.***
  
  The program works the same way, as it did in PyCharm, with the exception of location of the file, that if needed could be specify in the script.
  
  ## Summary
  The script lets the user to add items to the grocery list, then saves it as a binary data into a file, that can be later extracted back to display by using pickle module. While collecting user input, I added custom and regular error handling to catch incorrect value, display more user friendly message, as well as have the program to continue to run instead of shutting down.
  The code could be improved by adding more menu options like removing item from the list, having a nicer exit or adding another error handling for when the user uses numbers instead of words. However, the focus was on pickling and error handling, and, hopefully, I covered that in this assignment.
 
