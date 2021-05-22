'''
Prequisties
1. Open account in Google API
  a. Activate the account
  b. Enable Google Drive API 
  c. Create Service account 
    i. goto Keys and add keys => download JSON
2. Make sure the google sheet is visible to everyone
---------------------------------------                 KEY                         -------------------
https://docs.google.com/spreadsheets/d/1nqYVCwF6qtjM-KfIekq4YuN005FPX0pzcdBPw0z6QEE/edit#gid=1386834576
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('../arcane-optics-314123-a79fd8ea1a55.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_key("1nqYVCwF6qtjM-KfIekq4YuN005FPX0pzcdBPw0z6QEE")
# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# Extract and print all of the values
list_of_hashes = sheet_instance.get_all_records()
print(list_of_hashes)
