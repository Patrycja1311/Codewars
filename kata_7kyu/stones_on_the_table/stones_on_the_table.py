def solution(stones):
    count = 0
    for i in range(1, len(stones)):
        if stones[i] == stones[i - 1]:
            count += 1
    return count
