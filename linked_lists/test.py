from linked_list import Node, LinkedList


# Nodes instantiation
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

# Node in memory
# print(node_a)
# print(id(node_a))

# Create LL
ll = LinkedList()
print(ll)

# Insert at beginning
ll.insert_at_beginning(node_c)
print(ll)
ll.insert_at_beginning(node_b)
print(ll)
ll.insert_at_beginning(node_a)
print(ll)
ll.insert_at_beginning(node_d)
print(ll)

# Insert at end
ll.insert_at_end(node_e)
print(ll)

# Insert before
ll.insert_before('A', node_f)
print(ll)

node_g = Node('G')
ll.insert_before('D', node_g)
print(ll)

node_h = Node('H')
ll.insert_before('E', node_h)
print(ll)

# Delete a given node
ll.delete('E')
print(ll)
ll.delete('D')
print(ll)
ll.delete('C')
print(ll)

print('Activitie 1-------------------------------------------------------------------')

print(ll.search('G'))  # output: True

print('Activitie 2-------------------------------------------------------------------')


from linked_list import DoublyLinkedList

# Create a new playlist
playlist = DoublyLinkedList()

# Add some songs to the playlist
playlist.insert_beginning('1', 'Dakiti', 'Bad Bunny ft. Jhay Cortez', 'El Último Tour Del Mundo')
playlist.insert_beginning('2', 'Baila Baila Baila', 'Ozuna', 'Nibiru')
playlist.insert_beginning('3', 'Tusa', 'Karol G ft. Nicki Minaj', 'KG0516')
playlist.insert_beginning('4', 'La Modelo', 'Ozuna ft. Cardi B', 'Singles')
playlist.insert_beginning('5', 'Ella Quiere Beber', 'Anuel AA ft. Romeo Santos', 'Real Hasta La Muerte')

# Test the playlist methods
print('Playlist Length:', playlist.playlist_len())
playlist.play()
playlist.show_details()
playlist.next()
playlist.show_details()
playlist.previous()
playlist.show_details()
playlist.play_shuffle()
playlist.search_by_name('Tusa')
playlist.search_by_artist('Ozuna')
playlist.search_by_artist('Daddy Yankee')

