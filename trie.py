class Trie:
    def __init__(self):
        self.child = {}

    def insert(self, word):
        child = self.child
        for char in word:
            if char not in child:
                child[char] = {"freq": 1}
            else:
                child[char]["freq"] += 1
            child = child[char]
        child['is_end'] = True

    def prefix(self, word):
        prefix = []
        child = self.child
        for char in word:
            prefix.append(char)
            if child[char]["freq"] == 1:
                break
            child = child[char]
        return "".join(prefix)


class GenerateUniquePrefixes():
    def get_shortest_prefixes(self, word_list):
        t = Trie()
        for word in word_list:
            t.insert(word)
        result = []
        for word in word_list:
            result.append(t.prefix(word))
        return result
