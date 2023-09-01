########################################################
### NAME: Brute Force Traveling Salesman Solution
### FILENAME: BruteForceSol.py
### VERSION: 2.0
### DESCRIPTION:
###   Brute force a solution to the traveling salesman
###   problem in order to compare GA and Brute force
###   approaches. Version 2.0 Wraps in a function for 
###   importing into driver code. 
### AUTHOR: Max Quinn Kirby
### DATE LAST UPDATED: 8/31/2023
########################################################

import numpy as np
from itertools import permutations

def BruteForce(CityX,CityY): ## Brute Force Solution Function (Takes X and Y Locations of Cities)

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
  NumCity = len(CityX)

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

  return BestSolution, BestIndividual