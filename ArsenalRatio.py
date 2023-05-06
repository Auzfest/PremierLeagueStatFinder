import pandas as pd

def FindArsenalratio():
    #read csv containing Premier League statistics from 2006 to 2018
    PLstats = pd.read_csv("stats.csv")

    print("from 2006-2018")

    #find the total wins for Arsenal
    ArsenalWins = PLstats.loc[PLstats['team'] == "Arsenal", "wins"]
    ArsenalTotalWins = 0.0

    for count in ArsenalWins:
        ArsenalTotalWins += count

    print(f"Arsenal total wins: {ArsenalTotalWins:0,.0f}")

    #find the total losses for Arsenal
    ArsenalLosses = PLstats.loc[PLstats['team'] == "Arsenal", "losses"]
    ArsenalTotalLosses = 0.0

    for count in ArsenalLosses:
        ArsenalTotalLosses += count

    print(f"Arsenal total losses: {ArsenalTotalLosses:0,.0f}")

    #find the total goals for Arsenal
    ArsenalGoals = PLstats.loc[PLstats['team'] == "Arsenal", "goals"]
    ArsenalTotalGoals = 0.0

    for counter in ArsenalGoals:
        ArsenalTotalGoals += counter

    print(f"Arsenal total goals: {ArsenalTotalGoals:0,.0f}")

    #Divide Arsenal goals and wins
    ArsenalRatio = ArsenalTotalGoals / ArsenalTotalWins
    print(f"Arsenal goal/win ratio: {ArsenalRatio:0,.2f}")

    #get average goals scored per game
    ArsenalTotalGames = ArsenalTotalLosses + ArsenalTotalWins
    ArsenalAverageGoals = ArsenalTotalGoals / ArsenalTotalGames
    print(f"On average they scored {ArsenalAverageGoals:0,.2f} goals per game")