import heapq

# Using built-in heapq (list-based min-heap)
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 7)
print(heapq.heappop(min_heap))  # → 3

# Custom Max-Heap (trick: push negative values)
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
print(-heapq.heappop(max_heap))  # → 30
