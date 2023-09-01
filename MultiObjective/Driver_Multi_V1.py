##############################################################################
### NAME: Driver Code for Multi Objective Traveling Salesman Problem Solution
### FILENAME: Driver_Multi_V1.py
### VERSION: 1.0
### DESCRIPTION: 
###
### AUTHOR: Max Quinn Kirby
### DATE LAST UPDATED: 9/1/2023
##############################################################################

import TSP_Multi_V1
import numpy as np



## Parameters
LocType = 'HardCode' # Type of Location Coordinates to Evaluate (HardCode or Variable)
SpeedType = 'HardCode' # Type of Speed to Evalute (HardCode or Variable)
NumCity = 10 # Number of Cities
NumPop = 100 # Number of Members in the intial population
MutRate = .2 # Twenty Percent Mutation Rate

## City Locations
if LocType == 'HardCode':
    CityX = [1, 4, 3, 8, 9, 7, 2, 2, 4, 9]
    CityY = [9, 6, 1, 4, 1, 3, 6, 3, 1, 5]
elif LocType == 'Variable':
    CityX = list(np.random.randint(0,np.random.randint(0,100),size=NumCity))
    CityY = list(np.random.randint(0,np.random.randint(0,100),size=NumCity))

## Speed Limits


## Plot Problem Statement