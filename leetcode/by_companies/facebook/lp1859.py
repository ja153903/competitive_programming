class Solution:
    def sortSentence(self, s: str) -> str:
        words = sorted([(int(word[-1]), word[:-1]) for word in s.split()], key=lambda tup: tup[0])
        return " ".join([word[1] for word in words])
