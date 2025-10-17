def pendulum(values):
    values=sorted(values);r=[values[0]]
    [r.append(x) if i%2 else r.insert(0,x) for i,x in enumerate(values[1:],1)]
    return r
