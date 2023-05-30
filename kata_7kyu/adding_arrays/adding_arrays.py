def arr_adder(arr):
    words = []
    for i in range(len(arr[0])):
        word = ''
        for j in range(len(arr)):
            if arr[j][i] != '':
                word += arr[j][i]
            else:
                break
        words.append(word)
    return ' '.join(words)
