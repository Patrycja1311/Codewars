def find_employees_role(name):
    parts = name.split()
    if len(parts) != 2:
        return "Does not work here!"
    first, last = parts
    for e in employees:
        if e['first_name'] == first and e['last_name'] == last:
            return e['role']
    return "Does not work here!"
