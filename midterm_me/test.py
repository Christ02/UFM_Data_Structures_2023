from linked_list import LinkedList, Node
from stack import Stack

linked_list = LinkedList()

for i in range(10):
    node = Node(str(i))
    linked_list.insert_at_end(node)

print(linked_list)

def reverse_with_stack(linked_list):
    
    stack = Stack(10)
    
    # Put the nodes of the original list on the stack
    for node in linked_list:
        stack.push(node.data)
        
    reversed_list = LinkedList()
    
    # Create a new list with the nodes of the stack
    while not stack.top >-1:
        data = stack.pop()
        node = Node(data)
        reversed_list.insert_at_end(node)
        
    return reversed_list

# Reverse the linked list with a stack
reversed_list_with_stack = reverse_with_stack(linked_list)

#Reverse the original ll in place
linked_list.reverse_in_place()

#Compare them
print(reversed_list_with_stack)
print(linked_list)