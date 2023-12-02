class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countOfChars, ret = Counter(chars), 0

        for word in words:
            tempCount, check = countOfChars.copy(), True
            for letter in word:
                if(letter in tempCount):
                    tempCount[letter] -= 1
                    if(tempCount[letter] == 0):
                        del tempCount[letter]
                else:
                    check = False
                    break
            if(check):
                ret += len(word)
        return(ret)