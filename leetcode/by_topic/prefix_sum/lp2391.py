class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        travel_prefix = [0] + []
        for i, t in enumerate(travel):
            if i == 0:
                travel_prefix.append(t)
            else:
                travel_prefix.append(travel_prefix[-1] + t)

        # count of characters throughout
        g, p, m = 0, 0, 0

        # reach of variable
        gi, pi, mi = 0, 0, 0

        for i, garb in enumerate(garbage):
            moved_g, moved_p, moved_m = False, False, False

            for ch in garb:
                match ch:
                    case "G":
                        moved_g = True
                        g += 1
                    case "P":
                        moved_p = True
                        p += 1
                    case _:
                        moved_m = True
                        m += 1

            if moved_g:
                gi = i

            if moved_p:
                pi = i

            if moved_m:
                mi = i

        res = g + p + m
        res += sum(travel_prefix[i] for i in [gi, pi, mi])

        return res
