import random

def team_compete(x, y): #takes two team scores of the teams, compares them and decides who wins
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
    #disgusting looking code which will go through a swiss bracket, making it impossible to play yourself
    #also makes it impossible to play an opponent twice


class Team():
    #initializes a team with parameters
    def __init__(self, name, score, diff = 0,win = 0):
        self.name = name
        self.score = score
        self.diff = diff
        self.win = win

    def __str__(self):
        return "Team: " + self.name + " | Score: " + str(self.score) + " | Wins: " + str(self.win) + " | Diff: " + str(self.diff)
    #returns the team's stats with no real formatting
    
team_list = [] #blank team list

teams = int(input("How many teams?\n")) #gets # of teams

while(teams > 16):
    print("!!! Team limit of 16 exceeded !!!")
    teams = int(input("How many teams?\n"))
    #checking for how many teams there are, for this program I don't allow >16 since that's a bit much :)

for i in range(teams):
    temp = input("Enter team " + str(i + 1) + " here: ")
    temp2 = input("Enter team " + str(i + 1) + "'s score here: ")
    
    temp3 = Team(temp, temp2)

    team_list.append(temp3)
    print("\n-----\n")
    #this code allows you to put in the team names and their respective scores, then appends it to the team list



swiss_bracket()

team_list.sort(key=lambda x: x.win, reverse=True) #sorts team_list by wins
team_list.sort(key=lambda x: x.diff, reverse=True) #next sorts team_list by difference in scores

for i in range(teams):
    print(team_list[i])
    #goes through all teams
