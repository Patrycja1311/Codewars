def doubles(s):
    stack = []; [stack.pop() if stack and c == stack[-1] else stack.append(c) for c in s]; return ''.join(stack)
