class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        n = len(matrix)
        m = len(matrix[0])

        lo = 0
        hi = n * m - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            value = matrix[mid // m][mid % m]

            if value == target:
                return True

            if value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False