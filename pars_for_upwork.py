
import requests
from bs4 import BeautifulSoup

# Define the URL of the directory you want to scrape
url = 'https://ncuso.org/credit-union/'

# Send a GET request to the URL to retrieve the page
response = requests.get(url)

# Parse the page using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the list of credit unions
table = soup.find('table')

# Loop through the rows in the table
for row in table.find_all('tr'):
    # Get the cells in the row
    cells = row.find_all('td')

    # If the row contains data for a credit union
    if len(cells) > 0:
        # Get the name of the credit union
        name = cells[0].text

        # Get the state of the credit union
        state = cells[2].text

        # Check if the credit union is from one of the states you are interested in
        if state in ['California', 'Georgia', 'Ohio', 'Kansas', 'Montana', 'Kentucky', 'Virginia', 'Oklahoma']:
            # Print the name and state of the credit union
            print(name, state)
