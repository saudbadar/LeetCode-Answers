class Solution:
    def originalDigits(self, s: str) -> str:
        counter, lst = Counter(s), []
        def remove(letter, value, word):
            nonlocal lst, counter
            length = counter[letter]
            for letter in word:
                counter[letter] -= length
                if(counter[letter] == 0):
                    del counter[letter]
            for i in range(length):
                lst.append(value)

    #one,three,four,five,seven,nine
        if("z" in counter):
            remove("z", "0", "zero")
        if("x" in counter):
            remove("x", "6", "six")
        if("g" in counter):
            remove("g", "8", "eight")
        if("w" in counter):
            remove("w", "2", "two")
        if("u" in counter):
            remove("u", "4", "four")
        if("f" in counter):
            remove("f", "5", "five")
        if("i" in counter):
            remove("i", "9", "nine")
        if("s" in counter):
            remove("s", "7", "seven")
        if("r" in counter):
            remove("r", "3", "three")
        if("o" in counter):
            remove("o", "1", "one")
        lst.sort()
        return("".join(lst))