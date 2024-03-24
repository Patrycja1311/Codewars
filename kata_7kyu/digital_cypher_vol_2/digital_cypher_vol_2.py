def decode(code, key):
    key_str = str(key)
    decoded = ''
    for i in range(len(code)):
        decoded += chr((code[i] - int(key_str[i % len(key_str)])) + ord('a') - 1)
    return decoded
