
import unittest


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


# Same algorithm that convert tree to list
def has_loop(root): 
    debug = False
    stack = []
    id_set = set()
    iterator = root

    for i in range(1, 1_000_000):
        if debug: print(id_set)
        if iterator:
            if debug: print(iterator.value)
            stack.append(iterator)
            iterator = iterator.left_child
        elif stack:
            iterator = stack.pop()
            print('Node value: {}'.format(iterator.value))
            if (id(iterator) in id_set):
                return True
            else:
                id_set.add(id(iterator))
            iterator = iterator.right_child
        else:
            break

    return False


class Test(unittest.TestCase):
    def test_case1(self):
        """
        1                     4
        |  \
        2   3                 3 
        |\  |                   
        4 5 6                 2
        |
        7                     1 
        """
        root = TreeNode(1)
        root.left_child = TreeNode(2)
        root.right_child = TreeNode(3)
        root.left_child.left_child = TreeNode(4)
        root.left_child.right_child = TreeNode(5)
        root.right_child.left_child = TreeNode(6)
        root.left_child.left_child.left_child = TreeNode(7)
        result = has_loop(root)
        print('\n******************************')
        print(result)
        self.assertFalse(result)
    

    def test_case2(self):
        """
        1                     4
        |  \
        2   3                 3 
        |\  |                   
        4 5 6                 2
        |   |
        7   8                 1 
        """
        root = TreeNode(1)
        root.left_child = TreeNode(2)
        root.right_child = TreeNode(3)
        root.left_child.left_child = TreeNode(4)
        root.left_child.right_child = TreeNode(5)
        root.right_child.left_child = TreeNode(6)
        root.left_child.left_child.left_child = TreeNode(7)
        root.right_child.left_child.left_child = TreeNode(8)
        result = has_loop(root)
        print('\n******************************')
        print(result)
        self.assertFalse(result)


    def test_case3(self):
        """
        1                     4
        |  \
        2   3                 3 
        |   |                   
        4   5                 2
        |   |
        6-->7                 1 
        """
        root = TreeNode(1)
        root.left_child = TreeNode(2)
        root.right_child = TreeNode(3)
        root.left_child.left_child = TreeNode(4)
        root.right_child.left_child = TreeNode(5)
        root.left_child.left_child.left_child = TreeNode(6)
        shared_node= TreeNode(7)
        root.left_child.left_child.left_child.right_child = shared_node
        root.right_child.left_child.left_child = shared_node
        result = has_loop(root)
        print('\n******************************')
        print(result)
        self.assertTrue(result)


unittest.main(verbosity=3)