class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    ##push a new node to the front of the list
    def push(self, value):
        self.top = Node(value, self.top)

    ##remove as node from the front of the list
    def pop(self):
        if self.top is None:
            return None

        node =self.top
        self.top = self.top.next

        else: item = self.top.item
            self.top = self.top.next
        return item



        

