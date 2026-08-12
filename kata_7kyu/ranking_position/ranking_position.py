def ranking(people):
    people.sort(key=lambda x: (-x["points"], x["name"]))
    for i, p in enumerate(people):
        p["position"] = next((j+1 for j, x in enumerate(people) if x["points"] == p["points"]), i+1)
    return people
