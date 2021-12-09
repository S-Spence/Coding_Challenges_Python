
class TrieNode:
    def __inint__(self):
        # Each node has children the size of the alphabet
        self.children = [None] * 26
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, ch):
        return ord(ch)-ord("a")

    def insert(self, key):

        current = self.root
        length = len(key)

        for level in range(length):
            index = self.char_to_index(key[level])
