class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ss = " ".join(sentence) + " "
        ans = 0
        for _ in range(rows): 
            ans += cols
            while ss[ans % len(ss)] != " ": ans -= 1
            ans += 1
        return ans // len(ss)
