class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        sorted_words = sorted(words, key=lambda w: tuple(order.index(ch) for ch in w))
        return words == sorted_words
