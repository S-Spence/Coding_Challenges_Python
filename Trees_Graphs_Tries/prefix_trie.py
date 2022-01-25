import unittest
"""
Trie: A specialized tree used in searching. Most ofen with text. 
      In most cases, it will outperform bst's, hashtables, and most other data structres. 
      A trie has an empty root node as the start and letters are added.
      Each word must have a designated end. A boolean representing the at_end.
      Runtime to find a word O(len word). Space: O()

Problem: Implement a trie with insert, search, and starts with methods

Class Trie:
    void insert(string)
    bool search(string)
    bool starts_with(prefix)


"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str, current=None):
        """Insert a word into the trie. Time: O(len word), Space: O(len word)"""
        # set startin node to the root node if no node is passed in
        if current == None:
            current = self.root
        # If there are no more letters to add, set end to true
        if len(s) == 0:
            current.end = True
            return
        # If the current value is not in the trie, add it
        elif s[0] not in current.children:
            current.children[s[0]] = TrieNode()
            self.insert(s[1:], current.children[s[0]])
        else:
            # call insert by uddating current node to s[0] and slicing the string
            self.insert(s[1:], current.children[s[0]])

    def search(self, s: str, current=None) -> bool:
        """Search for a word in the trie. Time: O(len word), space: O(len word)"""
        # set current to the root if no node was passed in
        if current == None:
            current = self.root
        # If the word is empty and the node has an end, return true
        if len(s) == 0 and current.end:
            return True
        # If the word is empty, and there is no end to the word in the trie, return false
        elif len(s) == 0:
            return False
        # If the letter is not in the trie, return false
        elif s[0] not in current.children:
            return False
        else:
            return self.search(s[1:], current.children[s[0]])

    def starts_with(self, prefix: str, current=None) -> bool:
        """Find a prefix in a trie"""
        # set current value to the root node if it is empty
        if current == None:
            current = self.root

        if len(prefix) == 0:
            return True

        elif prefix[0] not in current.children:
            return False
        else:
            return self.starts_with(prefix[1:], current.children[prefix[0]])


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("tree")

    def test_1(self):

        self.assertTrue(self.trie.search("apple") == True)

    def test_2(self):

        self.assertTrue(self.trie.starts_with("tr") == True)

    def test_3(self):
        self.assertTrue(self.trie.starts_with("app") == True)

    def test_4(self):
        self.assertTrue(self.trie.search("camel") == False)

    def test_5(self):
        self.assertTrue(self.trie.starts_with("ch") == False)


# Run tests
if __name__ == "__main__":
    unittest.main()
