def last_index_of(head, search_val):
    index, last_index = 0, -1
    while head:
        if head.data == search_val:
            last_index = index
        head = head.next
        index += 1
    return last_index
