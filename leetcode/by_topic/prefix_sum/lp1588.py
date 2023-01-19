class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        prefix = []

        for num in arr:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] + num)

        res = 0

        for i in range(len(prefix)):
            for j in range(i, len(prefix)):
                if i == j:
                    res += arr[i]
                else:
                    current_length = j - i + 1
                    if current_length % 2 == 1:
                        # if the current length is odd, then we add to the result
                        if i > 0:
                            res += prefix[j] - prefix[i - 1]
                        else:
                            res += prefix[j]

        return res
