########################################################
### NAME: Brute Force Traveling Salesman Solution
### FILENAME: BruteForceSol.py
### VERSION: 1.0
### DESCRIPTION:
###   Brute force a solution to the traveling salesman
###   problem in order to compare GA and Brute force
###   approaches.
### AUTHOR: Max Quinn Kirby
### DATE LAST UPDATED: 8/31/2023
########################################################
import numpy as np
from itertools import permutations

## User Defined Functions
def factorial(n): # Finds the factorial of 
  return 1 if (n==1 or n==0) else n*factorial(n-1)

def Fitness(individual,CityX,CityY): # Determine the fitness of an individual
  ## Fitness Evaluation
  Distance = 0
  for i in range(0,NumCity-1):
    D_T = np.sqrt((CityX[individual[i+1]] - CityX[individual[i]])**2 + (CityY[individual[i+1]]-CityY[individual[i]]))
    Distance += D_T
  return Distance

## Parameters
NumCity = 10

## Hardcode (x,y) Locations of Cities
CityX = [1, 4, 3, 8, 9, 7, 2, 2, 4, 9]
CityY = [9, 6, 1, 4, 1, 3, 6, 3, 1, 5]

## Define Solution Space
numSol = factorial(NumCity)
StagArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SolutionSpace = permutations(StagArray)
print(numSol)

## Brute Force Solution
count = 0
fitList = []
BestSolution = 100000000
for i in list(SolutionSpace):
  count += 1

  ## Fitness Function
  Distance = 0
  for j in range(0,NumCity-1):
    X_Loc = (CityX[i[j+1]] - CityX[i[j]])**2
    Y_Loc = (CityY[i[j+1]] - CityY[i[j]])**2
    D_T = np.sqrt(X_Loc + Y_Loc)
    Distance += D_T
  
  ## Append to End of fitList
  fitList.append(Distance)

  ## Check Best Solution 
  if Distance < BestSolution: # Better solution found
    BestSolution = Distance
    BestIndividual = i

 
  print('Iteration: {} ----- Fitness: {}'.format(count,Distance))

## Index of Best
BestIndex = fitList.index(min(fitList))

## Solution Output
print('')
print('')
print('Best Individual Index: {}'.format(BestIndex))
print('Best Solution: {}'.format(BestSolution))
print('Best Individual: {}'.format(BestIndividual))


###### OUTPUT HISTORY ######
## PARAMETERS
# NumCity = 10
# CityX = [1, 4, 3, 8, 9, 7, 2, 2, 4, 9]
# CityY = [9, 6, 1, 4, 1, 3, 6, 3, 1, 5]
## RUN 8/31/2023 -- 4:35pm
# Best Individual Index: 1792029
# Best Solution: 22.437875313342335
# Best Individual: (4, 9, 3, 5, 8, 2, 7, 1, 6, 0)