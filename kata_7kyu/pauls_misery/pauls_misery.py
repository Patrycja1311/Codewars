def paul(x):
    score = sum({"kata": 5, "Petes kata": 10, "life": 0, "eating": 1}[i] for i in x)
    return ["Super happy!", "Happy!", "Sad!", "Miserable!"][(score >= 40) + (score >= 70) + (score >= 100)]
