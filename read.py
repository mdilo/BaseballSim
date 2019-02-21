# Use to locate and find player averages

import pandas as pd

# Read in files
def readFiles():
    global people 
    global pitchers 
    global batters 

    people = pd.read_csv("CSV_files/People.csv")
    pitchers = pd.read_csv("CSV_files/Pitching.csv")
    batters = pd.read_csv("CSV_files/Batting.csv")

    # Limit "people" database to just first and last names
    people = people[['playerID', 'nameFirst', 'nameLast']]

    # Restrict data to 2017
    pitchers = pitchers[(pitchers['yearID'] == 2017)]
    batters = batters[(batters['yearID'] == 2017)]

readFiles()

class People():

    def __init__(self, first, last, position, playerID = None):
        self.first = first
        self.last = last
        self.position = position

    def __str__(self):
        return self.first + " " + self.last

# Use first and last name to find playerID
    def locate(self):
        ID_person = people[(people['nameFirst'] == self.first) & (people['nameLast'] == self.last)]
        self.playerID = ID_person.iloc[0]['playerID']
        return self.playerID

# Determine which database to use and return player BAOpp or BA
    def chooseData(self):
        global find_person

        self.playerID = People.locate(self)
        if self.position == 'pitcher':
            find_person = pitchers[(pitchers['playerID'] == self.playerID)]

        elif self.position == 'batter':
            find_person = batters[(batters['playerID'] == self.playerID)]

        return find_person

test1 = People('Aaron', 'Nola', 'pitcher')
test2 = People('Eric', 'Hosmer', 'batter')

# print(test1, People.locate(test1), People.chooseData(test1))