def is_monotone(heights):
    return all(heights[i] <= heights[i + 1] for i in range(len(heights) - 1))
