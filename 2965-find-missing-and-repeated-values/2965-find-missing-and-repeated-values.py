class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)

        seen = set()
        repeated = 0

        total = 0

        for row in grid:
            for num in row:
                total += num

                if num in seen:
                    repeated = num
                else:
                    seen.add(num)

        expected = (n * n) * (n * n + 1) // 2

        missing = expected - (total - repeated)

        return [repeated, missing]