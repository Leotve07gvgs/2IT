
fil = open("planeter.txt", "w")
fil.write("Mars\n")
fil.close

with open("planeter.txt", "a") as fil:
    fil.write("Jorda")