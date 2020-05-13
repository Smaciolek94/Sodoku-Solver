import numpy as np
import pandas as pd
import math

puzzle = pd.read_csv("C:\\Users\\Stvma\\Documents\\GitHub\\Sodoku Solver\\puzzle 3.csv",header=None)
puzzle = np.array(puzzle)

def box(i,j,puzzle,possib,p,q):
    if i in range(p,p+3):
        if j in range(q,q+3):
            for m in range(1,10):
                if m in puzzle[p:p+3,q:q+3]:
                    if m in possib:
                        possib.remove(m)
                        return(possib)

#remember exclusive bounds
for i in range(0,9): #we're going to do this over all rows
    for j in range(0,9): #then over all columns
        if math.isnan(puzzle[i,j]): #if the value is missing, create a possibility vector
                        #this will need to be a more compelex 3-d data structure
            possib = [1,2,3,4,5,6,7,8,9]
            for k in range(1,10): #checking rows for values
                if k in puzzle[i,]:
                    if k in possib:
                        possib.remove(k) #removing values in rows
            for l in range(1,10): #checking columns for values
                if l in puzzle[:,j]: #need the : for columns but not rows
                    if l in possib: # python throws an error if the number is not in the possible range
                        possib.remove(l)
            box(i,j,puzzle,possib,0,0)
            box(i,j,puzzle,possib,0,3)
            box(i,j,puzzle,possib,0,6)
            box(i,j,puzzle,possib,3,0)
            box(i,j,puzzle,possib,3,3)
            box(i,j,puzzle,possib,3,6)
            box(i,j,puzzle,possib,6,0)
            box(i,j,puzzle,possib,6,3)
            box(i,j,puzzle,possib,6,6)
            if len(possib) == 1:
                puzzle[i,j] = int(possib[0])
            