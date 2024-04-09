class Cell:
    def __init__(self, status) -> None:
        self.type = status
    

    def status(self):
        return self.type



class Checkers():
    def __init__(self) -> None:
        # self.board = {row+col:Cell("W") for row in '87654321' for col in 'ABCDEFGH' }
        
        self.board = dict()

        self.temp = ['XBXBXBXB',
                   'BXBXBXBX',
                   'XBXBXBXB',
                   'XXXXXXXX',
                   'XXXXXXXX',
                   'WXWXWXWX',
                   'XWXWXWXW',
                   'WXWXWXWX']

        
        # for i in self.board:
        #     print(i, self.board[i])

        x = 0
        y = 0
        for row in '87654321':
            x = 0
            for col in 'ABCDEFGH':
                self.board [col + row] = self.temp[x][y]
                x += 1
            y += 1
                

        self.temp2 = 'XBXBXBXB'+'BXBXBXBX'+'XBXBXBXB'+'XXXXXXXX'+'XXXXXXXX'+'WXWXWXWX'+'XWXWXWXW'+'WXWXWXWX'
        i = 0
        for row in '87654321':
            for col in 'ABCDEFGH':
                self.board [col + row] = Cell(self.temp2[i])
                i += 1

    def move(self, f, t):
        a = self.board[f].status()
        self.board[f].type = "X"
        self.board[f].type = a

Checkers()