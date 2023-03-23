import pickle
import random
import sys
from double_linked_list import DoublyLinkedList, Node_song
from memory_profiler import profile
from data_persistence import pickle_object, unpickle_object



@profile
def insert_songs(ll):
    for i in range(2525):
        ll.insert_beginning('1', 'Dakiti', 'Bad Bunny ft. Jhay Cortez', 'El Último Tour Del Mundo')
        ll.insert_beginning('2', 'Baila Baila Baila', 'Ozuna', 'Nibiru')
        ll.insert_beginning('3', 'Tusa', 'Karol G ft. Nicki Minaj', 'KG0516')
        ll.insert_beginning('4', 'La Modelo', 'Ozuna ft. Cardi B', 'Singles')
        ll.insert_beginning('5', 'Ella Quiere Beber', 'Anuel AA ft. Romeo Santos', 'Real Hasta La Muerte')
    return ll


@profile
def traverse(ll):
    for i in ll:
        pass


@profile
def traverse_with_pickle():
    print(sys.getrecursionlimit())
    s_2 = unpickle_object('./data_persistence/saved_ll')
    for node in s_2:
        pass

    # cargar pickle
    pass

@profile
def main():
    ll = DoublyLinkedList()
    ll = insert_songs(ll)
    save_to_pickle(ll)
    traverse(ll)
    sys.setrecursionlimit(1000000)
    print(sys.getrecursionlimit())
    pickle_object(ll, './data_persistence/saved_ll')
    traverse_with_pickle()


if __name__ == "__main__":
    main()
