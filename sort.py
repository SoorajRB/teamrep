
def bubbleSort(alist):      #using bubblesort
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum): 
            if alist[i]>alist[i+1]:
                temp = alist[i]      #creating a new variable called temp
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17]
bubbleSort(alist)
print(alist)



#Aparna 
