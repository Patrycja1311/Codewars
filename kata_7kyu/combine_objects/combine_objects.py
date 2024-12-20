def combine(*objs):
    return {key: sum(obj.get(key, 0) for obj in objs) for obj in objs for key in obj}
