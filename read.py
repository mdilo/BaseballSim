import pandas as pd

# Read in files
people = pd.read_csv("People.csv")
pitchers = pd.read_csv("Pitching.csv")
batters = pd.read_csv("Batting.csv")

# Limit "people" database to just first and last names
people = people[['playerID', 'nameFirst', 'nameLast']]

# Restrict data to 2017
pitchers = pitchers[(pitchers['yearID'] == 2017)]
batters = batters[(batters['yearID'] == 2017)]

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
    def get_avg(self):
        if self.position == 'pitcher':
            find_person = pitchers[(pitchers['playerID'] == self.playerID)]
            avg = find_person.iloc[0]['BAOpp']

        elif self.position == 'batter':
            find_person = batters[(batters['playerID'] == self.playerID)]
            avg = find_person.iloc[0]['H'] / find_person.iloc[0]['AB']

        return "{0:.3f}".format(avg)

test1 = People('Aaron', 'Nola', 'pitcher')
test2 = People('Wil', 'Myers', 'batter')

print(test1, People.locate(test1), People.get_avg(test1))
print(test2, People.locate(test2), People.get_avg(test2))
