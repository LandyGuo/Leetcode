#coding=utf8
'''
328. Odd Even Linked List
Difficulty: Medium
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路：双指针法，一个指针指向偶数节点，一个指针指向奇数节点，移动步长为2
        """
        if not head:
            return 
        p1 ,p2= head,head.next
        even_head,odd_head =p1, p2#p1指向偶数节点，p2指向奇数节点
        while p2:#因为p2在p1之后，所以只用判断p2是否为空即可判断终止
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next if p1 else None
            p2 = p2.next
        #为了将偶数节点的最后一个连接奇数节点的头节点，需要定位到偶数节点的最后一个节点
        p1 = even_head
        while p1.next:
            p1= p1.next
        #连接偶数节点的最后一个与奇数节点的头节点
        p1.next = odd_head
        return even_head
        
