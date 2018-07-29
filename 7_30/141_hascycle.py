def hasCycle(head):
    map = {}
    while (head):
        if id(head) in map:
            return True
        else:
            map[id(head)] = True
        head = head.next
    return False