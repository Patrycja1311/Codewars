def missing(nums, s):
    letters = [c for c in s if c != ' ']
    return ''.join(letters[i] for i in sorted(nums)).lower() if max(nums) < len(letters) else "No mission today"
