from urllib.parse import quote


def generate_link(user):
    encoded_user = quote(user)
    return f"http://www.codewars.com/users/{encoded_user}"
