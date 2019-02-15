import random
import pandas as pd
from letsPlay import *


countRates = pd.read_csv("joey.csv")


class Pitcher():

    def __init__(self, first, last, position, fbRate, chRate, cbRate):
        self.first = first
        self.last = last
        self.position = position
        self.fbRate = fbRate
        self.chRate = chRate
        self.cbRate = cbRate

    def __str__(self):
        return self.first + " " + self.last

    def pitchArray(self):
        throwRates = countRates[(countRates['balls'] == balls) & (countRates['strikes'] == strikes)]
        self.fbRate = throwRates.iloc[0]['fbRate']
        self.chRate = throwRates.iloc[0]['chRate']
        self.chRate = throwRates.iloc[0]['chRate']
        return [self.fbRate, self.chRate, self.cbRate]

sp = Pitcher('Joey', 'Lucchesi', 'SP', 0, 0, 0)

def pitch():
    pitchProb = Pitcher.pitchArray(sp)
    throw = random.choices(['fb', 'ch', 'cb'], pitchProb, k=1)
    return throw
