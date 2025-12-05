from CodeSort import *
from arm import *
def lift():
    pass

def middle():
    pass

def right():
    pass

def checkway3(arr):
    Datasort = sortnum3(arr)
    if Datasort[0][0]<=3 :
        lift()
        
        
    elif Datasort[0][0]>3 and Datasort[0][0]<6 :
        middle()
    
    elif Datasort[0][0]>=6 :
        right()

def checkway2(arr):
    Datasort = sortnum2(arr)
    if Datasort[0][0]<=3 :
        lift()
        
    elif Datasort[0][0]>3 and Datasort[0][0]<6 :
        middle()
    
    elif Datasort[0][0]>=6 :
        right()
    









"""
caseN = 0
caseset = 0
for i in range(1,9):
    for j in range(1,9):
        for k in range(1,9):
            if i==j==k or i==j or i==k or k==j :
                pass
            else :
                arr = [i,j,k]
#                if j==5 and k==4 :
                if(sortnum3(arr)):
                        print(arr,"\n",sortnum3(arr)[0],sortnum3(arr)[1],sortnum3(arr)[2])
                        if(sortnum3(arr)[1]):
                            caseset +=1 
                        caseN += 1
                        print("case:",caseN)
                        print("--------")
                    #caseN += 1
                    #print("case:",caseN)
                    #print("--------")
                    
print("case:",caseN)
print("caseset:",caseset)

for i in range(1,9):
    for j in range(1,9):
        if i==j :
            pass
        else:
            arr =[i,j]
            print(arr)
            print(sortnum2(arr))
            caseN += 1 
            print(caseN)     
"""