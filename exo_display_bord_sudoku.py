class Sudoku:
    def __init__(self, board):
        
        self.board = [Sudoku.split(board[x:x+9]) for x in range(0, len(board), 9)]

    def split(word):
        return [int(char) for char in word]  

    def get_row(self, number):
        return self.board[number]
    def get_col(self, number):
        return [el[number] for el in self.board]
    
    def get_sqr(self, n, m=None):
        square = []
        brutBoard = sum(self.board, [])
        # for num in [0,3,6,27,30,54,57,60]:
        for i in range (0, len(brutBoard), 27):
            for num in range(i,i+9,3):
                if m is not None:
                    indexNumber = 9*n + m
                    if ((indexNumber>=num and indexNumber<=num+3) or (indexNumber>=num+9 and indexNumber<=num+12) or (indexNumber>=num+18 and indexNumber<=num+20)):
                        bigCellIs = brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21]
                        return bigCellIs
                square.append(brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21])
        return square[n]




g1 = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
g2 = Sudoku("005001000287369100416520000000700692000000000000806453843000000000930000950074200")
g3 = Sudoku("270981006015726983869000271092678354057134829384259617730800462028407130040302798")

# print(g1.board)
# print(g3.get_col(8))
print(g1.get_sqr(8,3))
print(g2.get_sqr(5, 2))
print(g2.get_sqr(8, 0))