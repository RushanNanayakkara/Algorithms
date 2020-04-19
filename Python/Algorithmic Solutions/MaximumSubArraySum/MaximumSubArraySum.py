import sys

def maxSubArray(arr):
    best = -sys.maxsize
    sum = 0
    
    for i in range(len(arr)):
        sum = max(arr[i],sum+arr[i])    
        best = max(best,sum)
    
    return best

if __name__ == "__main__":
    arr = [1,23,5,67,-34,65,-53,0]
    print(maxSubArray(arr))