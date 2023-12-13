# NBA dashboard

## Introduction

This dashboard was created out of curiosity to be most invested into the 2023-24 season of the NBA. In the end I have gathered and cleaned data from the NBA using API and endpoints to show the current top performing players and teams using existing and created measures within Power BI.

### Measures

- Points
- Assists
- Rebounds (Offensive, Defensive and Total)
- Blocks (Attempted, Total)
- Field Goals (Made, Attempted, 3's Made, 3' Attempted, %)
- Free Throws (Made, Attempted, %)
- Games Played 
- Fouls
- Steals
- Turnovers

#### Created Measures 

All created measures can be found [here](<https://en.wikipedia.org/wiki/Efficiency_(basketball)>).

- Efficiency
- Personal Efficiency Rating

## Data Gathering

Python was used to retrieve the data using the websites endpoints. Querying these endpoints will yield our desired data in JSON form. Most of the cleaning will be done in Power BI but the addition of image URL for both the teams and players are done in this step.

## Data Cleaning

Power BI is great for cleaning. Having the power steps very advantageous when wanting to remove steps while keep future steps in place. I frequently used this and created the additional measures in power query.

## Dashboard

Once all the measures have been created. It is relatively simple to put together the visualisations for the dashboard. Having domain expertise makes it easier in displaying what is necessary. This is especially true when showing the best performances/players of the season. 

## Screenshots

![[/Assets/Teams.png]]

![[Players.png]]

![[Best performances.png]]
