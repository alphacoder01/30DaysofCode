'''
The question is to merge 2 sorted arrays without using extra space
'''
import math


def mergeNormal(a1, a2):
    '''
    Normal merge of 2 sorted arrs.
    - TC = O(n+m)
    - SC = O(n+m)
    '''

    i = j = 0
    lengthA1, lengthA2 = len(a1), len(a2)
    merged = []

    while(i < lengthA1 and j < lengthA2):
        if a1[i] < a2[j]:
            merged.append(a1[i])
            i += 1
        elif a2[j] < a1[i]:
            merged.append(a2[j])
            j += 1
        else:
            merged.extend([a1[i], a2[j]])
            i += 1
            j += 1

    if i < lengthA1:
        merged.extend(a1[i:])
    elif j < lengthA2:
        merged.extend(a2[j:])
    return merged


def mergeUsingInsert(a1, a2):
    '''
    Swap elements between a1 and a2 and keep a2 sorted
    - TC = O(n*m)
    - SC = O(1)
    - See explanation in notebook.
    '''
    if len(a1) >= len(a2):
        bigarr = a1
        smallarr = a2
    else:
        bigarr = a2
        smallarr = a1

    i = 0
    while(i < len(bigarr)):
        if bigarr[i] > smallarr[0]:
            bigarr[i], smallarr[0] = smallarr[0], bigarr[i]
            i += 1

            if smallarr[0] > smallarr[-1]:
                smallarr[0], smallarr[-1] = smallarr[-1], smallarr[0]
            else:
                for j in range(1, len(smallarr)):
                    if smallarr[j] >= smallarr[0]:
                        idx = j
                        break
                smallarr = smallarr[:idx] + [smallarr[0]] + smallarr[idx:]

        elif bigarr[i] <= smallarr[0]:
            i += 1


# def GAP(a1, a2):
#     '''
#     Most optimised:
#     - TC = O(NlogN)
#     - SC = O(1)
#     '''

#     l1, l2 = len(a1), len(a2)
#     gap = math.ceil((l1+l2)/2)
#     t = gap
#     p1 = 0
#     p2 = t + p1
#     while(1):
#         a2Flag = 0
#         print(f"Gap = {t} and p1 = {p1}, p2 = {p2}")
#         if t == 1 and p2 > l2:
#             break

#         if p2 > l1:
#             p2 -= l1
#             a2Flag = 1
#             print(f"p2 > l1...so new p2 = {p2}")

#         secondEle = (a2[p2] if a2Flag else a1[p2])
#         if a1[p1] < secondEle:
#             p1 += 1
#             if a2Flag:
#                 p2 += l1 + 1
#             else:
#                 p2 += 1
#             print(f"No swap, p1 = {p1}, p2 = {p2}")

#         elif a1[p1] > secondEle:
#             a1[p1], secondEle = secondEle, a1[p1]
#             p1 += 1
#             if a2Flag:
#                 p2 += 1+l1
#             else:
#                 p2 += 1
#             print(f"Element Swapped p1 = {p1}, p2 ={p2}")

#         if p2 > l2:
#             t = t // 2
#             print(f"New Gap = {t}")


a1 = [1, 5, 7, 8, 9]
a2 = [2, 3]
mergeUsingInsert(a1, a2)

print(a1, a2)
