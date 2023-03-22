import pickle
import random
import sys
from double_linked_list import DoublyLinkedList, Node_song
from memory_profiler import profile


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
    for i in ll:
        pass


def save_to_pickle(ll):
    with open('songs.pkl', 'wb') as f:
        pickle.dump(ll, f)


def load_from_pickle():
    with open('songs.pkl', 'rb') as f:
        return pickle.load(f)


@profile
def traverse_with_pickle():
    ll = load_from_pickle()
    for i in ll:
        pass


@profile
def main():
    ll = DoublyLinkedList()
    ll = insert_songs(ll)
    save_to_pickle(ll)
    traverse(ll)
    traverse_with_pickle()


if __name__ == "__main__":
    main()
