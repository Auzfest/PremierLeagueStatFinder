import pandas as pd

def FindManCityRatio():
    #read csv containing Premier League statistics from 2006 to 2018
    PLstats = pd.read_csv("stats.csv")

    print("from 2006-2018")

    #find the total wins for Manchester City
    ManCityWins = PLstats.loc[PLstats['team'] == "Manchester City", "wins"]
    ManCityTotalWins = 0.0

    for count in ManCityWins:
        ManCityTotalWins += count

    print(f"Manchester City total wins: {ManCityTotalWins:0,.0f}")

    #find the total losses for Manchester City
    ManCityLosses = PLstats.loc[PLstats['team'] == "Manchester City", "losses"]
    ManCityTotalLosses = 0.0

    for count in ManCityLosses:
        ManCityTotalLosses += count

    print(f"Manchester City total losses: {ManCityTotalLosses:0,.0f}")

    #find the total goals for Manchester City
    ManCityGoals = PLstats.loc[PLstats['team'] == "Manchester City", "goals"]
    ManCityTotalGoals = 0.0

    for counter in ManCityGoals:
        ManCityTotalGoals += counter

    print(f"Manchester City total goals: {ManCityTotalGoals:0,.0f}")

    #Divide Manchester City losses and wins
    ManCityRatio = ManCityTotalGoals / ManCityTotalWins
    print(f"Manchester City lose/win ratio: {ManCityRatio:0,.2f}")
    
    #get average goals scored per game
    ManCityTotalGames = ManCityTotalLosses + ManCityTotalWins
    ManCityAverageGoals = ManCityTotalGoals / ManCityTotalGames
    print(f"On average they scored {ManCityAverageGoals:0,.2f} goals per game")