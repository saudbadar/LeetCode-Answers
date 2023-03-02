class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars) == 1):
            return(1)

        def helperFunction(pos, word, count):
            nonlocal chars
            chars[pos], pos = word, pos + 1
            if(count > 1):
                val = str(count)
                for word in val:
                    chars[pos] = word
                    pos += 1
            return(pos)

        pos, lastWord, count = 0, chars[0], 1
        for word in chars[1:]:
            if(lastWord != word):
                pos = helperFunction(pos, lastWord, count)
                count, lastWord = 0, word
            count += 1
        pos = helperFunction(pos, lastWord, count)
        return(pos)