'''
337. House Robber III 
Difficulty: Medium
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    思路：动态规划:
    opt[cur_root][0]:表示当前结点不能抢的最大收益
    opt[cur_root][1]:表示当前结点能抢时的最大收益
    显然有:
    opt[cur_root][0] = rob(cur_root.left,CanRob=True)+rob(cur_root.right,CanRob=True)
    opt[cur_root][1] = max(opt[cur_root][0],#可抢时不抢
                          root.val+rob(root.left,CanRob=False)+rob(root.right,CanRob=False)#可以抢时抢
                          )
    递归计算时肯定会超时，因为会有很多重复计算，因此采用一个opt来保存当前的已经计算的中间结果.
    最终的结果就是opt[root][1]---因为刚开始时，根节点是可抢可不抢的.
    
    '''
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.opt = collections.defaultdict(dict)
        self.doRob(root,True)#根节点默认可抢可不抢
        return self.opt[root][1]
    
    
    def doRob(self,root,CanRob):
        if not root:
            return 0
        if root not in self.opt:
            self.opt[root][0] = self.doRob(root.left,True)+self.doRob(root.right,True)#不能抢的情况下的最大收益
            self.opt[root][1] = max(root.val+self.doRob(root.left,False)+self.doRob(root.right,False),self.opt[root][0])
            #能抢(抢或不抢)情况下的最大收益
        if CanRob:
            return self.opt[root][1]#当前结点可以抢的最大收益
        else:
            return self.opt[root][0]#当前结点不能抢的最大收益
            
