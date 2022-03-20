
def maxDifference(arr):
    l = r = 0
    maxD = 0

    while len(arr) > r:
        if arr[r] > arr[l]:
            maxD = max(arr[r] - arr[l], maxD)
        else:
            l = r
        r += 1

    return maxD





input = [9,2,5,3,10,4]
print(maxDifference(input))

input = [7,6,5,4,3,2,1]
print(maxDifference(input))
