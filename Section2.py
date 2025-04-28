# Section 2: Linked Lists
# Detect and Remove Loop in Linked List:
# Implement an algorithm to detect if a loop exists in a linked list. If a loop is found, remove it.
# Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare method).
# the floyd's cycle use 2 pointers slow and fast if there is a loop at some point, the fast pointer will meet the slpw pointer inside the loop tell us that cycle is exist

# Define the Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #  define the Detect and remove function for the loop using Floyd's Cycle Detection (Tortoise and Hare)
    def detect_and_remove_loop(self):
        slow, fast = self.head, self.head

        # Detect if a loop exists
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                self.remove_loop(slow)
                return True
        return False

    # Remove the detected loop
    def remove_loop(self, loop_node):
        slow = self.head
        while slow != loop_node:
            slow, loop_node = slow.next, loop_node.next
        while loop_node.next != slow:
            loop_node = loop_node.next
        loop_node.next = None  # Remove the loop

    # Append new node to the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Create a loop for testing
    def create_loop(self, pos):
        loop_node = self.head
        count = 1
        while loop_node and loop_node.next:
            if count == pos:
                start_loop = loop_node
            loop_node = loop_node.next
            count += 1
        loop_node.next = start_loop  # Create the loop

# Example
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.create_loop(3)  # Create a loop starting at node 3
if ll.detect_and_remove_loop():
    print("Loop detected and removed.")
else:
    print("No loop found.")

# output: Loop detected and removed.



#Reverse a Linked List in Groups of K:
#Given a linked list, reverse it in groups of `k`.
#Implement the solution with **O(n) time complexity

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def reverse_in_groups(self, head, k):
        if not head:
            return None
        current, prev, count = head, None, 0

        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        if current:
            head.next = self.reverse_in_groups(current, k)

        return prev
    
    def print_list(self):
        temp = self.head
        count = 0
        while temp and count < 5:  # Limiting to print first 5 elements
            print(temp.data, end=" -> ")
            temp = temp.next
            count += 1
        if temp:  # If there are more elements, print "..."
            print("...")

# Test the code
ll = LinkedList()
for i in range(1, 11):  # Linked list from 1 to 10
    ll.append(i)

    print("Original Linked List:")
    ll.print_list()

    k = 2
    ll.head = ll.reverse_in_groups(ll.head, k)

    print(f"Linked List after reversing in groups of {k}:")
    ll.print_list()
