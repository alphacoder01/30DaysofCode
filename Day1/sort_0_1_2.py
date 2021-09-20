'''
Sort an array of 0’s 1’s 2’s without using extra space or sorting algo
'''


def goodApproach(arr):
    '''
    Uses counting sort 
    - TC = O(2N) - requires 2 passes
    - SC = O(1)
    '''
    zeroCount = oneCount = twoCount = 0
    for element in arr:
        if element == 0:
            zeroCount += 1
        elif element == 1:
            oneCount += 1
        else:
            twoCount += 1

    for j in range(len(arr)):
        if zeroCount != 0:
            arr[j] = 0
            zeroCount -= 1
        elif zeroCount == 0 and oneCount != 0:
            arr[j] = 1
            oneCount -= 1
        elif zeroCount == 0 and oneCount == 0 and twoCount != 0:
            arr[j] = 2
            twoCount -= 1


def bestApproach(arr):
    '''
    Modification of Dutch National Flag Algorithm
    - Uses 3 pointers (high,mid,low)
    - Makes all the elements left of low as 0 and right of high as 2
    - TC = O(N) - requires single pass
    - SC = O(1)
    '''

    low = mid = 0
    high = len(arr) - 1

    while(mid <= high):
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [0, 0, 1, 2, 1, 0, 2, 2, 1, 2]
bestApproach(arr)
print(arr)
