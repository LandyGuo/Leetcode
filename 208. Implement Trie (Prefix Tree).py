'''
208. Implement Trie (Prefix Tree) 
Difficulty: Medium
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.isword = False#注意这里：一定要添加一个isword属性，表明该节点是一个单词的结尾，因为insert("ab")与insert("abc")之后，"b"和"C"都是单词节点
        self.children = {}#注意用python实现前缀树，一般用字典放节点的孩子
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root#用cur_node表明在插入当前字符之前的prefix_tree中的位置(状态)
        for i,c in enumerate(word):#依次处理每个字符，
            if c not in cur_node.children:#没找到,创建节点插入到当前节点的孩子里
                new_node = TrieNode()
                new_node.val = c
                cur_node.children[c] = new_node 
            cur_node = cur_node.children[c]#找到当前字符的在prefix_tree中的位置
            if i==len(word)-1:#在单词的末尾字符处更新isword属性
                cur_node.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return True if cur_node.isword else False#注意：查找单词与查找前缀的区别仅仅在这里

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return True 
