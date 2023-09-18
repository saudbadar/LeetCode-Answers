"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        rowMax, colMax = len(grid), len(grid[0])
        def checkValid(startRow, startCol, endRow, endCol):
            check = grid[startRow][startCol]
            for row in range(startRow, endRow):
                for col in range(startCol, endCol):
                    if(check != grid[row][col]):
                        return(False)
            return(True)
        
        head = Node(0, 0, None, None, None, None)
        def recursion(startRow, startCol, length, node):
            if(checkValid(startRow, startCol, startRow + length, startCol + length)):
                node.val, node.isLeaf = grid[startRow][startCol], True
            else:
                node.isLeaf, newLength = False, length // 2
                node.topLeft, node.topRight, node.bottomLeft, node.bottomRight = Node(0, 0, None, None, None, None), Node(0, 0, None, None, None, None), Node(0, 0, None, None, None, None), Node(0, 0, None, None, None, None)
                recursion(startRow, startCol, newLength, node.topLeft)
                recursion(startRow, startCol + newLength, newLength, node.topRight)
                recursion(startRow + newLength, startCol, newLength, node.bottomLeft)
                recursion(startRow +newLength, startCol +newLength, newLength, node.bottomRight)
        recursion(0, 0, rowMax, head)
        return(head)