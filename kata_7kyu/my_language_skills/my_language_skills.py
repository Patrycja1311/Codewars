def my_languages(results):
    return [k for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True) if v >= 60]
