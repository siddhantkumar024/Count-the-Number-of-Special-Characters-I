class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        c=0
        for word in s:
            if word.lower() in s and word.upper() in s:
                c+=1
                print(word,c)
        return c//2

        
