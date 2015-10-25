import random

prob_car = 0;
numWithCar = 0;
numTrials = 10000;

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