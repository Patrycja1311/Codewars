def last_chair(n):
    import heapq
    heap = []
    heapq.heappush(heap, (-(n - 1), 1, n))
    for _ in range(n - 1):
        dist, l, r = heapq.heappop(heap)
        if l == 1:
            seat = 1
        elif r == n:
            seat = n
        else:
            seat = (l + r) // 2
        if l <= seat - 1:
            new_dist = (seat - 1 - l)
            heapq.heappush(heap, (-new_dist, l, seat - 1))
        if seat + 1 <= r:
            new_dist = (r - (seat + 1))
            heapq.heappush(heap, (-new_dist, seat + 1, r))
    dist, l, r = heapq.heappop(heap)
    if l == 1:
        return 1
    elif r == n:
        return n
    else:
        return (l + r) // 2

