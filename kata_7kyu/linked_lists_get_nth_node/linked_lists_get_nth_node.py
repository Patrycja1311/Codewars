def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index or empty list")
    current = node
    for _ in range(index):
        if current.next is None:
            raise Exception("Index out of bounds")
        current = current.next
    return current
