def user_contacts(data):
    return {user[0]: user[1] if len(user) > 1 else None for user in data}
