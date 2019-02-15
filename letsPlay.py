import random
import pandas as pd

countRates = pd.read_csv("joey.csv")
hitRates = pd.read_csv("wil.csv")



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
        self.cbRate = throwRates.iloc[0]['cbRate']
        return [self.fbRate, self.chRate, self.cbRate]

class Batter():

    def __init__(self, first, last, position, avg, BB, fbHit, chHit, cbHit):
        self.first = first
        self.last = last
        self.position = position
        self.avg = avg
        self.BB = BB
        self.fbHit = fbHit
        self.chHit = chHit
        self.cbHit = cbHit

    def __str__(self):
        return self.first + " " + self.last

    def hitArray(self):
        self.fbHit = hitRates.iloc[0]['rate']
        self.chHit = hitRates.iloc[1]['rate']
        self.cbHit = hitRates.iloc[2]['rate']
        return [self.fbHit, self.chHit, self.cbHit]

    def atBat(self):
        hits = 0
        walks = 0
        ab = 0
        outProb = 1 - (self.avg + self.BB)
        for i in range(1000):
            a = random.choices(['h', 'w', 'o'], [self.avg, self.BB, outProb], k=1)
            if a == ['h']:
                ab += 1
                hits += 1
            elif a == ['w']:
                walks += walks
            elif a == ['o']:
                ab += 1
            i += 1
        totalPA = i
        battingAvg = hits / ab
        OBP = (hits + walks) / totalPA
        print(p1,
        '|', hits, '/', ab,
        '|', "{0:.3f}".format(battingAvg), 'AVG',
        '|', "{0:.3f}".format(OBP), 'OBP')

p1 = Batter('Wil', 'Myers', 'OF', .300, .100, 0, 0, 0)
p2 = Batter('Eric', 'Hosmer', '1B', .250, .092, 0, 0, 0)
sp = Pitcher('Joey', 'Lucchesi', 'SP', 0, 0, 0)


def pitch():
    throw = random.choices(['fb', 'ch', 'cb'], Pitcher.pitchArray(sp), k=1)
    return throw




#I believe issue is in this block
#maybe something with the return value I don't know
def situation():
    pitch()
    if pitch() == ['fb']:
        hit = random.choices(['hit', 'miss', 'ball'],
                             [Batter.hitArray(p1)[0],
                             (1 - Batter.hitArray(p1)[0])/2,
                             (1 - Batter.hitArray(p1)[0])/2], k=1)
        print('test-', hit)
        return hit
    elif pitch() == ['ch']:
        hit = random.choices(['hit', 'miss', 'ball'],
                             [Batter.hitArray(p1)[1],
                             (1 - Batter.hitArray(p1)[1])/2,
                             (1 - Batter.hitArray(p1)[1])/2], k=1)
        print('test-', hit)
        return hit
    elif pitch() == ['cb']:
        hit = random.choices(['hit', 'miss', 'ball'],
                             [Batter.hitArray(p1)[2],
                             (1 - Batter.hitArray(p1)[2])/2,
                             (1 - Batter.hitArray(p1)[2])/2], k=1)
        print('test-', hit)
        return hit
    else:
        return 'something is wrong'






# function somewhat working, but can't get loop to continue after ball
def result():
    global balls
    global strikes
    global situation
    balls = 0
    strikes = 0
    while balls <= 3 & strikes <= 2:
        print(balls, '-', strikes)
        situation()
        if situation() == ['hit']:
            outcome = 'you got a hit!'
            print(outcome)
            break
        elif situation() == ['miss']:
            strikes += 1
            outcome = 'strike'
            print(outcome)
        elif situation() == ['ball']:
            balls += 1
            outcome = 'ball'
            print(outcome)


    if balls == 4:
        print('walk')
    elif strikes == 3:
        print('K')

result()
