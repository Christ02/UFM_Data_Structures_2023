class Node:
    '''
    Node object.

    Args:
        data (str): string value to store in node

    Attributes:
        data (str): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, data: str):
        self.data = data
        self.next = None


    def __repr__(self):
        return '| Data: {} |'.format(self.data)


class LinkedList:
    '''
    Linked List object.

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
            nodes.append(node.data)

        nodes.append("NIL")
        return " --> ".join(nodes)


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


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


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
    
class Node_song:
    def __init__(self, id, name, artist, album):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.length = 0

    def insert_end(self, song_id: int, name: str, artist: str, album: str):
        new_node = Node_song(song_id, name, artist, album)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert_beginning(self, song_id: int, name: str, artist: str, album: str):
        new_node = Node_song(song_id, name, artist, album)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert_before(self, song_id: int, name: str, artist: str, album: str, ref_song: Node_song):
        if not ref_song:
            print("Reference song not found")
            return

        new_node = Node_song(song_id, name, artist, album)
        if ref_song.prev is None:
            new_node.next = ref_song
            ref_song.prev = new_node
            self.head = new_node
        else:
            new_node.prev = ref_song.prev
            ref_song.prev.next = new_node
            new_node.next = ref_song
            ref_song.prev = new_node
        self.length += 1

    def insert_after(self, song_id: int, name: str, artist: str, album: str, ref_song: Node_song):
        if not ref_song:
            print("Reference song not found")
            return

        new_node = Node_song(song_id, name, artist, album)
        if ref_song.next is None:
            new_node.prev = ref_song
            ref_song.next = new_node
            self.tail = new_node
        else:
            new_node.next = ref_song.next
            ref_song.next.prev = new_node
            new_node.prev = ref_song
            ref_song.next = new_node
        self.length += 1

    def delete(self, node_to_delete):
        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == node_to_delete:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == node_to_delete:
                previous_node.next = current_node.next
                return

            previous_node = current_node

    def search_by_name(self, name):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.name == name:
                return curr_node
            curr_node = curr_node.next
        print("Song not found")
        return None

    def search_by_artist(self, artist):
        found_songs = []
        curr_node = self.head
        while curr_node is not None:
            if curr_node.artist == artist:
                found_songs.append(curr_node)
            curr_node = curr_node.next
        if not found_songs:
            print("No songs found for artist")
        return found_songs

    def play(self):
        if self.head is None:
            print("Playlist is empty")
            return
        self.current = self.head

    def show_details(self):
        if self.current is None:
            print("No song is currently playing")
            return
        print(f"ID: {self.current.id}")
        print(f"Name: {self.current.name}")
        print(f"Artist: {self.current.artist}")
        print(f"Album: {self.current.album}")

    def next(self):
        if self.current is None:
            print("No song is currently playing")
            return
        if self.current.next is None:
            print("End of playlist")
            return
        self.current = self.current.next

    def previous(self):
        if self.current is None:
            print("No song is currently playing")
            return
        if self.current.prev is None:
            print("Beginning of playlist")
            return
        self.current = self.current.prev

    def playlist_len(self):
        return self.length

    def play_shuffle(self):
        if self.head is None:
            print("Playlist is empty")
            return
        import random
        rand_index = random.randint(0, self.length - 1)
        curr_index = 0
        curr_node = self.head
        while curr_node is not None:
            if curr_index == rand_index:
                self.current = curr_node
                return
            curr_node = curr_node.next
            curr_index += 1

