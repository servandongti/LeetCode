class Solution(object):

    def searchMatrix(self, matrix, target):
        # binary search
        try:
            ls_row, ls_col = len(matrix), len(matrix[0])
        except:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        begin, end = 0, ls_row * ls_col - 1
        while begin <= end:
            mid = (begin + end) / 2
            row, col = mid / ls_col, mid % ls_col
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return False
