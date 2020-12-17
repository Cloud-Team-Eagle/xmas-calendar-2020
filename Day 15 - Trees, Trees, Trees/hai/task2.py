
import unittest


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    def __str__(self):
        return str(self.value)


def prefix(root): 
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node)
        
        if node.right_child or node.left_child:
            if node.right_child:
                stack.append(node.right_child)
            if node.left_child:
                stack.append(node.left_child)

        
def postfix(root): 
    stack = []
    stack.append(root)
    visited = set()

    while stack:
        node = stack[-1]
        
        if node.right_child or node.left_child:
            print("node has children:", )
            if node.left_child:
                stack.append(node.left_child)
            if node.right_child:
                stack.append(node.right_child)
        else:
            print(stack.pop())




class Test(unittest.TestCase):
    def test_case1(self):
        """
        +                     
        |  \
        *   3                  
        |\                     
        4 5                  
        """
        root = TreeNode('+')
        root.left_child = TreeNode('*')
        root.left_child.left_child = TreeNode(4)
        root.left_child.right_child = TreeNode(5)
        root.right_child = TreeNode(3)
  
        print("prefix")
        prefix(root)

        print("postfix")
        postfix(root)
        
        

unittest.main() #verbosity=3)