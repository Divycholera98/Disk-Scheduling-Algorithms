import numpy as np
from matplotlib import pyplot as plt

print("------------------------------------------------")
print("-----------------Disk Scheduling----------------")
print("------------------------------------------------")

def fcfs(arr,n):
    ind=np.arange(1,len(arr)+1)
    sum=0
    for i in range(len(arr)-1):
        x=arr[i]
        y=arr[i+1]
        print(f' | {x} - {y} | = { abs(x-y) }') 
        sum+=abs(x-y)
    arr=arr[::-1]
    print(f" Head movement = {sum}")
    plt.plot(arr,ind,marker='o')
    plt.xlim(0,n)
    plt.title("fcfs")
    plt.show()

def sstf(arr,ind,n):
    arr1=np.copy(arr)
    arr1.sort()
    i=np.where(arr1==ind)
    i=i[0][0]
    j=i-1
    k=i+1
    arr2=[]
    arr2.append(ind)
    while(True):
        if(j>=0 and k<len(arr)):
            if(abs(arr1[j]-arr1[i])> abs(arr1[i]-arr1[k])):
                arr2.append(arr1[k])
                i=k
                k=k+1
            else :
                arr2.append(arr1[j])
                i=j
                j=j-1
        elif j>=0:
            arr2.append(arr1[j])
            i=j
            j=j-1
        elif k<len(arr):
            arr2.append(arr1[k])
            i=k
            k=k+1
        else :
            break
    sum=0
    for i in range(len(arr2)-1):
        x=arr2[i]
        y=arr2[i+1]
        print(f' | {x} - {y} | = { abs(x-y) }') 
        sum+=abs(x-y)
    print(f" Head movement = {sum}")
    arr2.reverse()
    ind=np.arange(1,len(arr2)+1)
    plt.plot(arr2,ind,marker='o')
    plt.title("sstf")
    plt.xlim(0,n)
    plt.show()
    
def scan(arr,ind,n):
    arr1=np.copy(arr)
    arr1.sort()
    i=np.where(arr1==ind)
    i=i[0][0]
    arr2=[]
    arr2.append(ind)
    if arr[0]<n-arr[-1]:
        for j in range(i):
            arr2.append(arr1[i-j-1])
        arr2.append(0)
        for j in range(i+1,len(arr1)):
            arr2.append(arr1[j])
    else:
        for j in range(i+1,len(arr1)):
            arr2.append(arr1[j])
        arr2.append(n)
        for j in range(i):
            arr2.append(arr1[i-j-1])
    sum=0
    for i in range(len(arr2)-1):
        x=arr2[i]
        y=arr2[i+1]
        print(f' | {x} - {y} | = { abs(x-y) }') 
        sum+=abs(x-y)
    print(f" Head movement = {sum}")
    arr2.reverse()
    ind=np.arange(1,len(arr2)+1)
    plt.plot(arr2,ind,marker='o')
    plt.xlim(0,n)
    plt.title("scan")
    plt.show()
        



def look(arr,ind,n):
    arr1=np.copy(arr)
    arr1.sort()
    i=np.where(arr1==ind)
    i=i[0][0]
    arr2=[]
    arr2.append(ind)
    if arr[0]<n-arr[-1]:
        for j in range(i):
            arr2.append(arr1[i-j-1])
        for j in range(i+1,len(arr1)):
            arr2.append(arr1[j])
    else:
        for j in range(i+1,len(arr1)):
            arr2.append(arr1[j])
        for j in range(i):
            arr2.append(arr1[i-j-1])
    sum=0
    for i in range(len(arr2)-1):
        x=arr2[i]
        y=arr2[i+1]
        print(f' | {x} - {y} | = { abs(x-y) }') 
        sum+=abs(x-y)
    print(f" Head movement = {sum}")
    arr2.reverse()
    ind=np.arange(1,len(arr2)+1)
    plt.plot(arr2,ind,marker='o')
    plt.xlim(0,n)
    plt.title("look")
    plt.show()
    

def cscan(arr,ind,n):
    arr1=np.copy(arr)
    arr1.sort()
    i=np.where(arr1==ind)
    i=i[0][0]
    arr2=[]
    arr2.append(ind)
    if arr[0]<n-arr[-1]:
        for j in range(i):
            arr2.append(arr1[i-j-1])
        arr2.append(0)
        arr2.append(n)
        for j in range(len(arr1)-i-1):
            arr2.append(arr1[len(arr1)-j-1])
    else:
        for j in range(len(arr1)-i-1):
            arr2.append(arr1[len(arr1)-j-1])
        arr2.append(n)
        arr2.append(0)
        for j in range(i):
            arr2.append(arr1[i-j-1])
        
    sum=0
    for i in range(len(arr2)-1):
        x=arr2[i]
        y=arr2[i+1]
        if(x==n and y==0) or (x==0 and y==n):
            continue
        print(f' | {x} - {y} | = { abs(x-y) }') 
        sum+=abs(x-y)
    arr=arr[::-1]
    print(f" Head movement = {sum}")
    arr2.reverse()
    ind=np.arange(1,len(arr2)+1)
    plt.plot(arr2,ind,marker='o')
    plt.xlim(0,n)
    plt.title("cscan")
    plt.show()

def clook (arr,ind,n):
    arr1=np.copy(arr)
    arr1.sort()
    i=np.where(arr1==ind)
    i=i[0][0]
    arr2=[]
    arr2.append(ind)
    if arr[0]<n-arr[-1]:
        for j in range(i):
            arr2.append(arr1[i-j-1])
        for j in range(len(arr1)-i-1):
            arr2.append(arr1[len(arr1)-j-1])
    else:
        for j in range(len(arr1)-i-1):
            arr2.append(arr1[len(arr1)-j-1])
        for j in range(i):
            arr2.append(arr1[i-j-1])
    sum=0
    for i in range(len(arr2)-1):
        x=arr2[i]
        y=arr2[i+1]
        print(f' | {x} - {y} | = { abs(x-y) }') 
        sum+=abs(x-y)
    print(f" Head movement = {sum}")
    arr2.reverse()
    ind=np.arange(1,len(arr2)+1)
    plt.plot(arr2,ind,marker='o')
    plt.xlim(0,n)
    plt.title("clook")
    plt.show()

ind=int(input("Enter head point  :  "))
n=int(input("Enter the size of disk  : "))
arr=input("Enter disk queue  : ").split()
arr.insert(0,ind)
arr=np.array(arr,dtype=int)
print("---------------------first come first serve----------------")
fcfs(arr,n)
print("---------------------shortest seek time first----------------")
sstf(arr,ind,n)
print("---------------------scan----------------")
scan(arr,ind,n)
print("---------------------cscan----------------")
cscan(arr,ind,n)
print("---------------------look----------------")
look(arr,ind,n)
print("---------------------clook----------------")
clook(arr,ind,n)
