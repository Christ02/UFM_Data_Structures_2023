class Node:
    '''
    Node object for Doubly Non-Circular Linked List.


    Args:
        song_id (int): ID of the song
        name (str): Name of the song
        artist (str): Name of the artist
        album (str): Name of the album

    Attributes:
        song_id (int): ID of the song
        name (str): Name of the song
        artist (str): Name of the artist
        album (str): Name of the album
        prev (Node): pointer to previous node in list
        next (Node): pointer to next node in list
    '''
    
    def __init__(self,  song_id: int, name: str, artist: str, album: str):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.album = album
        self.prev = None
        self.next = None


    def __repr__(self):
        return '| ID: {} | Name: {} | Artist: {} | Album: {} |'.format(
            self.song_id, self.name, self.artist, self.album)


class DoublyLinkedList:
    '''
    Doubly Non-Circular Linked List object.

    Args:
        None

    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(str(node))

        nodes.append("NIL")
        return " <--> ".join(nodes)


    def traverse(self):
        '''
        Navigates every node in the list.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            for current_node in self:
                pass

            current_node.next = new_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.

        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.

        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))
        
    def search(self, reference_node: str):
        '''
        Searches for a node with a specific value in the linked list.

        Args:
            target_node (str): the value of the node to search for

        Returns:
            bool: True if the node is found, False otherwise
        '''
        if self.start is None:
            print('Empty linked list...')
            return False

        for node in self:
            if node.data == reference_node:
                print(f'{reference_node} found in the linked list.')
                return True

        print(f'{reference_node} not found in the linked list.')
        return False
