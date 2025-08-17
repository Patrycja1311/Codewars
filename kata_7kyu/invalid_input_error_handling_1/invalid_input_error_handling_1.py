def get_count(words=None):
    if not isinstance(words, str):
        return {"vowels": 0, "consonants": 0}

    words = words.lower()
    return {
        "vowels": sum(c in "aeiou" for c in words),
        "consonants": sum(c.isalpha() and c not in "aeiou" for c in words)
    }