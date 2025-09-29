from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # number of rows == number of columns 
        N = len(grid)
        # possible directions
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # check if out of bounds
        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        # looking for the first island
        visit = set()
        def dfs(r, c):
            if (invalid(r, c) or grid[r][c] == 0 or (r, c) in visit):
                return
            visit.add((r, c))
            # calling dfs for all directions
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            # length of the bridge
            res = 0
            # queue
            q = deque(visit)

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        # checking for valid coordinate or if the current loc checked
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                # increment our travel 
                res += 1

        # adds one island to the visit set
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()


# Test cases
solution = Solution()

# Test case 1: Small grid with minimum bridge length of 1
grid1 = [
    [0, 1],
    [1, 0]
]
print("Test Case 1:", solution.shortestBridge(grid1))  # Expected output: 1

# Test case 2: Larger grid with bridge length of 2
grid2 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1]
]
print("Test Case 2:", solution.shortestBridge(grid2))  # Expected output: 2

# Test case 3: Large island surrounding the other
grid3 = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
print("Test Case 3:", solution.shortestBridge(grid3))  # Expected output: 1

# Test case 4: Two islands with a complex grid
grid4 = [
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
print("Test Case 4:", solution.shortestBridge(grid4))  # Expected output: 1

# Test case 5: Edge case with multiple bridge options
grid5 = [
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]
print("Test Case 5:", solution.shortestBridge(grid5))  # Expected output: 2

# Test case 6: Grid with no water cells
grid6 = [
    [1, 1],
    [1, 1]
]
print("Test Case 6:", solution.shortestBridge(grid6))  # Expected output: 0
