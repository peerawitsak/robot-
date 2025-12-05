# 1 2 3   6 7 8 
# 1 3 6 --> 6 , 3 1
# 6 2 8 --> 8 6 ,2
#caseN = 0
arr = []

def Starksort3(): #sort of input 3 times output is array
    #print(arr)
    last_item = arr.pop()
    if last_item <4:
        arr.sort(reverse=False)
    elif last_item >5:
        arr.sort(reverse=True)

    elif last_item == 4 or last_item == 5 :
        if arr[0]<=3:
            if arr[0]<arr[1]:
                arr.sort(reverse=True)
            else :
                pass
        else:
            pass
    else :
        pass
    arr.insert(0,last_item)
    #print(arr)
    return(arr) 

def Starksort2(): #sort of input 2 times output is array
    #print(arr)
    last_item = arr.pop()
    arr.insert(0,last_item)
    #print(arr)
    return(arr) 

def InputList3(x): # input 3 times in array
    x = int(x)
    arr.append(x)
    if len(arr)==3 :
        return Starksort3()



def InputList2(x): #input 2 times in array
    x = int(x)
    arr.append(x)
    if len(arr)==2 :
        return Starksort2()
    


# เปลี่ยนเลข ลำดับใส่เข้า  last in frist out 
InputList3(6)
InputList3(1)
print(InputList3(7))


InputList2(4)
print(InputList2(5))


"""
for i in range(1,9):
    for j in range(1,9):
        for k in range(1,9):
            if i==j==k or i==j or i==k or k==j :
                pass
            else :
                InputList3(i)
                InputList3(j)
                InputList3(k)
                arr = []
                caseN += 1
                print("case:",caseN)
                print("--------")
"""