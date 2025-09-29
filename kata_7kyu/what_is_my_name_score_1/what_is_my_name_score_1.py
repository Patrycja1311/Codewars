from preloaded import alpha

def name_score(name):
    global alpha
    table = {ch:score for group,score in alpha.items() for ch in group}
    return {name: sum(table.get(c.upper(),0) for c in name if c != " ")}
