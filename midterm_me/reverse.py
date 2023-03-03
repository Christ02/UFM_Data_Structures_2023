from stack import Stack
from linked_list import LinkedList, Node

class Reverse:

    def reverse_with_stack(llist):
        '''
        Utiliza una instancia de la clase Stack para invertir el orden de una lista
        simplemente ligada.

        Args:
            llist (LinkedList): lista a invertir

        Returns:
            LinkedList: nueva lista invertida
        '''

        # Crear nueva lista ligada
        reversed_llist = LinkedList()

        # Crear pila
        stack = Stack()

        # Poner los nodos de la lista original en la pila
        for node in llist:
            stack.push(node)

        # Crear nueva lista con los nodos de la pila
        while not stack.is_empty():
            node = stack.pop()
            reversed_llist.insert_at_end(Node(node.data))

        return reversed_llist