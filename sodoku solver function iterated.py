import numpy as np
import pandas as pd
import math

#puzzle = pd.read_csv("C:\\Users\\Stvma\\Documents\\GitHub\\Sodoku Solver\\puzzle 2.csv",header=None)
puzzle = pd.read_csv("C:\\Users\\smaci\\Documents\\GitHub\\Sodoku-Solver\\puzzle 5.csv",header=None)
puzzle = np.array(puzzle)
print(puzzle)

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
    
def box3(i,j,puzzle,possib,possible3,p,q):
    if i in range(p,p+3):
        if j in range(q,q+3):
            for m in range(1,10):
                if np.count_nonzero(possible3[p:p+3,q:q+3,:]==m) == 3:
                    if m not in possible3[i,j,:]:
                        if m in possib:
                            possib.remove(m)
    return(possib)
    
def box4(i,j,puzzle,possib,possible4,p,q):
    if i in range(p,p+3):
        if j in range(q,q+3):
            for m in range(1,10):
                if np.count_nonzero(possible4[p:p+3,q:q+3,:]==m) == 4:
                    if m not in possible4[i,j,:]:
                        if m in possib:
                            possib.remove(m)
    return(possib)
    
def one(i,j,puzzle,possib):
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
    return(possib)
  
def two(i,j,puzzle,possib,possible2):
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
    possib = box2(i,j,puzzle,possib,possible2,0,0)
    possib = box2(i,j,puzzle,possib,possible2,0,3)
    possib = box2(i,j,puzzle,possib,possible2,0,6)
    possib = box2(i,j,puzzle,possib,possible2,3,0)
    possib = box2(i,j,puzzle,possib,possible2,3,3)
    possib = box2(i,j,puzzle,possib,possible2,3,6)
    possib = box2(i,j,puzzle,possib,possible2,6,0)
    possib = box2(i,j,puzzle,possib,possible2,6,3)
    possib = box2(i,j,puzzle,possib,possible2,6,6)
    return(possib)
    
def three(i,j,puzzle,possib,possible3):
    for o in range(1,10):
        if np.count_nonzero(possible3[i,:,:]==o) == 3:#counts the number of times 
            if o not in possible3[i,j,:]: #super important not to delete it if it in in the cell
                if o in possib:
                    possib.remove(o)
    for p in range(1,10):
        if np.count_nonzero(possible3[:,j,:]==p) == 3:
            if p not in possible3[i,j,:]:
                if p in possib:
                    possib.remove(p)
    possib = box3(i,j,puzzle,possib,possible3,0,0)
    possib = box3(i,j,puzzle,possib,possible3,0,3)
    possib = box3(i,j,puzzle,possib,possible3,0,6)
    possib = box3(i,j,puzzle,possib,possible3,3,0)
    possib = box3(i,j,puzzle,possib,possible3,3,3)
    possib = box3(i,j,puzzle,possib,possible3,3,6)
    possib = box3(i,j,puzzle,possib,possible3,6,0)
    possib = box3(i,j,puzzle,possib,possible3,6,3)
    possib = box3(i,j,puzzle,possib,possible3,6,6)
    return(possib)

def four(i,j,puzzle,possib,possible4):
    for o in range(1,10):
        if np.count_nonzero(possible4[i,:,:]==o) == 4:
            if o not in possible4[i,j,:]:
                if o in possib:
                    possib.remove(o)
    for p in range(1,10):
        if np.count_nonzero(possible4[:,j,:]==p) == 4:
            if p not in possible4[i,j,:]:
                if p in possib:
                    possib.remove(p)
    possib = box4(i,j,puzzle,possib,possible4,0,0)
    possib = box4(i,j,puzzle,possib,possible4,0,3)
    possib = box4(i,j,puzzle,possib,possible4,0,6)
    possib = box4(i,j,puzzle,possib,possible4,3,0)
    possib = box4(i,j,puzzle,possib,possible4,3,3)
    possib = box4(i,j,puzzle,possib,possible4,3,6)
    possib = box4(i,j,puzzle,possib,possible4,6,0)
    possib = box4(i,j,puzzle,possib,possible4,6,3)
    possib = box4(i,j,puzzle,possib,possible4,6,6)
    return(possib)
    
counter1 = 0
while np.isnan(puzzle).any() == True:
    for i in range(0,9): #we're going to do this over all rows
        for j in range(0,9): #then over all columns
            if math.isnan(puzzle[i,j]): #if the value is missing, create a possibility vector
                possib = [1,2,3,4,5,6,7,8,9]
                one(i,j,puzzle,possib)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])
    counter1 = counter1 + 1
    if counter1 > 20:
        break 

