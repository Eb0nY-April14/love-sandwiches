# python code goes here
import gspread
from google.oauth2.service_account import Credentials

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
    Get sales figure input from the user
    """
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
    validate_data(sales_data)
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
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    # print(values)


get_sales_data()
