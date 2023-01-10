class Solution:
    def minimumHealth(self, damage: list[int], armor: int) -> int:
        """
        You are playing a game that has n levels numbered from 0 to n - 1.
        You are given a 0-indexed integer array damage where damage[i] is
        the amount of health you will lose to complete the ith level.

        You are also given an integer armor.
        You may use your armor ability at most once during the game on any
        level which will protect you from at most armor damage.

        You must complete the levels in order and your health must be greater than 0 at all times to beat the game.

        Return the minimum health you need to start with to beat the game.

        Constraints:
            * n == damage.length
            * 1 <= n <= 105
            * 0 <= damage[i] <= 105
            * 0 <= armor <= 105

        damage = [2,7,4,3], armor = 4
        prefix = [2, 9, 13, 16]

        damage = [3, 3, 3], armor = 0
        prefix = [3, 6, 9]

        damage = [2,5,3,4], armor = 7
        [2, 7, 10, 14], armor = 7

        max_damage = 5, we can cover up to 7
        armor - max_damage < 0 ? armor : max_damage
        """
        ps = [0] * len(damage)
        max_damage = damage[0]

        for i in range(len(damage)):
            if i > 0:
                ps[i] += ps[i - 1]

            ps[i] += damage[i]

            max_damage = max(max_damage, damage[i])

        if armor == 0:
            return ps[-1] + 1

        damage_taken_by_armor = armor if armor - max_damage < 0 else max_damage

        return ps[-1] - damage_taken_by_armor + 1
