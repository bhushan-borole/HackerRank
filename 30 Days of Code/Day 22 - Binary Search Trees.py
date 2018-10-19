# https://www.hackerrank.com/challenges/30-binary-search-trees/problem

def getHeight(self,root):
    if root:
        leftDepth = self.getHeight(root.left)
        rightDepth = self.getHeight(root.right)
        return max(leftDepth,rightDepth) + 1
    else:
        return -1