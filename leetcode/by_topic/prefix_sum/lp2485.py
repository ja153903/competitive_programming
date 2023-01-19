class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = []

        for i in range(1, n + 1):
            if i == 1:
                prefix.append(i)
            else:
                prefix.append(prefix[-1] + i)

        for i, num in enumerate(prefix):
            if i == 0:
                if num == prefix[-1]:
                    return i + 1
            elif num == prefix[-1] - prefix[i - 1]:
                return i + 1

        return -1
