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
sales = SHEET.worksheet('sales')

# Here, we declare another variable called 'data' and use the get_all_values()
# of the gspread method to pull all the values from our sales worksheet.
data = sales.get_all_values()

# This prints the content of the 'data' variable to the terminal.
# It produces a list of lists. Each nested list contains a row
# within our sales worksheet. The first row is our sandwich
# headings & the second row is our first set of numbers from
# the sales worksheet etc.
# This shows that our API credentials are working & our Python
# code is pulling data from our spreadsheet.
print(data)