possible2 = np.zeros((9,9,2))
counter2 = 0
while np.isnan(puzzle).any() == True:
    for i in range(0,9): #we're going to do this over all rows
        for j in range(0,9): #then over all columns
            if math.isnan(puzzle[i,j]): #if the value is missing, create a possibility vector
                possib = [1,2,3,4,5,6,7,8,9]
                one(i,j,puzzle,possib)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])    
                if len(possib) == 2:
                    possible2[i,j,:] = possib
                two(i,j,puzzle,possib,possible2)
                if len(possib) == 1: #if it's now down to one possibility, set it to that, clear the 2-digit matrix
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0]
    counter2 = counter2 + 1
    if counter2 > 20:
        break                     

possible2 = np.zeros((9,9,2))
possible3 = np.zeros((9,9,3))
counter3 = 0
while np.isnan(puzzle).any() == True: #itereate this so long as there are missing values
    #this loop creates the possible variable, and fills in any spots with one correct answer    
    for i in range(0,9): #we're going to do this over all rows
        for j in range(0,9): #then over all columns
            if math.isnan(puzzle[i,j]): #if the value is missing, create a possibility vector
                possib = [1,2,3,4,5,6,7,8,9]
                one(i,j,puzzle,possib)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])
                if len(possib) == 2:
                    possible2[i,j,:] = possib
                if len(possib) == 3:
                    possible3[i,j,:] = possib
                two(i,j,puzzle,possib,possible2)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0]
                    possible3[i,j,:] = [0,0,0]
                if len(possib) == 2:
                    possible2[i,j,:] = possib
                    possible3[i,j,:] = [0,0,0]
                if len(possib) == 3:
                    possible3[i,j,:] = possib
                three(i,j,puzzle,possib,possible3)
                if len(possib) == 1: #if one possibility remains, set it, clear matrices
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0]
                    possible3[i,j,:] = [0,0,0]
                if len(possib) == 2: #if it's now decreased to 2 possibilities, set the 2 digit possibility matrix
                    possible2[i,j,:] = possib
                    possible3[i,j,:] = [0,0,0] #clear the 3 digit possibility matrix
                if len(possib) == 3:
                    possible3[i,j,:] = possib
    counter3 = counter3 + 1
    if counter3 > 20:
        break 

possible2 = np.zeros((9,9,2))
possible3 = np.zeros((9,9,3))
possible4 = np.zeros((9,9,4))
counter4 = 0
while np.isnan(puzzle).any() == True: 
    for i in range(0,9):
        for j in range(0,9):
            if math.isnan(puzzle[i,j]): 
                possib = [1,2,3,4,5,6,7,8,9]
                one(i,j,puzzle,possib)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])
                if len(possib) == 2:
                    possible2[i,j,:] = possib
                if len(possib) == 3:
                    possible3[i,j,:] = possib
                if len(possib) == 4:
                    possible4[i,j,:] = possib
                two(i,j,puzzle,possib,possible2)
                if len(possib) == 1:
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0]
                    possible3[i,j,:] = [0,0,0]
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 2:
                    possible2[i,j,:] = possib
                    possible3[i,j,:] = [0,0,0]
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 3:
                    possible3[i,j,:] = possib
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 4:
                    possible4[i,j,:] = possib
                three(i,j,puzzle,possib,possible3)
                if len(possib) == 1: 
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0]
                    possible3[i,j,:] = [0,0,0]
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 2: 
                    possible2[i,j,:] = possib
                    possible3[i,j,:] = [0,0,0] 
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 3:
                    possible3[i,j,:] = possib
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 4:
                    possible4[i,j,:] = possib
                four(i,j,puzzle,possib,possible4)
                if len(possib) == 1: 
                    puzzle[i,j] = int(possib[0])
                    possible2[i,j,:] = [0,0]
                    possible3[i,j,:] = [0,0,0]
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 2: 
                    possible2[i,j,:] = possib
                    possible3[i,j,:] = [0,0,0] 
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 3:
                    possible3[i,j,:] = possib
                    possible4[i,j,:] = [0,0,0,0]
                if len(possib) == 4:
                    possible4[i,j,:] = possib
    counter4 = counter4 + 1
    if counter4 > 20:
        break 
print("page break")
print(puzzle)