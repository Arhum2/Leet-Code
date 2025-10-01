# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            isBalanced = (abs(left[1] - right[1]) <=1 and left[0] and right[0])

            return [isBalanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Balanced tree
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print(f"Test 1 - Balanced tree: {solution.isBalanced(root1)}")  # Should be True
    
    # Test case 2: Unbalanced tree
    #       1
    #      / \
    #     2   2
    #    / \
    #   3   3
    #  / \
    # 4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    
    print(f"Test 2 - Unbalanced tree: {solution.isBalanced(root2)}")  # Should be False
    
    # Test case 3: Empty tree
    root3 = None
    print(f"Test 3 - Empty tree: {solution.isBalanced(root3)}")  # Should be True
    
    # Test case 4: Single node
    root4 = TreeNode(1)
    print(f"Test 4 - Single node: {solution.isBalanced(root4)}")  # Should be True
    
    # Test case 5: Simple unbalanced tree
    #   1
    #  /
    # 2
    #/
    #3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    
    print(f"Test 5 - Simple unbalanced: {solution.isBalanced(root5)}")  # Should be False