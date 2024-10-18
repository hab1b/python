import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request to the website
URL = 'https://www.basketball-reference.com/leagues/NBA_2023_totals.html'
response = requests.get(URL)

# Step 2: Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find the table with player stats
table = soup.find('table', {'id': 'totals_stats'})

# Step 4: Extract the table headers
headers = [th.getText() for th in table.find_all('th')][1:30]  # Skip the 'rank' column

# Debug: Check headers and columns count
print("Headers:", headers)

# Step 5: Extract the rows of the table
rows = table.find_all('tr')[1:]

# Step 6: Collect player stats data
player_data = []
for row in rows:
    columns = row.find_all('td')
    if columns:
        # Truncate extra columns to match headers
        player_data.append([column.getText() for column in columns[:len(headers)]])  

# Step 7: Create a DataFrame and save to CSV
df = pd.DataFrame(player_data, columns=headers)
df.to_csv('nba_player_stats.csv', index=False)

print("Data successfully scraped and saved to nba_player_stats.csv")