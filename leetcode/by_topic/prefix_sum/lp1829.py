class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        prefix_xor = []

        for num in nums:
            if not prefix_xor:
                prefix_xor.append(num)
            else:
                prefix_xor.append(prefix_xor[-1] ^ num)

        max_1bits = 2**maximumBit - 1

        result = [max_1bits ^ bit for bit in prefix_xor]

        result.reverse()

        return result
