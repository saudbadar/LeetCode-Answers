class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, res, left, maxfreq = {}, 0, 0, 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfreq = max(maxfreq, count[s[right]])

            while((right - left + 1) - maxfreq > k):
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return(res)
        