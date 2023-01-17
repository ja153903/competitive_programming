class Solution:
    def minPartitions(self, n: str) -> int:
        """
        The seemingly odd trick here is that
        the largest number will dictate
        how many times we need to subtract anything
        """
        return int(max(list(n)))
