#wap to check whether a player has scored more than a 10000 runs and also has a strike rate of more than 100

runs=int(input("Enter the runs scored by the player : "))
strikerate= float(input("Enter the strike rate of the player : "))

if (runs >=10000 and strikerate >=100):
    print("The player has scored more than 10000 runs and also has a strike rate of more than 100")
else:
    print("The player has not scored more than 10000 runs and also has a strike rate of more than 100")
