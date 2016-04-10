'''
331. Verify Preorder Serialization of a Binary Tree 
Difficulty: Medium
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
'''
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        思路：根据二叉树上还能挂几个节点，一个根节点(如果不为"#")后面还有2个空位置，
        增加一个子节点，如果是数，可以增加一个空位置；如果是"#"减少一个空位置
        如果序列没遍历完，就始终保持empty_space>=0 并且empty_space最后一定是0
        """
        nodes = preorder.split(',')
        empty_space = 2 if nodes[0]!="#" else 0
        for x in nodes[1:]:
            if empty_space<=0:
                return False
            elif x=="#":
                empty_space-=1
            else:
                empty_space+=1
        return True if empty_space==0 else False
        
