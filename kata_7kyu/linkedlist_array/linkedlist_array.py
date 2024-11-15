def list_to_array(node):
    result = []
    while node is not None:
        result.append(node.value)
        node = node.next
    return result
