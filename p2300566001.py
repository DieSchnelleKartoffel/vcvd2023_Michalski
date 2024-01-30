#Hello and welcome to the code! Equations used here have been derived
#independently on the piece of paper using good old ballpen, maths and
#physics knowledge from presentation.

#Importing libraries for maths and graph plotting. I've read article
#to do it: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1

import math
import matplotlib.pyplot as plt

#declaration of kilometer, hour and milisecond:
kilometer = float(1000)
hour = float(3600)
milisec = float(1000)

#Firstly, we want to plot table with different friction coefficients:
print("      LIST OF FRICTION COEFFICIENT")
print("        (for rubber car tires)")
print("material:               Static   Dynamic")
print("concrete dry ----------- 0.65 -- 0.5")
print("concrete wet ----------- 0.4 --- 0.35")
print("ice dry ---------------- 0.2 --- 0.15")
print("ice wet ---------------- 0.1 --- 0.08")
print("water aquaplanning ----- 0.1 --- 0.05")
print("gravel dry ------------- ___ --- 0.35")
print("sand dry --------------- ___ --- 0.3")
print("")

#Secondly, we want to ask politely about conditions, in which car is
#currently on the road, to calculate everything.

print("Insert velocity of a car in kilometers per hour:")
velocity = float(input())
print("Insert mass of a car in kilograms:")
mass = float(input())
print("Insert friction of coefficient of the road:")
print("//table of examples is listed above")
friction = float(input())

#I've decided to add some more variety to the calculation
#results. Just out of curiosity.

print("Insert reaction time of driver in seconds:")
print("//average: 0.3")
reactionTime = float(input())
print("Insert gravity in meters per second squared:")
print("//gravity on Earth: 9.81")
gravity = float(input())

#Thirdly, we want to start calculating everything step by step.
#I'm beggining with change of speed from km/h to m/s.
speedms = float(velocity*kilometer/hour)

#time of braking, derived to know, what will be the list size:
brakingTime = float(speedms/(friction*gravity))
brakingTimeRound = int(round((brakingTime*milisec), 0) + 1)
brakingTotal = int(brakingTimeRound + reactionTime*milisec)

#creation of three sets of lists - velicity, distance and time of movement:
speedList = list(range(0,brakingTotal-1))
distanceList = list(range(0,brakingTotal-1))
timeList = list(range(0,brakingTotal-1))

#calculation of speed to fill the speedList:

for brakingTotal in speedList:
    if brakingTotal < (reactionTime*milisec):
        speedList[brakingTotal] = float(speedms)
        #if the driver did not react yet, the velocity is constant.
    else:
        speedList[brakingTotal] = float(speedms - friction*gravity*((brakingTotal/milisec)-(reactionTime)))
        #if the driver reacted, the velocity is decreasing.

#calculation of distance to fill the speedList:
#Unfortunatly, line no 82 is pretty bloated.
        
for brakingTotal in distanceList:
    if brakingTotal < (reactionTime*milisec):
        distanceList[brakingTotal] = float(speedms * (brakingTotal/milisec))
        #if the driver did not react yet, the increase of distance is constant.
    else:
        distanceList[brakingTotal] = float((speedms * reactionTime) + (speedms * ((brakingTotal/milisec)-(reactionTime))) - ((0.5)*friction*gravity*(((brakingTotal/milisec)-(reactionTime)))*((brakingTotal/milisec)-(reactionTime))))
        #if the driver reacted, the distance is increasing slower and slower.
        #Explanation of line 81:
        #Total distance = Distance before braking + Distance after applying brakes derived from the equation:
        # S = S0 + V*t - (a*t^2)/2,  a = Fr/m = friction*G*m / m = friction*G

#Now, after calculations are done, we need only to output data and draw graphs.

print("")        
print("Total breaking time in miliseconds (with reaction time): ", brakingTotal)
print("Braking time of car in miliseconds: ", brakingTimeRound)
print("Braking distance in meters: ", round(distanceList[brakingTotal],2))
        
plt.plot(timeList, speedList) #drawing of the graph,
plt.xlabel('Time (ms)') #naming the X axis of graph
plt.ylabel('Velocity (m/s)') #naming the Y axis of graph
plt.title("Velocity of car during braking") #adding title of graph
plt.grid() #adding grid to the graph
plt.savefig("velBrk.pdf", format="pdf", bbox_inches="tight") #saving .pdf file with graph
plt.show() #displaying of graph

plt.plot(timeList, distanceList)
plt.xlabel('Time (ms)')
plt.ylabel('Distance (m)')
plt.title("Distance of car during braking")
plt.grid()
plt.savefig("distBrk.pdf", format="pdf", bbox_inches="tight")
plt.show()
