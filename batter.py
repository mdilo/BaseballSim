# This will just simulate a batter season using batting average and extra base hit chance
# Pull ID and avg from read.py

import pandas as pd 
import random
from datetime import datetime
from read import *

# Used for timing execution
startTime = datetime.now()

readFiles()

class Batter():

    def __init__(self, first, last, position, playerID, avg):
        self.first = first
        self.last = last
        self.position = position
        self.playerID = None
        self.avg = None

    def __str__(self):
        return self.first + " " + self.last

    # Determine batting average separate from everything
    def get_avg(self):
        self.playerID = People.locate(self)
        find_person = People.chooseData(self)

        avg = find_person.iloc[0]['H'] / find_person.iloc[0]['AB']
        
        return avg

    # Finding individual hit type rates
    def hit_types(self):
        self.playerID = People.locate(self)
        find_person = People.chooseData(self)

        hits = find_person.iloc[0]['H']
        double = find_person.iloc[0]['2B']
        triple = find_person.iloc[0]['3B']
        hr = find_person.iloc[0]['HR']
        single = hits - (double + triple + hr)

        doubleRate = double / hits
        tripleRate = triple / hits
        hrRate = hr / hits
        singleRate = single / hits

        return singleRate,doubleRate,tripleRate,hrRate
        

def atBat_sim():
    singleRate,doubleRate,tripleRate,hrRate = Batter.hit_types(test)
    avg = Batter.get_avg(test)
    missChance = 1 - avg

    hit_out = random.choices(['hit', 'out'], [avg, missChance], k=1)[0]
    if hit_out == 'hit':
        bases = random.choices(['1B', '2B', '3B', 'HR'], [singleRate, doubleRate, tripleRate, hrRate], k=1)[0]
    
    elif hit_out == 'out':
        bases = 'OUT'

    return bases


test = People('Manny', 'Machado', 'batter')

print(test, '|', People.locate(test), '|', "{0:.3f}".format(Batter.get_avg(test)))

outcome = []
for i in range(420):
    outcome.append(atBat_sim())

simAvg = "{0:.3f}".format((420 - outcome.count('OUT')) / 420)
print('simAVERAGE: ', simAvg)
print('SINGLES: ', outcome.count('1B'))
print('DOUBLES: ', outcome.count('2B'))
print('TRIPLES: ', outcome.count('3B'))
print('HOMERUNS: ', outcome.count('HR'))

# print('Time to complete execution - ', datetime.now() - startTime)