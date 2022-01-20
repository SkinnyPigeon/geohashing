class Trie:
    def __init__(self):
        """
        Initializes class instance with an empty dictionary \
        called child.

            Parameters:
                None

            Returns:
                None
        """
        self.child = {}

    def insert(self, geohash):
        """
        Generates a Trie graph. As each letter of each geohash is inserted, \
        it is checked against the keys in the current layer of the graph. \
        If the key already exists, it continues down the existing path. \
        If the key does not exist, it adds the key and begins a new path.

            Parameters:
                geohash (str): The geohash that is to be mapped into the Trie \
                structure

            Returns:
                None
        """
        child = self.child
        for char in geohash:
            if char not in child:
                child[char] = {"freq": 1}
            else:
                child[char]["freq"] += 1
            child = child[char]
        child['is_end'] = True

    def prefix(self, geohash):
        """
        Traverses the Trie structure looking for the first instance \
        that the character frequency is 1. At this point it has reached \
        a unique prefix. If no unique prefix is found, it returns the \
        full geohash it has checked.

            Parameters:
                geohash (str): The geohash whose unique prefix is being \
                searched for

            Returns:
                prefix (str): Either the unique prefix for the given geohash \
                or the complete geohash if no unique prefix is found
        """
        prefix = []
        child = self.child
        for char in geohash:
            prefix.append(char)
            if child[char]["freq"] == 1:
                break
            child = child[char]
        return "".join(prefix)


class GenerateUniquePrefixes():
    def get_shortest_prefixes(self, geohashes):
        """
        Creates the Trie class instance, inserts them into the Trie \
        structure, then searches for their unique prefixes.

            Parameters:
                geohashes (list): The list of geohashes whose unique \
                prefixes are being searched for

            Returns:
                prefixes (list): The list of unique (where available) \
                geohashes
        """
        t = Trie()
        for geohash in geohashes:
            t.insert(geohash)
        prefixes = []
        for geohash in geohashes:
            prefixes.append(t.prefix(geohash))
        return prefixes
