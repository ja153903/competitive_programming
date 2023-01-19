class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        result = []

        i, n = 0, len(intervals)

        # Insert all intervals that happen before the interval we want to insert
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # Merge all incoming intervals with new_intervals
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval = [
                min(intervals[i][0], new_interval[0]),
                max(intervals[i][1], new_interval[1]),
            ]

            i += 1

        # add the new interval
        result.append(new_interval)

        # add the rest
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
