class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """2661. First Completely Painted Row or Column
        m =len(mat)
        n = len(mat[0])
        pos_map = {}
        for i in range(m):
            for j in range(n):
                pos_map[mat[i][j]] = (i, j)
        row_count = [0] * m
        col_count = [0] * n
        for i, num in enumerate(arr):
            row, col = pos_map[num] 
            row_count[row] += 1 
            col_count[col] += 1
            if row_count[row] == n or col_count[col] == m:
                return i
