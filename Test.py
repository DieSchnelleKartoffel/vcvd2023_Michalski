#Hello and welcome to the code! Equations used here have been derived
#independently on the piece of paper using good old ballpen, maths and
#physics knowledge from presentation. Photo of the calculations is
#included in repository.

#Importing libraries for maths and graph plotting. I've read article
#to do it: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1

import math
import matplotlib.pyplot as plt

#declaration of kilometer, hour and milisecond:
kilometer = float(1000)
hour = float(3600)
milisec = float(1000)

#Firstly, we want to plot table with different friction coefficients:
print("LIST OF FRICTION COEFFICIENT")
print("  (for rubber car tires)")
print("concrete dry ---------- 0,65")
print("concrete wet ----------- 0,4")
print("ice dry ---------------- 0,2")
print("ice wet ---------------- 0,1")
print("water aquaplanning ----- 0,1")
print("gravel dry ------------ 0,35")
print("sand dry --------------- 0,3")
print("")

#Secondly, we want to ask politely about conditions, in which car is
#currently on the road, to calculate everything.
print("Insert speed of a car in kilometers per hour:")
speed = float(input())
print("Insert mass of a car in kilograms:")
mass = float(input())
print("Insert reaction time of driver in seconds:")
print("//average: 0.3")
reactionTime = float(input())
print("Insert gravity in meters per second squared:")
print("//gravity on Earth: 9.81")
gravity = float(input())
print("Insert friction of coefficient of the road:")
print("//table of examples is listed above")
friCoeff = float(input())

#Thirdly, we want to start calculating everything step by step.
speedms = float(speed*kilometer/hour)
print('speedms: ',speedms)

#time of braking, derived to know, what will be the list size:
brakingTime = float(speedms/(friCoeff*gravity))
print('brakingTime: ',brakingTime)
brakingTimeRound = int(round((brakingTime*milisec), 0) + 1)
print('brakingTimeRound: ',brakingTimeRound)
brakingTotal = int(brakingTimeRound + reactionTime*milisec)

#creation of two sets of lists:
speedList = list(range(0,brakingTotal-1))
print('speedList: ', speedList)
distanceList = list(range(0,brakingTotal-1))
print('distanceList: ',distanceList)
timeList = list(range(0,brakingTotal-1))

#calculation of speed to fill the speedList:
for brakingTotal in speedList:
    if brakingTotal < (reactionTime*milisec):
        speedList[brakingTotal] = float(speedms)
    else:
        speedList[brakingTotal] = float(speedms - (0.5)*friCoeff*gravity*(brakingTotal/milisec-reactionTime)*(brakingTotal/milisec-reactionTime))

print('speedList calculated: ', speedList)
#calculation of distance to fill the speedList:
for brakingTotal in distanceList:
    if brakingTotal < (reactionTime*milisec):
        distanceList[brakingTotal] = float(speedms * (brakingTotal/milisec))
    else:
        distanceList[brakingTotal] = float((speedms * reactionTime) + (speedms * ((brakingTotal/milisec)-(reactionTime))) - ((0.5)*friCoeff*gravity*(((brakingTotal/milisec)-(reactionTime)))*((brakingTotal/milisec)-(reactionTime))))

print('distanceList calculated: ',distanceList)
#Now, after calculations are done, we need only to draw graphs.
        
plt.plot(timeList, speedList)
plt.xlabel('Time (ms)')
plt.ylabel('Velocity (m/s)')
plt.title("Velocity of car during braking")
plt.show()

plt.plot(timeList, distanceList)
plt.xlabel('Time (ms)')
plt.ylabel('Distance (m)')
plt.title("Distance of car during braking")
plt.show()

