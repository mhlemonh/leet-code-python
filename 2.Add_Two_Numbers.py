# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from itertools import izip_longest

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        list_1 = self.extract_num(l1)
        list_2 = self.extract_num(l2)
        sum_list = self.list_sum(list_1, list_2)
        return self.assemble(sum_list)


    def assemble(self, number_list):
        link_tail = None
        for num in reversed(number_list):
            linked_list = ListNode(num)
            linked_list.next = link_tail
            link_tail = linked_list
        try:
            return linked_list
        except UnboundLocalError:
            return None

    def list_sum(self, list1, list2):
        sum_list = []
        r=0
        for n1, n2 in izip_longest(list1, list2, fillvalue=0):
            s = n1+n2+r
            if s > 9:
                r = 1
                s = s-10
            else:
                r = 0
            sum_list.append(s)
        if r > 0:
            sum_list.append(r)
        return sum_list

    def extract_num(self, list_node):
        numbers = []
        while (list_node is not None):
            numbers.append(list_node.val)
            list_node = list_node.next
        return numbers
