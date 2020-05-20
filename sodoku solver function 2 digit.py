import numpy as np
import pandas as pd
import math

puzzle = pd.read_csv("C:\\Users\\Stvma\\Documents\\GitHub\\Sodoku Solver\\puzzle 4.csv",header=None)
puzzle = np.array(puzzle)
possible2 = np.zeros((9,9,2))

def box(i,j,puzzle,possib,p,q):
    if i in range(p,p+3):
        if j in range(q,q+3):
            for m in range(1,10):
                if m in puzzle[p:p+3,q:q+3]:
                    if m in possib:
                        possib.remove(m)
    return(possib)

def box2(i,j,puzzle,possib,possible2,p,q):
    if i in range(p,p+3):
        if j in range(q,q+3):
            for m in range(1,10):
                if np.count_nonzero(possible2[p:p+3,q:q+3,:]==m) == 2:
                    if m not in possible2[i,j,:]:
                        if m in possib:
                            possib.remove(m)
    return(possib)

#remember exclusive bounds
counter = 0
while np.isnan(puzzle).any() == True: #itereate this so long as there are missing values
    #this loop creates the possible variable, and fills in any spots with one correct answer
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
                possib = box(i,j,puzzle,possib,0,0)
                possib = box(i,j,puzzle,possib,0,3)
                possib = box(i,j,puzzle,possib,0,6)
                possib = box(i,j,puzzle,possib,3,0)
                possib = box(i,j,puzzle,possib,3,3)
                possib = box(i,j,puzzle,possib,3,6)
                possib = box(i,j,puzzle,possib,6,0)
                possib = box(i,j,puzzle,possib,6,3)
                possib = box(i,j,puzzle,possib,6,6)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])
                    #break #9 tries with, 4 without, 5 without 2-digit
                if len(possib) == 2: #creating a possibility 3-d array
                    possible2[i,j,:] = possib
                    #possible2[i,j,1] = possib[1]    
                #if a number appears twice in a row or column that has 2 possibilities, then it can be removed, 
                #as long as it is not one of the possibilities for the cell
                for m in range(1,10):
                    if np.count_nonzero(possible2[i,:,:]==m) == 2:#counts the number of times 
                        if m not in possible2[i,j,:]: #super important not to delete it if it in in the cell
                            if m in possib:
                                possib.remove(m)
                for n in range(1,10):
                    if np.count_nonzero(possible2[:,j,:]==n) == 2:
                        if n not in possible2[i,j,:]:
                            if n in possib:
                                possib.remove(n)
                            box(i,j,puzzle,possib,0,0)
                possib = box2(i,j,puzzle,possib,possible2,0,0)
                possib = box2(i,j,puzzle,possib,possible2,0,3)
                possib = box2(i,j,puzzle,possib,possible2,0,6)
                possib = box2(i,j,puzzle,possib,possible2,3,0)
                possib = box2(i,j,puzzle,possib,possible2,3,3)
                possib = box2(i,j,puzzle,possib,possible2,3,6)
                possib = box2(i,j,puzzle,possib,possible2,6,0)
                possib = box2(i,j,puzzle,possib,possible2,6,3)
                possib = box2(i,j,puzzle,possib,possible2,6,6)
                if len(possib) == 1: #if just one possibility remains, setting it and clearing matrix
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0] 
    counter = counter + 1
    if counter > 100:
        break #breaks if not solved withing 10 runs
#need to be able to update as numbers are filled in