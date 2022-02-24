import random

def team_compete(x, y):
    team1 = team_list[x]
    team2 = team_list[y]
    team1.diff += int(team1.score) - int(team2.score)
    team2.diff += int(team2.score) - int(team1.score)

    if (team1.score > team2.score):
        team1.win +=1
    elif(team2.score > team1.score):
        team2.win +=1


def swiss_bracket():
    itt = 0 #itt = iteration
    for ii in range(teams - (itt + 1)):
        for jj in range(itt + (ii + 1)):
            team_compete(ii +1,jj)



class Team():

    def __init__(self, name, score, diff = 0,win = 0):
        self.name = name
        self.score = score
        self.diff = diff
        self.win = win

    def __str__(self):
        return "Team: " + self.name + " | Score: " + str(self.score) + " | Wins: " + str(self.win) + " | Diff: " + str(self.diff)

team_list = []

teams = int(input("How many teams?\n"))

while(teams > 16):
    print("!!! Team limit of 16 exceeded !!!")
    teams = int(input("How many teams?\n"))

for i in range(teams):
    temp = input("Enter team " + str(i + 1) + " here: ")
    temp2 = input("Enter team " + str(i + 1) + "'s score here: ")

    temp3 = Team(temp, temp2)

    team_list.append(temp3)
    print("\n-----\n")



swiss_bracket()

team_list.sort(key=lambda x: x.win, reverse=True)
team_list.sort(key=lambda x: x.diff, reverse=True)

for i in range(teams):
    print(team_list[i])
