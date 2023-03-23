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
        
    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

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
    