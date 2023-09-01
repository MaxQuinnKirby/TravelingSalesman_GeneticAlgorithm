This is a working solution to the traveling salesman problem using genetic alogorithms.

********************************************************************************************************
PROBLEM STATEMENTS:

Single Objective Problem Statement
- Given the (X,Y) Locations of a number of cities, find the shortest distance route, stopping at each 
  only one time. 

Multi Objective Problem Statement 
- Given the (X,Y) Locations of a number of cities and the speed limits between each city. Each city has a road
  between every other city. Find the Pareto Front for minimzing time caused by speed limits and distance. Distance
  can be regarded as in miles with the speed limits being in miles per hour.

********************************************************************************************************
There are two main directories: 
1) SingleObjective 
  -- DESCRIPTION: Solutions of Single Objective Optimization for the Traveling Salesman Problem
2) MultiObjective
  -- DESCRIPTION: Solutions of Multi Objective Optimization for the Traveling Salesman Problem

********************************************************************************************************
\SingleObjective
"testsheet_kirby.py"
--This is temporary file that is used as a command line of sorts to test groups of code

"BruteForceSol.py"
--This is a brute force solution to the program which can be used as baseline to compare outputs.

"BruteForceSol_V2.py"
--Version 2 of the brute force solution to the traveling salesman problem.

"Driver_V1.py"
-- Driver Code for V3 of traveling salesman solution and V2 of Brute Force Solution

"TS_V1.py" 
-- Uses Pandas as population datastructure
-- Ran into to many issues with the concatenation of new rows where adhering to the pandas structure 
  was causing more issues than it was worth.
-- abandoned

"TS_V2.py"
-- Uses list of lists as population datastructure
-- Finished and Working
-- Uses Random Selection for Parents (non-biased)
-- Uses a Swap Mutation
-- Uses a Single Index Crossover to generate offsprings
-- Runs 100x and Compares against brute force solution with outputs showing the average 
   accuracy of the results, precision, and best results obtained.

"TS_V3.py"
-- Works off Version 2
-- Wraps Version 2 into a function to be called by the Driver Code


********************************************************************************************************
\Multi-Objective
"TSP_Multi_V1.py" -- Version 1 of the Multi-Objective Traveling Salesman solution
"Driver_Multi_V1.py" -- Version 1 of the Driver Code for the Multi-Objective Traveling Salesman Solution