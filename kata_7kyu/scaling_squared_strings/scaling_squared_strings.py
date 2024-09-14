def scale(strng, k, v):
    return '\n'.join([(''.join(char * k for char in line)) for line in strng.split('\n') for _ in range(v)]) if strng else ""
