def vowel_one(s):
    vovels = ['a','e','i','o','u']
    return ''.join(['1' if elem in vovels else '0' for elem in s.lower() ])


if __name__ == '__main__':
    vowel_one('vowelOne')
    vowel_one('123, arou')