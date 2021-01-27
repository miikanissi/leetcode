# A bus has n stops numbered from 0 to n - 1 that form a circle.
# We know the distance between all pairs of neighboring stops where
# distance[i] is the distance between the stops number i and (i + 1) % n.
# The bus goes along both directions i.e. clockwise and counterclockwise.
# Return the shortest distance between the given start and destination stops.
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        sum1 = sum(distance[start:destination])
        sum2 = sum(distance) - sum1
        return min(sum1, sum2)


if __name__ == "__main__":
    distance = [1, 2, 3, 4]
    start = 0
    dest = 1
    print(Solution().distanceBetweenBusStops(distance, start, dest))
