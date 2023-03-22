from double_linked_list import DoublyLinkedList, Node_song
from memory_profiler import profile
import sys
import random

@profile
def insert_songs(ll):
    for i in range(7000):

        ll.insert_beginning('1', 'Dakiti', 'Bad Bunny ft. Jhay Cortez', 'El Último Tour Del Mundo')
        ll.insert_beginning('2', 'Baila Baila Baila', 'Ozuna', 'Nibiru')
        ll.insert_beginning('3', 'Tusa', 'Karol G ft. Nicki Minaj', 'KG0516')
        ll.insert_beginning('4', 'La Modelo', 'Ozuna ft. Cardi B', 'Singles')
        ll.insert_beginning('5', 'Ella Quiere Beber', 'Anuel AA ft. Romeo Santos', 'Real Hasta La Muerte')
            
    return ll


@profile
def traverse(ll):
    node = ll.head
    while node is not None:
        node = node.next
@profile
def traverse_with_pickle(ll):
    # cargar pickle
    pass


@profile
def main():
    ll = DoublyLinkedList()
    ll = insert_songs(ll)
    traverse(ll)
    # guardar en pickle

main()