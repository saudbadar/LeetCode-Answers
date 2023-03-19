class WordDictionary:

    def __init__(self):
        self.nestedDict = defaultdict(dict)
        

    def addWord(self, word: str) -> None:
        currDict = self.nestedDict
        for letter in word:
            if(letter not in currDict):
                currDict[letter] = {}
            currDict = currDict[letter]
        if('~' not in currDict):
            currDict['~'] = {}
        

    def search(self, word: str) -> bool:
        def dotSearch(currDict, wordLeft):
            if(not wordLeft):
                if('~' in currDict):
                    return(True)
                return(False)
            
            if(wordLeft[0] == '.'):
                for checkDict in currDict.values():
                    if(dotSearch(checkDict, wordLeft[1:])):
                        return(True)
            elif(wordLeft[0] in currDict):
                if(dotSearch(currDict[wordLeft[0]], wordLeft[1:])):
                    return(True)
            else:
                return(False)
        return(dotSearch(self.nestedDict, word))