'''
289. Game of Life My Submissions QuestionEditorial Solution
Total Accepted: 16057 Total Submissions: 47114 Difficulty: Medium
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        思路：题目要求在原址上修改，因此注重考察编码问题:
        0：死 1：活
        +10(只有状态转换才会加10)
        10:死->活(当前状态死，下个状态活)
        11:活->死(当前状态活，下个状态死)
        总结：
        当前状态死: 0 or 10  (%10==0)  
        当前状态活: 1 or 11  (%10==1)
        下个状态死: 0 or 11
        下个状态活: 1 or 10 
        """
        if not board:
            return 
        rows,cols = len(board),len(board[0])
        grid = lambda r,c:((r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1))
        for row in range(rows):
            for col in range(cols):
                lives = sum([board[x][y]%10 for x,y in grid(row,col) if (x>=0 and x<rows) and (y>=0 and y<cols)])
                #只修改状态转换的节点
                #死->活  or 活->死
                if (board[row][col]%10==0 and lives==3) or (board[row][col]%10==1 and (lives!=2 and lives!=3)):
                    board[row][col]+=10
        #只修改状态转换的节点，值为10或11的，其它节点保持不变
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==10:
                    board[row][col]=1
                elif board[row][col]==11:
                    board[row][col]=0
