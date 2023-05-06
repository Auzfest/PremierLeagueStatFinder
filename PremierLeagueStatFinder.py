import ManUnitedRatio
import ManCityRatio
import LiverpoolRatio
import ArsenalRatio

def main():
    print("\n")
    print("This program takes the Premier League goals, losses and wins between 2006 and 2018 from select teams below")
    done = 0
    while done != 1:
        print("\n")
        print("Type the number corresponding to the team you want to view or 5 to quit")
        print("1. Manchester United")
        print("2. Manchester City")
        print("3. Liverpool")
        print("4. Arsenal")
        print("5. quit")
        userChoice = int(input("Type here -> "))
        print("\n")

        if userChoice == 1:
            ManUnitedRatio.FindManURatio()
        elif userChoice == 2:
            ManCityRatio.FindManCityRatio()
        elif userChoice == 3:
            LiverpoolRatio.FindLiverpoolratio()
        elif userChoice == 4:
            ArsenalRatio.FindArsenalratio()
        elif userChoice == 5:
            done = 1
        else:
            print("Invalid response, please try again")

if __name__ == "__main__":
    main()