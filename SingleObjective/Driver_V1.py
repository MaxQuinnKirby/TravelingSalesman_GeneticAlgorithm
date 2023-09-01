########################################################
### NAME: Genetic Algorithm Driver Code
### FILENAME: Driver_V1.py
### VERSION: 1.0
### DESCRIPTION:
###     Driver Code for the Genetic Algorithm Solutions.
###     Driver code is used for V3 of GA Solutions. This
###     also runs a brute force solution, V2.
### AUTHOR: Max Quinn Kirby
### DATE LAST UPDATED: 9/1/2023
########################################################

import BruteForceSol_V2 as BFS
import numpy as np
import TS_V3 as TS

### Parameters
NumCity = 10
NumPop = 100 # Population Amount
NumGen = 1000 # Number of Generations
MutRate = .20 # 20 Percent Change of mutation

### Define CityX and CityY
CityX = list(np.random.randint(0,np.random.randint(0,100),size=NumCity))
CityY = list(np.random.randint(0,np.random.randint(0,100),size=NumCity))

### Find Brute Force Solution
BestSolution, BestIndividual = BFS.BruteForce(CityX,CityY)

### Output Brute Force Solution
print('**** Brute Force Solution ****')
print('Best Solution: {}'.format(BestSolution))

### Find Genetic Algorithm Solution
AllSol, BestSol = TS.TSP_GA(CityX,CityY,NumPop,NumGen,MutRate,NumCity)

### Output Genetic Algorithm Solution
print('**** Genetic Algorithm ****')
print('Best Solution: {}'.format(min(AllSol)))