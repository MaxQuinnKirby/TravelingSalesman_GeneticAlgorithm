########################################################
### NAME: Traveling Salesman Genetic Algorithm
### FILENAME: TS_V3.py
### VERSION: 3.0
### DESCRIPTION:
###     Solution to the Traveling Salesman problem using
###     a genetic algorithm. This is wrapped in a Function
###     so that the code can be used by the Driver_V1 code.
### AUTHOR: Max Quinn Kirby
### DATE LAST UPDATED: 9/1/2023
########################################################

import numpy as np
import copy

def TSP_GA(CityX,CityY,NumPop,NumGen,MutRate,NumCity): 
    ## User Defined Functions
    def Fitness(individual,CityX,CityY): # Determine the fitness of a specific individual
        Distance = 0
        # Remove Fitness from individual
        if len(individual) > NumCity:
            individual.pop(-1)
        indiv = []
        for i in range(0,len(individual)): indiv.append(int(individual[i]))
        for i in range(0,len(individual)-1):
            Distance += np.sqrt((CityY[indiv[i+1]]-CityY[indiv[i]])**2 + (CityX[indiv[i+1]]-CityX[indiv[i]])**2)
        return Distance

    def RandomSelect(Population,NumPop): # Randomly Select any Member from the population
        index = np.random.randint(0,NumPop-1)
        Selected = Population[index]
        return Selected

    def SingleIndexCrossover(Parent_Head,Parent_Tail,NumCity): # Crossover at a random index
        Parent_Head = copy.deepcopy(Parent_Head)
        Parent_Tail = copy.deepcopy(Parent_Tail)
        Parent_Head.pop(-1)
        Parent_Tail.pop(-1)
        index = np.random.randint(1,NumCity-1)
        Head = Parent_Head[0:index]
        for i in range(0,len(Head)): Parent_Tail.remove(Head[i])
        Tail = Parent_Tail
        return Head + Tail

    def SwapMutation(individual,MutRate): # Swap Mutation depending on rate
        chance = np.random.randint(0,100)
        if chance <= (MutRate*100): # random chance is less than rate
            # Swap Two Values
            Index1 = np.random.randint(0,NumCity)
            Index2 = np.random.randint(0,NumCity)
            while Index1 == Index2:
                Index2 = np.random.randint(0,NumCity)
            Val1 = individual[Index1]
            Val2 = individual[Index2]
            individual[Index1] = Val2
            individual[Index2] = Val1
            return individual
        return individual
 
    ## OVERLOOP to Compare Results to Brute Force
    AllSol = [] # Final Solution List
    for i in range(0,100):
        ## Initialize Population
        Population = []
        for i in range(0,NumPop): # For Each Individual
            StagArray = np.arange(0,NumCity)
            np.random.shuffle(StagArray)
            StagArray = list(np.copy(StagArray)) + [Fitness(StagArray,CityX,CityY)]
            Population.append(list(np.copy(StagArray)))

        ## Sort Population in ascending order
        Population.sort(key=lambda x:x[10])

        #### EVOLUTIONARY LOOP ####
        BestSol = Population[0]
        for i in range(0,NumGen): # Iterate for the number of generations

            ## Best Individual
            if Population[0][-1] < BestSol[-1]: # New Best Solution found
                BestSolGen = i # Generation in Which best sol was found
                BestSol = Population[0]
            
            ## Select Parents
            Parent1 = RandomSelect(Population,NumPop)
            Parent2 = RandomSelect(Population,NumPop)
            
            ## Perform Crossover
            OffspringA = SingleIndexCrossover(Parent1,Parent2,NumCity)
            OffspringB = SingleIndexCrossover(Parent2,Parent1,NumCity)

            ## Perform Mutation
            OffspringA = SwapMutation(OffspringA,MutRate)
            OffspringB = SwapMutation(OffspringB,MutRate)
            
            ## Evaluate Offspring
            OffspringA = OffspringA + [Fitness(OffspringA,CityX,CityY)]
            OffspringB = OffspringB + [Fitness(OffspringB,CityX,CityY)]

            ## Add Offspring to Population
            Population.append(OffspringA)
            Population.append(OffspringB)

            ## Sort Population
            Population.sort(key=lambda x:x[10])

            ## Remove Weakest
            Population.pop(-1)
            Population.pop(-1)

            ## Output Best of Generation
            BestGen = Population[0]

            ## Output Generation Information
            print('Gen: {} ---- Fitness: {}'.format(i,BestGen[-1]))
        
        ### Output Best Solution
        print('')
        print('')
        print('Best Solution: {}'.format(BestSol[-1]))
        
        ### Add Final Solution to Array 
        AllSol.append(BestSol)
    
    # Return All Solutions
    return AllSol, BestSol