'''
211. Add and Search Word - Data structure design 
Difficulty: Medium
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.isword = False
        self.children = {}


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TreeNode(-1)

    def addWord(self, word):#添加单词就是建立前缀树的过程
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for i,c in enumerate(word):
            if c not in cur_node.children:
                new_node = TreeNode(c)
                cur_node.children[c] = new_node
            cur_node = cur_node.children[c]
            if i==len(word)-1:
                cur_node.isword = True
                
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.doSearch(0,self.root,word)#通过添加一个函数，修改入口参数

    def doSearch(self,index,root,word):#每次调用只匹配当前一个字符
        if index==len(word) and root.isword:
            return True
        if index>=len(word):#有可能单词结束但在前缀树中单词的最后一个字符不是单词节点，这时候index会继续增加
            return False
        cur_c,cur_root = word[index],root
        if cur_c==".":#如果当前是“.”,当前就跟所有的孩子匹配上
            for _,nxt_root in cur_root.children.items():
                if self.doSearch(index+1,nxt_root,word):#所有孩子中只要有一个匹配上，就说明能匹配
                    return True
            return False
        else:#不是"."，按正常匹配流程：找到孩子继续匹配，没找到就匹配失败
            if cur_c in cur_root.children:
                return self.doSearch(index+1,cur_root.children[cur_c],word)
            return False
            
        
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
