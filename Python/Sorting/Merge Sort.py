def MergeSort(arr):
    if(len(arr)<=1):
        return arr
    mid = len(arr)//2
    subArr1 = arr[0:mid]
    subArr2 = arr[mid:len(arr)]
    sorted1 = MergeSort(subArr1)
    sorted2 = MergeSort(subArr2)

    itr1 = 0
    itr2 = 0
    for i in range(len(arr)):
        if(itr1<len(sorted1) and (itr2==len(sorted2) or sorted1[itr1]<sorted2[itr2])):
            arr[i] = sorted1[itr1]
            itr1+=1
        else:
            arr[i] = sorted2[itr2]
            itr2+=1
    
    return arr

if __name__ == "__main__":
    arr = [12,3,34,657,8768,79,8]
    print(MergeSort(arr))