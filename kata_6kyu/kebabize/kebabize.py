def kebabize(st):
    a = [i if i.islower() else "-" + i.lower() for i in st if i.islower() or i.isupper()]
    return "".join(a).lstrip("-")
