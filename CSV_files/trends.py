import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd 

def readFiles():
    global people 
    global batters 

    people = pd.read_csv("CSV_files/People.csv")
    pitchers = pd.read_csv("CSV_files/Pitching.csv")
    batters = pd.read_csv("CSV_files/Batting.csv")

    # Limit "people" database to just first and last names
    people = people[['playerID', 'nameFirst', 'nameLast']]

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

    def avgTrend(self):
        year = []
        hits = []
        for i in len(batters[(batters['playerID'] == self.playerID)]):
            




