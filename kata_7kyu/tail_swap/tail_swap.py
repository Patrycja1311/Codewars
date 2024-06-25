def tail_swap(strings):
    part1, part2 = [s.split(':') for s in strings]
    return [f"{part1[0]}:{part2[1]}", f"{part2[0]}:{part1[1]}"]
