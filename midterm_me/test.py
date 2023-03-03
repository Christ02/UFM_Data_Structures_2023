from linked_list import LinkedList, Node

from stack import Stack

def reverse_with_stack(linked_list):
    stack = Stack()
    for node in linked_list:
        stack.push(node.data)
    reversed_list = LinkedList()
    while not stack.is_empty():
        data = stack.pop()
        node = Node(data)
        reversed_list.insert_at_end(node)
    return reversed_list


# Create a linked list and add 10 elements to it
linked_list = LinkedList()
for i in range(10):
    node = Node(str(i))
    linked_list.insert_at_end(node)

# Print the original linked list
print(linked_list)

# Reverse the linked list with a stack
reversed_list_with_stack = reverse_with_stack(linked_list)

# Reverse the original linked list in place
linked_list.reverse_in_place()

# Print both lists to compare them
print(reversed_list_with_stack)
print(linked_list)