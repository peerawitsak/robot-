def sortnum3(arrnum):# input form of list output :[sortnum,setmid]
    arr3 = []
    Setmid = 0
    same = [0,0,0]
    for i in arrnum:
        arr3.append(i)
        
    if arr3[0]<=3 and (arr3[1]>3 and arr3[1]<6) and arr3[2]>=6:
        same= [1,1,1]
        return(arr3,Setmid,same)
    elif arr3[0]<=3 and (arr3[2]>3 and arr3[2]<6) and arr3[1]>=6:
        same= [1,1,1]
        return(arr3,Setmid,same)
    elif arr3[1]<=3 and (arr3[2]>3 and arr3[2]<6) and arr3[0]>=6:
        same= [1,1,1]
        return(arr3,Setmid,same)
    elif arr3[1]<=3 and (arr3[0]>3 and arr3[0]<6) and arr3[2]>=6:
        same= [1,1,1]
        return(arr3,Setmid,same)
    elif arr3[2]<=3 and (arr3[0]>3 and arr3[0]<6) and arr3[1]>=6:
        same= [1,1,1]
        return(arr3,Setmid,same)
    elif arr3[2]<=3 and (arr3[1]>3 and arr3[1]<6) and arr3[0]>=6:
        same= [1,1,1]
        return(arr3,Setmid,same)
    else:
        # same > 1
        last_item = arr3.pop() 

        if last_item <4 : #last = 1 2 3
            if (arr3[0]==2 and arr3[1]==1) or (arr3[0]==3 and arr3[1]==1) or (arr3[0]==3 and arr3[1]==2):
                pass# frist mid = 2 1 ,3 1 ,3 2
            elif (arr3[0]==5 and arr3[1]==4) or (arr3[0]==4 and arr3[1]==5):
                pass#frist mid = 5 4, 4 5
            elif (arr3[0]>=6 and arr3[1]>=6):
                pass# 7 6 2 --> 2 7 6
            else:
                arr3.sort(reverse=False)
        
        elif last_item>5 :#last 6 7 8
            if (arr3[0]==1 and arr3[1]==2) or (arr3[0]==1 and arr3[1]==3) or (arr3[0]==2 and arr3[1]==3):
                pass#frist mid = 1 2 ,1 3 ,2 3
            elif (arr3[0]==5 and arr3[1]==4) or (arr3[0]==4 and arr3[1]==5) or (arr3[0]>=6 and arr3[1]>=6):
                pass#first mid 5 4, 4 5
            else :
                arr3.sort(reverse=True)
            
        else : #last item is 5 or 4 
            if arr3[0]<=3: #[frist = 1 2 3]
                if arr3[0]<arr3[1] :#[mid = 4 5 6 7 8]
                    if (arr3[0]==1 and arr3[1]==2) or (arr3[0]==1 and arr3[1]==3) or (arr3[0]==2 and arr3[1]==3):
                        pass#frist mid = 1 2 ,1 3 ,2 3
                    else:
                        arr3.sort(reverse=True)
                else:
                    pass
            elif arr3[0]>=6:# [frist = 6 7 8] Ex.4 6 5 ---> 5 4 6 , 5 6 4 --> 4 5 6
                if (arr3[1] == 4 or arr3[1]==5) :
                    arr3.sort(reverse=False)
                else:
                    pass # 8 7 4  --> 4 8 7
                
            else :
                pass
        arr3.insert(0,last_item)#last in frist out
        
        if arr3[1]!=arrnum[0]:#set mid
            Setmid = 1
        else : Setmid =0
        #print(arrnum,"\n",arr3,Setmid)
        for j in arr3 :
            if(j<=3):
                same[0]+=1
            elif(j>3 and j<6):
                same[1]+=1
            elif(j>=6):
                same[2]+=1
            else :
                pass
    
        return(arr3,Setmid,same) #return (arr,setmid) setmid = 1 is set

def sortnum2(arrnum):
    arr2 = []
    same = [0,0,0]
    setmid = 0
    for i in arrnum:
        arr2.append(i)
    last_item = arr2.pop() 
    arr2.insert(0,last_item)
    for j in arr2 :
            if(j<=3):
                same[0]+=1
            elif(j>3 and j<6):
                same[1]+=1
            elif(j>=6):
                same[2]+=1
            else :
                pass
    return(arr2,setmid,same)
    




 