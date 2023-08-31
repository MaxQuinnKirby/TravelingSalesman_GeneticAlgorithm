########################################################
### NAME: Traveling Salesman Genetic Algorithm
### FILENAME: TS_V2.py
### VERSION: 2.0
### DESCRIPTION:
###     Solution to the Traveling Salesman problem using
###     a genetic algorithm. Uses Single Index Crossover,
###     Random parent selection, and a swap mutation.
### AUTHOR: Max Quinn Kirby
### DATE LAST UPDATED: 8/29/2023
########################################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def Fitness(individual,CityX,CityY): # Determine the Fitness of a given individual
    Distance = 0
    for i in range(0,len(individual)-1):
        Distance += np.sqrt((CityY[individual[i+1]]-CityY[individual[i]])**2 + (CityX[individual[i+1]]-CityX[individual[i]])**2)
    return Distance

def RandomSelect(Population,NumPop): # Randomly Selects a Parent for Reproduction
    ## Random Index for what to select
    index = random.randint(0,NumPop-1)
    ## Pull Parent's Information
    array = Population.iloc[index].to_numpy()
    return array

def SingleIndexX(Parent_Head,Parent_Tail,NumCity): # Uses a single random indicie to split the head and tail
    ## Generate Index to be Split at 
    index = np.random.randint(0,NumCity-1)
    ## Find the head of the first Parent
    Head = Parent_Head[0:index]
    ## Covert to Lists
    Parent_Head = list(Parent_Head)
    Parent_Tail = list(Parent_Tail)
    ## Maintain Fesability with Crossover
    for i in range(0,len(Head)): Parent_Tail.remove(Head[i])
    ## Find Tail by Remainder of Parent2
    Tail = Parent_Tail
    ## Generate Offspring
    Offspring = Head + Tail
    return Offspring

# def SwapMutation(Offspring, NumCity): # Performs Swap Mutation



### Hardcode (x,y) Locations of Cities
CityX = [1, 4, 3, 8, 9, 7, 2, 2, 4, 9]
CityY = [9, 6, 1, 4, 1, 3, 6, 3, 1, 5]

## Parameters
NumPop = 100 # Number of Members in a population
NumCity = 10 # Number of Cities
NumGen = 100 # Number of Generations
SelectionType = 'Random' # Type of Selection to be used
MutRate = 0.2 # 20 Percent change of mutation
CrossoverType = 'SingleIndex' # Type of crossover to be used

# Plot Cities on Map 
for i in range(0, len(CityX)):
    plt.plot(CityX[i],CityY[i],marker="o",markeredgecolor='red',markerfacecolor='green')
    plt.text(CityX[i],CityY[i],'{}'.format(i))
plt.title('Traveling Salesman Problem -- Problem Statement')
plt.xlabel('X--Location')
plt.ylabel('Y--Location')
plt.show()

## Initalize Starting Population
dict = {
    'City1': [],'City2': [], 'City3': [], 'City4': [],'City5': [],
    'City6': [],'City7': [],'City8': [],'City9': [],'City10': [], 
    'Fitness': []
}
Population = pd.DataFrame(dict)
for i in range(0,NumPop):
    StagArray = np.arange(0,NumCity)
    np.random.shuffle(StagArray)
    Population.loc[len(Population.index)] = np.copy(StagArray)

print(Population)

## Evolutionary Loops
for i in range(0,NumGen):
    ## Perform Selection
    if SelectionType == 'Random':
        Parent1 = RandomSelect(Population,NumPop)
        Parent2 = RandomSelect(Population,NumPop)
        while np.array_equiv(Parent1,Parent2):
            Parent2 = RandomSelect(Population,NumPop)
    
    ## Perform Crossover
    if CrossoverType == 'SingleIndex':
        OffspringA = SingleIndexX(Parent_Head=Parent1,Parent_Tail=Parent2,NumCity=NumCity) # Parent 1 is the Head
        OffspringB = SingleIndexX(Parent_Head=Parent2,Parent_Tail=Parent1,NumCity=NumCity) # Parent 2 is the Head
        while np.array_equiv(OffspringA,OffspringB): # Repeat crossover if children are the same
            OffspringB = SingleIndexX(Parent2,Parent1,NumCity)

    ## Perform Mutation
    
    ## Merge Offsprings with Population
    Population.loc[len(Population.index)] = np.copy(OffspringA) + Fitness(OffspringA,CityX,CityY)
    Population.loc[len(Population.index)] = np.copy(OffspringB) + Fitness(OffspringB,CityX,CityY)

    print(Population)
    break
    ## Evaluate Population
    # Generate Fitness Level for Each Member in Population


    ## Remove Weakest

