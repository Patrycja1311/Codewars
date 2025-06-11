def obfuscate(email):
    obfuscated = email.replace('.', ' [dot] ')
    obfuscated = obfuscated.replace('@', ' [at] ')
    return obfuscated
