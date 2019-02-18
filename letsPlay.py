import random
import pandas as pd

# Read in batter and pitcher CSVs
# Reed to make these self specific, each player has own rates
countRates = pd.read_csv("joey.csv")
hitRates = pd.read_csv("wil.csv")

# Create a class for pitchers with name and rates
class Pitcher():

    def __init__(self, first, last, position, fbRate, chRate, cbRate):
        self.first = first
        self.last = last
        self.position = position
        self.fbRate = fbRate
        self.chRate = chRate
        self.cbRate = cbRate

    # Gives full name of instance as a string
    def __str__(self):
        return self.first + " " + self.last

# Spit out array of pitch rates during given count
    def pitchArray(self):
        throwRates = countRates[(countRates['balls'] == balls) & (countRates['strikes'] == strikes)]
        self.fbRate = throwRates.iloc[0]['fbRate']
        self.chRate = throwRates.iloc[0]['chRate']
        self.cbRate = throwRates.iloc[0]['cbRate']
        return [self.fbRate, self.chRate, self.cbRate]

# Create a class for batters with names and hit rates
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

# Spit out hit rates given the pitch thrown
    def hitArray(self):
        self.fbHit = hitRates.iloc[0]['rate']
        self.chHit = hitRates.iloc[1]['rate']
        self.cbHit = hitRates.iloc[2]['rate']
        return [self.fbHit, self.chHit, self.cbHit]


# Randomly (weighted) choose pitch based on rates given from pitchArray
def pitch(pitcher):
    global throw
    throw = random.choices(['fb', 'ch', 'cb'], Pitcher.pitchArray(pitcher), k=1)[0]
    return throw

# Determine if the batter will hit, miss, or ball based on pitch thrown
# Have to get actual rates for this and determine if pitch is in or out of zone
def situation(pitcher,batter):
    global hit
    pitch(pitcher)
    if throw == 'fb':
        hit = random.choices(['hit', 'miss', 'ball'],
                             [Batter.hitArray(batter)[0],
                             (1 - Batter.hitArray(batter)[0])/2,
                             (1 - Batter.hitArray(batter)[0])/2], k=1)[0]
    elif throw == 'ch':
        hit = random.choices(['hit', 'miss', 'ball'],
                             [Batter.hitArray(batter)[1],
                             (1 - Batter.hitArray(batter)[1])/2,
                             (1 - Batter.hitArray(batter)[1])/2], k=1)[0]
    elif throw == 'cb':
        hit = random.choices(['hit', 'miss', 'ball'],
                             [Batter.hitArray(batter)[2],
                             (1 - Batter.hitArray(batter)[2])/2,
                             (1 - Batter.hitArray(batter)[2])/2], k=1)[0]
    else:
        hit = 'broke'
    return hit

# Determine count using above functions
def result():
    global balls
    global strikes
    balls = 0
    strikes = 0

    print('PITCHING:', pitcher_list[0])
    for i in range(len(batter_list)):
        batter = batter_list[i]
        print('AT BAT:', batter)
        while balls <= 3 and strikes <= 2:
            print(balls, '-', strikes)
            situation(pitcher, batter)
            if hit == 'hit':
                print('you got a hit!')
                break

            elif hit == 'miss':
                strikes += 1
                print('strike')

            elif hit == 'ball':
                balls += 1
                print('ball')

        if balls == 4:
            print('WALK')
            break
        elif strikes == 3:
            print('K')
            break

# Arbitrary hitters and pitchers to test functions
p1 = Batter('Wil', 'Myers', 'OF', .300, .100, 0, 0, 0)
p2 = Batter('Eric', 'Hosmer', '1B', .250, .092, 0, 0, 0)
sp = Pitcher('Joey', 'Lucchesi', 'SP', 0, 0, 0)

pitcher_list = [sp]
batter_list = [p1, p2]

pitcher = pitcher_list[0]
result()
