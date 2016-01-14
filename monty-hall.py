"""
Use this script to prove to oneself that switching doors yields a 2/3, not 1/2,
probability of winning the goat. This script implements a Monte Carlo simulation.

If the script takes too long, try reducing numTrials (however beware as Monte Carlo
simulations are quite slow to converge).
"""

import random

prob_car = 0;
numWithCar = 0;
numTrials = 1000000;

def monteCarlo():
    doors = [1,0,0]
    random.shuffle(doors)
    car = doors.index(1)
    selected = random.randint(0,2)
    if car == selected:
        return 0
    else:
        none = doors.index(0)
        if none == selected:
            none = 3 - selected - car
        other = 3 - selected - none
        return doors[other]

for i in range(numTrials):
    numWithCar+=monteCarlo()
print("Calculated probability of winning the car: ", numWithCar/numTrials)