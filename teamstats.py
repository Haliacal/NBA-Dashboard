import requests
import pandas as pd
# Importing the necessary libraries

# Under the Header tab, select general and copy the first part of the request URL
url = "https://stats.nba.com/stats/leaguedashteamstats"

#Header Tab, under "Query String Parameter" subsection
params =(
("MeasureType", "Base"),
("PerMode", "PerGame"),
("PlusMinus", "N"),
("PaceAdjust", "N"),
("Rank", "N"),
("LeagueID", "00"),
("Season", "2023-24"),
("SeasonType", "Regular Season"),
("PORound", "0"),
("Outcome", ""),
("Location", ""),
("Month", "0"),
("SeasonSegment", ""),
("DateFrom", ""),
("DateTo", ""),
("OpponentTeamID", "0"),
("VsConference", ""),
("VsDivision", ""),
("TeamID", "0"),
("Conference", ""),
("Division", ""),
("GameSegment", ""),
("Period", "0"),
("ShotClockRange", ""),
("LastNGames", "0"),
("GameScope", ""),
("PlayerExperience", ""),
("PlayerPosition", ""),
("StarterBench", ""),
("TwoWay", "0"),
("GameSubtype", ""),
("ISTRound", ""),
)

# Header tab, under “Request Headers” subsection
header = {
"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"origin": "https://www.nba.com",
"referer": "https://www.nba.com/",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
"x-nba-stats-origin": "stats",
"x-nba-stats-token": "true"}

#Using Request library to get the data
response = requests.get(url, headers=header, params=params, verify=False)
response_json = response.json()
frame = pd.DataFrame(response_json['resultSets'][0]['rowSet'])
frame.columns = response_json['resultSets'][0]['headers']
print(frame.head())
frame.to_csv("datasets/teamstats.csv")