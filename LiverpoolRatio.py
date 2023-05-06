import pandas as pd

def FindLiverpoolratio():
    #read csv containing Premier League statistics from 2006 to 2018
    PLstats = pd.read_csv("stats.csv")

    print("from 2006-2018")

    #find the total wins for Liverpool
    LiverpoolWins = PLstats.loc[PLstats['team'] == "Liverpool", "wins"]
    LiverpoolTotalWins = 0.0

    for count in LiverpoolWins:
        LiverpoolTotalWins += count

    print(f"Liverpool total wins: {LiverpoolTotalWins:0,.0f}")

    #find the total losses for Liverpool
    LiverpoolLosses = PLstats.loc[PLstats['team'] == "Liverpool", "losses"]
    LiverpoolTotalLosses = 0.0

    for count in LiverpoolLosses:
        LiverpoolTotalLosses += count

    print(f"Liverpool total losses: {LiverpoolTotalLosses:0,.0f}")

    #find the total goals for Liverpool
    LiverpoolGoals = PLstats.loc[PLstats['team'] == "Liverpool", "goals"]
    LiverpoolTotalGoals = 0.0

    for counter in LiverpoolGoals:
        LiverpoolTotalGoals += counter

    print(f"Liverpool total goals: {LiverpoolTotalGoals:0,.0f}")

    #Divide Liverpool goals and wins
    LiverpoolRatio = LiverpoolTotalGoals / LiverpoolTotalWins
    print(f"Liverpool goal/win ratio: {LiverpoolRatio:0,.2f}")

    #get avaerage goals scored per game
    LiverpoolTotalGames = LiverpoolTotalLosses + LiverpoolTotalWins
    LiverpoolAverageGoals = LiverpoolTotalGoals / LiverpoolTotalGames
    print(f"On average they scored {LiverpoolAverageGoals:0,.2f} goals per game")