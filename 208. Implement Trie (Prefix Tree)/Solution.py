class Trie:
    def __init__(self):
        self.myDict = defaultdict(dict)

    def insert(self, word: str) -> None:
        pos = self.myDict
        for letter in word:
            if(letter not in pos):
                pos[letter] = {}
            pos = pos[letter]
        pos['end'] = {}           
        

    def search(self, word: str) -> bool:
        pos = self.myDict
        for letter in word:
            if(letter not in pos):
                return(False)
            pos = pos[letter]
        return(True if 'end' in pos else False)
        

    def startsWith(self, prefix: str) -> bool:
        pos = self.myDict
        for letter in prefix:
            if(letter not in pos):
                return(False)
            pos = pos[letter]
        return(True if pos else False)