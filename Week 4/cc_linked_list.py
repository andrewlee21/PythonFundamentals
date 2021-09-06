class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("head Node created:", self.head.value)
            return
# 'Traversing list to get to tail node'
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next

        temp_node.next = new_node
        print("Appended new Node with value:", temp_node.next.value)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head Node created:", value)
            return
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head
            print("Prepended new Head Node ith value:", self.head.value)
            print("Node following head is", old_head.value)
        return


llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")

