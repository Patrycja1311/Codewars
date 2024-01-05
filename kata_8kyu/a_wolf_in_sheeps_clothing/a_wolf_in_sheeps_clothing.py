def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if 'wolf' == queue[-1] else f"Oi! Sheep number {len(queue)-queue.index('wolf')-1}! You are about to be eaten by a wolf!"
