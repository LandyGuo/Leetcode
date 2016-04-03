/*
220. Contains Duplicate III 
Difficulty: Medium
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
*/

//关键:给定val，在大小为k的集合里查找离val最近的数(O(lgk)才能AC，若为O(k)会超时)
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(t<0) return false;//两个数之间距离最小为0，不可能为负
        multiset<long long> bst;
        for(int i=0;i<nums.size();i++)
        {
            if(bst.size()==k+1) //维持bst的大小为k
                bst.erase(bst.find(nums[i-k-1]));
            //注意:如果bst中存在nums[i],则lower_bound指向nums[i],upper_bound()指向bst中>nums[i]的第一个数
            //如果不存在nums[i]，则lower_bound指向第一个>nums[i]的数，upper_bound也指向第一个>nums[i]的位置(前一个就是第一个<nums[i]的位置)
            auto lb = bst.lower_bound(nums[i]);//在bst中第一个>=nums[i]的数
            auto ub = bst.upper_bound(nums[i]);//在bst中第一个>nums[i]的数，之前迭代器指向第一个<=nums[i]的数
            if(lb!=ub)//不相等，说明nums[i]存在于bst中，距离为0
                return true;
            //相等说明nums[i]不存在于BST中
            else if((lb!=bst.end()&&*lb-nums[i]<=t)//lb指向第一个>nums[i]的数，查找时间O(lgk) 
            ||(lb!=bst.begin()&& nums[i]-*(--lb)<=t))//lb-1指向第一个<nums[i]的数
                return true;
            bst.insert(nums[i]);
        }
        return false;
        
    }
};
