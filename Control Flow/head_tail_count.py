# Calculating Number of head and Tail in a range of 5 
import random

headCount=0 
tailCount=0

for i in range(5):
    num= random.randint(0,1)
    
    if num>0.5:
        print('Head')
        headCount+=1
    else:
        print('Tails')
        tailCount+=1

print("Head Counts=",headCount,"Tails Count=",tailCount)