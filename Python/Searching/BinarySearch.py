import math


#By shrinking the range of search
def BinarySearchMethod1(arr,val):
    a=0
    b=len(arr)-1
    mid = round(a+b/2)
    while(a<b):
        if(arr[mid]==val):
            return mid
        if(arr[mid]>val):
            b = mid
        else:
            a = mid
        mid = round(a+b/2)
    return -1

# Step half of the unsearched area if val is in that half. Repeat until
# all searched or element found
def BinarySearchMethod2(arr,val):
    step = len(arr)//2
    i = 0
    while(step>0):
        if(arr[i+step]==val):
            return i+step
        if(arr[i+step]<val):
            i += step
        else:
            step= step//2
    return -1


if __name__ == "__main__":
    arr = [1,23,5,5657,8,6,23]
    arr.sort()
    print(BinarySearchMethod2(arr,6))