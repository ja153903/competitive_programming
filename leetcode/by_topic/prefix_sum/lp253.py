class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        starts, ends = [], []

        for s, e in intervals:
            starts.append(s)
            ends.append(e)

        starts.sort()
        ends.sort()

        ei = 0
        num_min_meetings = 0

        for si in range(len(intervals)):
            if starts[si] < ends[ei]:
                num_min_meetings += 1
            else:
                ei += 1

        return num_min_meetings
