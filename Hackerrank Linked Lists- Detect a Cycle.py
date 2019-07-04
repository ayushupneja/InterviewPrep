"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    newNode = Node(3)
    current = head
    nexter = current.next
    while (current.next != None):
        if current.next == newNode:
            return True
        else:
            current.next = newNode
            current = nexter
            nexter = nexter.next
    return False
