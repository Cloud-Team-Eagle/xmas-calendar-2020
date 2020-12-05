import unittest

# A cycle occurs when a node’s next points back
# to a previous node in the list. 
# The linked list is no longer linear with a 
# beginning and end—instead, it cycles through a loop of nodes.
#
# Write a function contains_cycle() that takes the 
# first node in a singly-linked list and returns a 
# boolean indicating whether the list contains a cycle.



class LinkedListNode(object):
	def __init__(self, value):
		self.value = value
		self.next  = None


#   a -->  b --> c --> d --> e -\
#                ^--------------/

#   a -->  b --> c --> d --> e -\
#                      ^--------/

#   a -->  b --> c --> d --> e -> e

def contains_cycle(first_node):
	# do the quick wins
	if first_node is None or first_node.next is None:
		return False

	slow_it = first_node
	fast_it = first_node.next

	for i in range(10_000):
		if slow_it == fast_it:
			return True

		if (fast_it is None 
			or fast_it.next == None 
			or fast_it.next.next == None):
			return False
		
		slow_it = slow_it.next
		fast_it = fast_it.next.next
		
	# raise 




def contains_cycle_1(first_node):
	iterator = first_node

	visited = set()
	while iterator is not None and iterator.next is not None:
		if id(iterator) in visited:
			return True
		else:
			visited.add(id(iterator))

		iterator = iterator.next
      
	return False




# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

    def test_linked_list_with_no_cycle(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_two_node_cycle_at_end(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = fourth
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_empty_list(self):
        result = contains_cycle(None)
        self.assertFalse(result)

    def test_one_element_linked_list_no_cycle(self):
        first = Test.LinkedListNode(1)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_one_element_linked_list_cycle(self):
        first = Test.LinkedListNode(1)
        first.next = first
        result = contains_cycle(first)
        self.assertTrue(result)


unittest.main(verbosity=2)
