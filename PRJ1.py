import requests
from bs4 import BeautifulSoup # bs4 is beautifulSoup 4 library
import pandas as pd

# Step 1: Fetch the HTML page
url = 'https://urbanjaipur.com/bedsheet-size-chart/' # Data of bedsheets
response = requests.get(url) # request accepted so give 200 otherwisw 404
html_content = response.content # give content of webpage in html

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser') # give a parse tree of html content 
# where tags as nodes where head tag is root and others so on

# Step 3: Extract the data you need
# Example: Extracting all rows from a table
table = soup.find('table')  # Assuming you want to extract data from the first table
rows = table.find_all('tr') # tr tags for rows where find all rows from table

# Step 4: Organize the data into a list of dictionaries
data = []
for row in rows:
    cols = row.find_all('td') # they are cells present in each row which is td given in td_cell image
    cols = [col.text.strip() for col in cols] # making list of all td mean cells 
    if cols:
        data.append(cols) # append all td mean cell in data list

# Step 5: Convert the data to a DataFrame
df = pd.DataFrame(data, columns=['Bed Sheet Type', 'Flat Bed Sheet', 'Filtered Bed Sheet'])   

# Step 6: Export the data to an Excel file
df.to_excel('Sheet.xlsx', index=False) # here index = false mean we remove starting row labels 

print("Data has been successfully exported to Sheet.xlsx")
