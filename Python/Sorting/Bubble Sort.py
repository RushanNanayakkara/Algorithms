def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


if __name__ == "__main__":
    arr = [2,5,7,3,5,7,0]
    print(BubbleSort(arr))
