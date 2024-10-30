import heapq
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    # count how many times a number occurs
    #key: the number
    #value: the frequency of the number
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    # create a heap
    # add the first k elements to the heap
    # if the heap is full, pop the smallest element and push the current element
    h = []
    heapq.heapify(h)

    for key, val in freq.items():
        if len(h) < k:
            heapq.heappush(h, (val, key))
        else:
            heapq.heappushpop(h, (val, key))

    # take the heap and add the elements to a list
    result = []
    for key, val in h:
        result.append(val)
    
    return result

topKFrequent([2,2,3,1,1,1], 2)