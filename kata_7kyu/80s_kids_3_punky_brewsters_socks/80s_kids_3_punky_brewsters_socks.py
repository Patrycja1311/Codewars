def get_socks(name, socks):
    if name == 'Henry':
        seen = set()
        for sock in socks:
            if sock in seen:
                return [sock, sock]
            seen.add(sock)
        return []

    elif name == 'Punky':
        unique = list(set(socks))
        if len(unique) >= 2:
            return unique[:2]
        return []
