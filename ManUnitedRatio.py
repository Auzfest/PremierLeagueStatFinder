import pandas as pd

def FindManURatio():
    #read csv containing Premier League statistics from 2006 to 2018
    PLstats = pd.read_csv("stats.csv")

    print("from 2006-2018")

    #find the total wins for Manchester United
    ManUWins = PLstats.loc[PLstats['team'] == "Manchester United", "wins"]
    ManUTotalWins = 0.0

    for count in ManUWins:
        ManUTotalWins += count

    print(f"Manchester United total wins: {ManUTotalWins:0,.0f}")

    #find the total losses for Manchester United
    ManULosses = PLstats.loc[PLstats['team'] == "Manchester United", "losses"]
    ManUTotalLosses = 0.0

    for count in ManULosses:
        ManUTotalLosses += count

    print(f"Manchester United total losses: {ManUTotalLosses:0,.0f}")

    #find the total goals for Manchester United
    ManUGoals = PLstats.loc[PLstats['team'] == "Manchester United", "goals"]
    ManUTotalGoals = 0.0

    for counter in ManUGoals:
        ManUTotalGoals += counter

    print(f"Manchester United total goals: {ManUTotalGoals:0,.0f}")

    #Divide Manchester United losses and wins
    ManURatio = ManUTotalLosses / ManUTotalWins
    print(f"Manchester United losses/win ratio: {ManURatio:0,.2f}")

    #get average goals scored per game
    ManUTotalGames = ManUTotalLosses + ManUTotalWins
    ManUAverageGoals = ManUTotalGoals / ManUTotalGames
    print(f"On average they scored {ManUAverageGoals:0,.2f} goals per game")