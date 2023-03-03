from linked_list import LinkedList, Node
from stack import Stack

linked_list = LinkedList()
for i in range(10):
    node = Node(str(i))
    linked_list.insert_at_end(node)

print(linked_list)

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

reversed_list_with_stack = reverse_with_stack(linked_list)

linked_list.reverse_in_place()

print(reversed_list_with_stack)
print(linked_list)