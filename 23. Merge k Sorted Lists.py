#coding=utf8
'''
23. Merge k Sorted Lists
Difficulty: Hard
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        思路：模仿归并排序，将链表的列表进行递归二分，将分到的两边的列表进行合并
        """
        length = len(lists)
        if length==0:
            return None
        if length==1:#1个链表直接返回
            return lists[0]
        l1 = self.mergeKLists(lists[:length/2])
        l2 = self.mergeKLists(lists[length/2:])
        return self.mergeTwo(l1,l2)#合并两个子链表
        
        
    def mergeTwo(self,p1,p2):#二个链表的合并方法
        p = new_head = ListNode(-1)
        while p1 and p2:
            if p1.val<p2.val:
                tmp = p1.next
                p1.next = None
                p.next = p1
                p = p.next
                p1 = tmp
            else:
                tmp = p2.next
                p2.next = None
                p.next = p2
                p = p.next
                p2 = tmp
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return  new_head.next
            
