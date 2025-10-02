def top3(products, amounts, prices):
    revenues = [(p, a * pr, i) for i, (p, a, pr) in enumerate(zip(products, amounts, prices))]
    revenues.sort(key=lambda x: (-x[1], x[2]))
    return [p for p, _, _ in revenues[:3]]
