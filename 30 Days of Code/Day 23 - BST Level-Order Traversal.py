# https://www.hackerrank.com/challenges/30-binary-trees/problem

def levelOrder(self,root):
    leafs = [root]
    while len(leafs) > 0:
        leaf = leafs.pop(0)
        print(leaf.data, end=" ")
        if leaf.left:
            leafs.append(leaf.left)
        if leaf.right:
            leafs.append(leaf.right)