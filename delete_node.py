#Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

def delete_node(node_to_delete):

    next_node  = node_to_delete #deleting basically means skipping that node to the next one

    if next_node:

        #if the next_node exists, then we assign the node to be deleted value to the next node and also the same with the pointer
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next.next

    else:
        # incase we are at the last node.
        raise Exception("Can't delete last node with this approach")

