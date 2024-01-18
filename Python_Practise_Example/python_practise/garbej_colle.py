import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create circular references
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

# Explicitly collect garbage
gc.collect()

# At this point, the circular references are no longer reachable, and the garbage collector will reclaim the memory
