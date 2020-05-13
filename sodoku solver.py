import numpy as np
import pandas as pd
import math

puzzle = pd.read_csv("C:\\Users\\Stvma\\Documents\\GitHub\\Sodoku Solver\\puzzle.csv",header=None)
puzzle = np.array(puzzle)

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
            if i in range(0,3): #boxes
                if j in range(0,3):
                    for m in range(1,10):
                        if m in puzzle[0:3,0:3]:
                            if m in possib:
                                possib.remove(m)
                elif j in range(3,6):
                    for m in range(1,10):
                        if m in puzzle[0:3,3:6]:
                            if m in possib:
                                possib.remove(m)
                elif j in range(6,9):
                    for m in range(1,10):
                        if m in puzzle[0:3,6:9]:
                            if m in possib:
                                possib.remove(m)
            if i in range(3,6): #boxes
                if j in range(0,3):
                    for m in range(1,10):
                        if m in puzzle[3:6,0:3]:
                            if m in possib:
                                possib.remove(m)
                elif j in range(3,6):
                    for m in range(1,10):
                        if m in puzzle[3:6,3:6]:
                            if m in possib:
                                possib.remove(m)
                elif j in range(6,9):
                    for m in range(1,10):
                        if m in puzzle[3:6,6:9]:
                            if m in possib:
                                possib.remove(m)   
            if i in range(6,9): #boxes
                if j in range(0,3):
                    for m in range(1,10):
                        if m in puzzle[6:9,0:3]:
                            if m in possib:
                                possib.remove(m)
                elif j in range(3,6):
                    for m in range(1,10):
                        if m in puzzle[6:9,3:6]:
                            if m in possib:
                                possib.remove(m)
                elif j in range(6,9):
                    for m in range(1,10):
                        if m in puzzle[6:9,6:9]:
                            if m in possib:
                                possib.remove(m)  
            if len(possib) == 1:
                puzzle[i,j] = int(possib[0])
            