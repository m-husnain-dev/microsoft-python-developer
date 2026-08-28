import pandas as pd
from bs4 import BeautifulSoup

# Step 3.1: Fetch HTML Content
# Local HTML file ko read karke BeautifulSoup se parse kar rahe hain
url = "http://localhost:8000/learn/baseball_stats.html"

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
except Exception as e:
    # Fallback to local file read if network call fails
    with open("baseball_stats.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

# Step 3.2: Extract the Required Data
game_data = []

# Table ke tbody me se tamam rows <tr> find kar rahe hain
rows = soup.find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 7:
        game_id = cols[0].get_text(strip=True)
        team1 = cols[1].get_text(strip=True)
        team2 = cols[2].get_text(strip=True)
        exp_runs_team1 = cols[3].get_text(strip=True)
        exp_runs_team2 = cols[4].get_text(strip=True)
        over_under = cols[5].get_text(strip=True)
        moneyline_fav = cols[6].get_text(strip=True)

        game_data.append(
            {
                "GameID": game_id,
                "Team 1": team1,
                "Team 2": team2,
                "Expected Runs (Team 1)": exp_runs_team1,
                "Expected Runs (Team 2)": exp_runs_team2,
                "Over/Under": over_under,
                "Moneyline Favorite": moneyline_fav,
            }
        )


# Step 4.1: Convert to a DataFrame
# Extracted list ko pandas DataFrame me convert kar rahe hain
df = pd.DataFrame(game_data)

# Inspect the DataFrame
print("--- Extracted Data Preview ---")
print(df.head())


# Step 5.1: Save to a CSV File
# Exact requirement 'sports_statistics.csv' ke naam se save kar rahe hain
df.to_csv("sports_statistics.csv", index=False)
print("\nSuccess! CSV file generated: sports_statistics.csv")