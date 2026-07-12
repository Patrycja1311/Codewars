def chore_assignment(chores):
    chores.sort()
    return sorted(chores[i] + chores[-i-1] for i in range(len(chores)//2))
