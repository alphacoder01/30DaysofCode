'''
Find repeating and missing number in an unsorted array of size n
where a[i] belongs to [1,n]
'''


def simpleApproach(arr):
    '''
    Based on hashmap based frequency counting
    TC - O(N) + O(N) = O(2N)
    SC - O(N)
    '''
    r = m = -1

    hashmap = [0]*(len(arr) + 1)
    for i in arr:
        hashmap[i] += 1

    for i in range(len(hashmap)):
        if hashmap[i] == 0:
            m = i
        elif hashmap[i] == 2:
            r = i

    return r, m


def optimalApproach1(arr):
    '''
    sum of first n num. = (n*(n+1))/2
     "   "  "    n*n " = (n*(n+1)*(2n+1)/6)
    subtract the above 2 equations

    - TC = O(N)
    - SC = O(1)
    '''
    s = s2 = 0
    n = len(arr)
    for i in arr:
        s += i
        s2 += i*i

    S = (n*(n+1)) // 2
    S2 = (n*(n+1)*(2*n+1)//6)

    A = S2 - s2
    B = S - s

    m = B + (A//B - B)//2
    r = (A//B - B)//2

    return r, m


arr = [4, 3, 6, 2, 1, 1]
r, m = optimalApproach1(arr)
print(f"Repeating element = {r} and Missing element = {m}")
