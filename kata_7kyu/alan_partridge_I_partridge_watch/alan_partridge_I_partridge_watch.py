def part(arr):
    related_terms = {
        "Partridge", "PearTree", "Chat", "Dan", "Toblerone",
        "Lynn", "AlphaPapa", "Nomad"
    }
    count = sum(1 for term in arr if term in related_terms)
    return "Mine's a Pint" + "!" * count if count else "Lynn, I've pierced my foot on a spike!!"
