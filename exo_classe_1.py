
# Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:
class ones_threes_nines:
    def __init__(self, number):
        self.number = number
        self.nines = 0
        self.threes = 0
        self.ones=0
        self.answer = ''
        self.countNumber()
    
    def countNumber(self):

        first_reminder = self.number % 9 
       
        if first_reminder == 0:
            self.nines = self.number // 9
            self.answer = ('nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones))
        else:
            second_reminder = first_reminder % 3
            threes = first_reminder // 3
            if second_reminder == 0:
                self.answer = ('nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones))
            else:
                self.ones = second_reminder
                self.answer = ('nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones))
        return self.answer


test = ones_threes_nines(1)
print(test.answer)


'''

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
        if m is not None and m <=2:
            m =1
        elif m is not None and (m >=3 and m <=5):
            m= 2
        else:
            m=3
        for i in range (0, len(brutBoard), 27):
            j = 1
            for num in range(i,i+9,3):
                
                print(len(square),   m)
                if m is not None and (len(square) == 5 and m ==j):
                    bigCellIs = brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21]
                    return bigCellIs
                square.append(brutBoard[num:num+3] + brutBoard[num+9:num+12] + brutBoard[num+18:num+21])
                j += 1
        # print("bigCellIs: ",num, num+21, m + 9*n, bigCellIs)
        # return square[n]




g1 = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
g2 = Sudoku("005001000287369100416520000000700692000000000000806453843000000000930000950074200")
g3 = Sudoku("270981006015726983869000271092678354057134829384259617730800462028407130040302798")

# print(g1.board)
# print(g3.get_col(8))
print(g1.get_sqr(1,8))
print(g2.get_sqr(5, 2))
print(g2.get_sqr(8, 0))

'''