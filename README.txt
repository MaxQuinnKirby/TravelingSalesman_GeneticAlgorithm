This is a working solution to the traveling salesman problem using genetic alogorithms.

Files and their information is described below:
"testsheet_kirby.py" -- this is temporary file that is used as a command line of sorts to test groups of code
"BruteForceSol.py" -- this is a brute force solution to the program which can be used as baseline to compare outputs.
"TS_V1" -- Version 1 of the traveling salesman solution
"TS_V2" -- Version 2 of the traveling salesman solution
"TS_V3" -- Version 3 of the traveling salesman solution

Version 1
-- Uses Pandas as population datastructure
-- Ran into to many issues with the concatenation of new rows where adhering to the pandas structure 
  was causing more issues than it was worth.
-- abandoned

Version 2
-- Uses list of lists as population datastructure
-- Finished and Working
-- Uses Random Selection for Parents (non-biased)
-- Uses a Swap Mutation
-- Uses a Single Index Crossover to generate offsprings
-- Runs 100x and Compares against brute force solution with outputs showing the average 
   accuracy of the results, precision, and best results obtained.

Version 3
-- Works off V2 using list of list as population datastructure