'''
Find the maximum subarray sum
'''


def extremelyNaive(arr):
    '''
    - TC = O(N**3)
    - SC = O(1)
    '''
    maxi = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum = 0
            for k in range(i, j):
                sum += arr[k]
            maxi = max(sum, maxi)
    return maxi


def naive(arr):
    '''
    - TC = O(N**2)
    - SC = O(1)
    '''
    maxi = 0
    for i in range(len(arr)):
        sum = arr[i]
        for j in range(i+1, len(arr)):
            sum += arr[j]
            maxi = max(sum, maxi)
    return maxi


def optimised_kadane(arr):
    '''
    - TC = O(N)
    - SC = O(1)
    '''
    sum = 0
    maxi = arr[0]
    for i in range(len(arr)):
        sum += arr[i]
        if sum < 0:
            sum = 0
        else:
            if maxi < sum:
                maxi = sum
    return maxi


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(optimised_kadane(arr))
