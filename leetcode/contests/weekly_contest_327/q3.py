from collections import Counter


class Solution:
    def isItPossible_TLE(self, word1: str, word2: str) -> bool:
        # TLE: Optimize
        as_list1 = list(word1)
        as_list2 = list(word2)

        for i in range(len(as_list1)):
            for j in range(len(as_list2)):
                as_list1[i], as_list2[j] = as_list2[j], as_list1[i]

                if len(set(as_list1)) == len(set(as_list2)):
                    return True

                as_list1[i], as_list2[j] = as_list2[j], as_list1[i]

        return False

    def isItPossible(self, word1: str, word2: str) -> bool:
        w1_cnt = Counter(word1)
        w2_cnt = Counter(word2)

        for i in range(97, 123):
            w1_ch = chr(i)

            for j in range(97, 123):
                w2_ch = chr(j)

                if w2_ch in w2_cnt and w1_ch in w1_cnt:
                    w1_cnt[w1_ch] -= 1
                    w2_cnt[w2_ch] -= 1

                    if w1_cnt[w1_ch] == 0:
                        del w1_cnt[w1_ch]

                    if w2_cnt[w2_ch] == 0:
                        del w2_cnt[w2_ch]

                    w1_cnt[w2_ch] += 1
                    w2_cnt[w1_ch] += 1

                    if len(w1_cnt) == len(w2_cnt):
                        return True

                    w1_cnt[w2_ch] -= 1
                    w2_cnt[w1_ch] -= 1

                    if w1_cnt[w2_ch] == 0:
                        del w1_cnt[w2_ch]

                    if w2_cnt[w1_ch] == 0:
                        del w2_cnt[w1_ch]

                    w1_cnt[w1_ch] += 1
                    w2_cnt[w2_ch] += 1

        return False
