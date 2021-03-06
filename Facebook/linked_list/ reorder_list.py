# time: O(n)
# space: O(n)
# Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""

Given 1->2->3->4->5
reorder it to 1->5->2->4->3.

double_ll = [[1, N], [2,1], [3,2], [4, 3], [5, 4]]
double_ll = [[4, 3], [5, 4]]


double_ll = [[4, 3]]
new_parent = 5
parent = 4
1->N
2->3->4
1->5->2->3->4


double_ll = []
new_parent = 4
parent = 3
1->5->2->N
3
1->5->2->4->3
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        double_ll = [] #this will imitate a doubley linked list
        current = head 
        prev = None
        while current: #fill doubley ll
            double_ll.append([current, prev])
            prev = current
            current = current.next
        double_ll = double_ll[(len(double_ll) // 2) + 1:] #remove and include only nodes that will be swapped
        current = head
        while current: #while you can move through linked list
            if double_ll:
                new_next, parent = double_ll.pop() #pop of double_ll
                next_node = current.next #store next_node
                parent.next = None #remove relationship with parent
                current.next = new_next #general swaps
                new_next.next = next_node
                current = new_next.next
                continue
            current = current.next #continue until the end of the linked list