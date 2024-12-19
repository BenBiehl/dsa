"""
Description:
    A collection of nodes that are linked to each other. Below is a command line application
    to mess around with a linked list.
Use Cases:
    Used to implement stacks and queues, graph adjacency list, when you
    need efficient insertions/deletions.
Time Complexity:
    Insertion at Beginning:     O(1)
    Insertion at End:           O(n)
    Insertion at Position:      O(n)
    Deletion at Beginning:      O(1)
    Deletion at End:            O(n)
    Deletion at Position:       O(n)
    Searching:                  O(n)
https://www.geeksforgeeks.org/python-linked-list/
"""

# Node Class
class Node:
    def __init__(self, data):
        self.data = data # Set data to passed in data
        self.next = None # When adding new node, make sure it points to nothing

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None # Before items are added, there will be no head

    def insertAtBegin(self, data):
        new_node = Node(data) # Initialize new node
        new_node.next = self.head # The current head will become the next node
        self.head = new_node # The new head will be the node we created

    def insertAtIndex(self, data, index):
        if index == 0: 
            self.insertAtBegin(data) # Just call insertAtBegin if user wants to insert at first index
            return
        
        position = 0 # Set initial position at beginning
        current_node = self.head # Set current node to the beginning/head
        while current_node is not None and position + 1 != index: # While current node isn't None and the next position isn't the desired index
            position += 1 # Increment the position
            current_node = current_node.next # Update current node to the next node

        if current_node is not None: # Check if current node doesn't point to None
            new_node = Node(data) # Initialize a new node
            new_node.next = current_node.next # Set its node to the next node
            current_node.next = new_node # Set current node next to the new node
        else:
            print("Index not present") # Index wasn't in range

    def insertAtEnd(self, data):
        new_node = Node(data) # Initialize new node
        if self.head is None: # If there isn't a head node already
            self.head = new_node # Set the new node to be the head node
            return

        current_node = self.head # Set current node to be the head
        while current_node.next: # Iterate through the linked list, until there isn't a next node
            current_node = current_node.next # Setting the current node to the next is how we iterate

        current_node.next = new_node # If there isn't a next node, set the next node to the new one

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")
    
    def remove_node(self, data):
        current_node = self.head

        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        print("Node with the given data not found")

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size
    
    def printLL(self):
        current_node = self.head
        while current_node:
            print(f"Current Linked List: {current_node.data}")
            current_node = current_node.next

# Main Loop
if __name__ == "__main__":
    llist = LinkedList()
    llist.insertAtEnd('1')
    llist.insertAtEnd('2')
    llist.insertAtEnd('3')
    llist.insertAtEnd('4')
    llist.insertAtEnd('5')
    while True:
        llist.printLL()
        print()
        print("Choose an option below to manipulate the linked list.")


    