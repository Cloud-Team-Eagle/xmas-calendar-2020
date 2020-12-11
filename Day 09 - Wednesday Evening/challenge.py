
class TreeNode(object):
	def __init__(self, value):
		self.value = value
		self.children  = []



# Challenge
# Imagine the tree being the orgchart of our organization.
# Print out all employees ordered by rank (the closer to the root node the higher in rank).

root = TreeNode('Big boss')

master1 = TreeNode('Master 1')
master2 = TreeNode('Master 2')
master3 = TreeNode('Master 3')

minion1 = TreeNode('Minion 1')
minion2 = TreeNode('Minion 2')
minion3 = TreeNode('Minion 3')
minion4 = TreeNode('Minion 4')
minion5 = TreeNode('Minion 5')

master2.children = [minion1, minion2]
master3.children = [minion3, minion4, minion5]

root.children = [master1, master2, master3]

#                      4
#                   /    \
#                  2       5 
#                /  \   
#               1    3
#              

# BFS:                   4, 2, 5, 1, 3
# DFS Prefix:            4, 2, 1, 3, 5
# DFS Infix(in order):   1, 2, 3, 4, 5  
# DFS Suffix:            1, 3, 2, 5, 4  


# BFS - Breadth First Search
def main():
  to_visit_queue = []

  to_visit_queue.append(root)  #enqueue first node of tree

  while to_visit_queue:
    node = to_visit_queue.pop(0) #dequeue
    
    print(node.value)
    for child in node.children:
      to_visit_queue.append(child)


if __name__ == "__main__":
    main()
