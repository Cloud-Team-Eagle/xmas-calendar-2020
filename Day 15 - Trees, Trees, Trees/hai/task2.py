
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
    visited = set()
    stack = []
    stack.append(root)

    while stack:
        node = stack[-1]
        
        left = node.left_child
        right = node.right_child

        if left and not left in visited:
            stack.append(left)
        elif right and not right in visited:
            stack.append(right)
        else:
            visited.add(node)
            stack.pop()
            print(node)




def infix(root): 
    stack = []
    visited = set()
    stack.append(root)

    while stack:
        node = stack.pop()
        is_leaf = node.right_child == node.right_child == None
        if is_leaf:
            print(node.value)
        else:
            if node in visited:
                print(node.value)
            else:
                visited.add(node)
                stack.append(node.right_child)
                stack.append(node)
                stack.append(node.left_child)
        








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

        print("\n\n\n")
  
        print("prefix")
        prefix(root)

        print("\n\n\n")

        print("postfix")
        postfix(root)

        print("\n\n\n")
        
        
        print("infix")
        infix(root)

        print("\n\n\n")



unittest.main() #verbosity=3)