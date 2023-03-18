class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str):
        if word == "$":
            self.children["$"] = ""
            return

        if word[0] not in self.children:
            self.children[word[0]] = Trie()

        if len(word) > 1:
            self.children[word[0]].insert(word[1:])
        else:
            self.children[word[0]].insert("$")

    def search(self, word):
        if len(word) == 0:
            if "$" in self.children:
                return True
            else:
                return False
        else:
            if word[0] in self.children:
                return self.children[word[0]].search(word[1:])
            else:
                return False

    def startsWith(self, prefix: str):
        if len(prefix) == 0:
            return True
        else:
            if prefix[0] in self.children:
                return self.children[prefix[0]].startsWith(prefix[1:])
            else:
                return False
