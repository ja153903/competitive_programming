class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for ch in s:
            if not result or result[-1] != ch:
                result.append(ch)
            elif result:
                result.pop()

        return "".join(result)
