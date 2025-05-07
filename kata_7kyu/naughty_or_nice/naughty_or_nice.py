def get_nice_names(people):
    return [person['name'] for person in people if person.get('was_nice')]


def get_naughty_names(people):
    return [person['name'] for person in people if not person.get('was_nice')]
