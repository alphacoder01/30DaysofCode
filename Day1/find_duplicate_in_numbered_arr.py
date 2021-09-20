'''
[1,5,3,2,5,4] 
N = 6
* The important point is elements are 1,N
and array is N+1 size
duplicate element = 5
'''


def usingSorting(arr):
    '''
    - TC = O(NlogN)
    - SC = O(1)
    '''
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            return arr[i]
    return -1


def usingExtraArray(arr):
    '''
    - TC = O(N)
    - SC = O(N) for extra array
    '''
    extra = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        extra[arr[i]] += 1
        if extra[arr[i]] > 1:
            return arr[i]
    return -1


arr = [1, 5, 3, 2, 5, 4]
(usingExtraArray(arr))
