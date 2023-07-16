from collections import Counter


def count_vegetables(string):
    list_vege = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]
    list_string = string.split()
    list_vege_count = Counter(vege for vege in list_string if vege in list_vege)
    vegetables_count = sorted(list_vege_count.most_common(), key=lambda x: (x[1], x[0]), reverse=True)
    return [(x[1], x[0]) for x in vegetables_count]
