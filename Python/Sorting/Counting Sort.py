# The CountingSort algorithm can only be used when the range of the values is known 
# and the range of values is small.

def CountingSort(arr,maxVal):
    bookKeepingArray = [0 for i in range(maxVal+1)]
    for v in arr:
        bookKeepingArray[v]+=1
    
    resultArr = []
    for i in range(len(bookKeepingArray)):
        resultArr += [i]*bookKeepingArray[i]

    return resultArr

if __name__ == "__main__":
    arr = [12,32,54,76,8,0]
    print(CountingSort(arr,100))
        