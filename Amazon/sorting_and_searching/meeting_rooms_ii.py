"""
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2


[[0, 30],[5, 10],[15, 20]]
                  *
heap = [20, 30]

"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)