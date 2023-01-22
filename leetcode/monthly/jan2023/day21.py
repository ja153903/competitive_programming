class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        # O(1) time
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        # if the sum of all indices we're going through
                        # happens to be the current length fo the string
                        # then we can consider its individual parts
                        if a + b + c + d == len(s):
                            a_as_int = int(s[:a])
                            b_as_int = int(s[a : a + b])
                            c_as_int = int(s[a + b : a + b + c])
                            d_as_int = int(s[a + b + c :])

                            # if all the parts are between 0 and 255
                            # and the length of their parts as a string
                            # is the length of the original string + 3 (for the dots)
                            # then we consider this a solution
                            if (
                                a_as_int <= 255
                                and b_as_int <= 255
                                and c_as_int <= 255
                                and d_as_int <= 255
                                and len(
                                    res := f"{a_as_int}.{b_as_int}.{c_as_int}.{d_as_int}"
                                )
                                == len(s) + 3
                            ):
                                result.append(res)

        return result
