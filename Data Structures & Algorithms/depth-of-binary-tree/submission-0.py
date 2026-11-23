# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        nodes = [(root, 1)]
        visited = set()
        maxPath = 0

        while nodes:
            currNode, path = nodes.pop()
            if (not currNode):
                continue
            nodes.append((currNode.left, path + 1))
            nodes.append((currNode.right, path + 1))
            visited.add(currNode)
            maxPath = max(maxPath, path)

        return maxPath
        