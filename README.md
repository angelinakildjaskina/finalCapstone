# finalCapstone - Invetory Program
This project is an inventory program that allows the user to perform various actions with the inventory text file. This program could be applied for stock taking which is crucial for the management of a warehouse of any kind.

## How to Install the Program
* Download this repository as a .zip file
* Unzip the downloaded materials
* Open a IDE (for example, Visual Studio Code) and open the **inventory.py** file through it
  * You can drag and drop the file from the downloaded folder
* Done! You can now run the program
  * Always ensure that the **inventory.txt** file is in the same directory as **inventory.py**

## Project Setup
### What does the program do?
* The Shoe class is created
  * We use this class to create Shoe objects that have 5 attributes
* read_shoes_data() function reads from the text file and appends each objects to the list 
* capture_shoes() allows the user to add a new shoe obejct to the list
* view_all() function prints out all the shoe objects in a user-friendly manner
* re_stock() allows the user to identify the shoe with the lowest stock
  * It then asks the user if they'd like to re-stock the pair
* search_shoe() allows the user to find a shoe by searching up the product code (SKU)
* value_per_item() displays the total value of each product (quantity * price)
* highest_qty() identifies the shoe with the highest quantity
  * This shoe is then displayed as being on sale

### How to use the program?
1. Select one of the meny options
2. Perform the prompted actions (if any)
3. Type **q** to quit

<img width="484" alt="Screenshot 2022-11-21 at 20 49 27" src="https://user-images.githubusercontent.com/107858619/203156650-5938a26a-aba3-4617-ad37-b0552b7f0964.png">

