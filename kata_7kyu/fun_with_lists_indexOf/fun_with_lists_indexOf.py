def index_of(head, value): 
    i = 0
    while head and head.data != value:
        head, i = head.next, i + 1
    return i if head else -1
