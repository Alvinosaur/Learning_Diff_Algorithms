import heapq

def connect_ropes(ropes):
    heapq.heapify(ropes)
    while len(ropes) > 1:
        val1 = heapq.heappop(ropes)
        val2 = heapq.heappop(ropes)
        heapq.heappush(ropes, val1 + val2)
    return ropes[0]