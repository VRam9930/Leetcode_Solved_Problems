class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        prefixTop = [0] * n
        prefixBottom = [0] * n

        prefixTop[0] = grid[0][0]
        prefixBottom[0] = grid[1][0]

        for i in range(1, n):
            prefixTop[i] = prefixTop[i-1] + grid[0][i]
            prefixBottom[i] = prefixBottom[i-1] + grid[1][i]

        minMaxPoints = float('inf')
        
        for i in range(n):
            topRemaining = prefixTop[-1] - prefixTop[i]
            bottomRemaining = prefixBottom[i-1] if i > 0 else 0
            maxPointsForRobot2 = max(topRemaining, bottomRemaining)
            minMaxPoints = min(minMaxPoints, maxPointsForRobot2)
        
        return minMaxPoints


        
