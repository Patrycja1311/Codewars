def stringify(node):
    return " -> ".join(str(n.data) for n in iter_list(node)) + " -> None" if node else "None"


def iter_list(node):
    while node:
        yield node
        node = node.next
