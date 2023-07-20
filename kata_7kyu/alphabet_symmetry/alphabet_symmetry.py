def solve(arr):
    def alpha_position(char):
        return ord(char.lower()) - ord('a') + 1

    return [sum(alpha_position(char) == i + 1 for i, char in enumerate(ar)) for ar in arr]
