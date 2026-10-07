class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row_l = 0
        row_r = len(matrix)

        while row_l < row_r:
            row_m = row_l + (row_r - row_l) // 2
            row = matrix[row_m]

            if target < row[0]:
                row_r = row_m
                continue

            if target == row[0]:
                return True

            l = 0
            r = len(row)

            while l < r:
                m = l + (r - l) // 2

                if row[m] < target:
                    l = m + 1
                elif row[m] > target:
                    r = m
                else:
                    return True

            if row_m + 1 >= len(matrix):
                return False

            if matrix[row_m + 1][0] > target:
                return False

            row_l = row_m + 1

        return False