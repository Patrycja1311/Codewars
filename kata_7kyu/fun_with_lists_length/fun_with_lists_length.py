class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
