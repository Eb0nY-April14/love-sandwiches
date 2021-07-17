# python code goes here
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

# All the constants
# written below from
# line 6 to 15 of our
# code are the settings
# we need in order to
# access our spreadsheet data.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches-MS3')

# Here, we declare a
# 'sales' variable and
# use the worksheet method
# of the sheet to call
# our "sales" worksheet.
# used to check if our API
# is working correctly so
# we comment it out since
# it's not needed.
# sales = SHEET.worksheet('sales')

# Here, we declare another variable called 'data' and use the get_all_values()
# of the gspread method to pull all the values from our sales worksheet.
# used to check if our API
# is working correctly so
# we comment it out since
# it's not needed.
# data = sales.get_all_values()

# This prints the content of the 'data' variable to the terminal.
# It produces a list of lists. Each nested list contains a row
# within our sales worksheet. The first row is our sandwich type
# headings & the second row is our first set of numbers from
# the sales worksheet etc.
# This shows that our API credentials are working & our Python
# code is pulling data from our spreadsheet.
# used to check if our API
# is working correctly so
# we comment it out since
# it's not needed.
# print(data)


def get_sales_data():
    """
    Get sales figure input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data until it is valid.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60\n")

# This below(data_str) is the user-entered
# data which will be returned to us as a string.
        data_str = input("Enter your data here: ")

# The split method is used to break up our data string at the commas.
# It returns broken up values as a list.
# Our values need to be in a list in order to be able to insert them
# into our spreadsheet.
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")  # Prints this if true is returned
            break  # This ends the while loop

    return sales_data  # Returns the validated sales_data
    # print(sales_data)
    # The print statement below was used for testing purposes.
    # print(f"The data provided is {data_str}")


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    # print(values)
    try:
        # the first line of code below
        # loops through all the values in
        # the list & ensure that they are
        # all integers
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False  # returns false if an error is thrown
        # print(values)

    return True  # returns true if no error

# The update_sales_worksheet() and update_surplus_worksheet
# functions are refactored into one single function called
# update_worksheet() function so we commented out these 2
# functions.
# def update_sales_worksheet(data):
#    """
#    Update sales worksheet, add new row with the list data provided.
#    """
#    print("Updating sales worksheet...\n")
    # The "sales" enclosed in brackets
    # must correspond to the name given
    # to the sales spreadsheet we are using.
#    sales_worksheet = SHEET.worksheet("sales")
    # This line of code adds a new row to the
    # end of our data in the worksheet selected.
#    sales_worksheet.append_row(data)
#    print("Sales worksheet updated successfully.\n")


# def update_surplus_worksheet(data):
#    """
#    Update surplus worksheet, add new row with the list data provided.
#    """
#    print("Updating surplus worksheet...\n")
#    surplus_worksheet = SHEET.worksheet("surplus")
#    surplus_worksheet.append_row(data)
#    print("Surplus worksheet updated successfully.\n")

# Our newly Refactored function
def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste.
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    # The next line will access the last value in a Python list
    # when the length of the list will vary. It will slice the
    # last item of the list and store it in a variable called
    # stock_row. It will retrieve the latest stock numbers from
    # the spreadsheet.
    stock_row = stock[-1]

    # In Python list, a method called zip()
    # allows us to loop through 2 or more lists
    # at the same time.
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data
    # print(f"stock row: {stock_row}")
    # print(f"sales row: {sales_row}")
    # pprint(stock)


# Returns the sales_data value from the get_sales_data() function
# and stores it in a variable called data.
# In Python, we wrap all our function calls inside function called main
# as seen below.
def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]  # Converts our string data to list
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    print(f"The New Surplus value is: {new_surplus_data}")
    update_worksheet(new_surplus_data, "surplus")


print("Welcome to Love Sandwiches Data Automation")
main()
