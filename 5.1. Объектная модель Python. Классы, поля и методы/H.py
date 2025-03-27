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
        x = 0
        y = 0
        for row in '87654321':
            x = 0
            for col in 'ABCDEFGH':
                self.board [col + row] = Cell(self.temp[x][y])
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



######
class Cell():
    def __init__(self, cell_item='X') -> None:
        self.state = cell_item

    def status(self):
        return self.state

    def remove_check(self):
        check = self.status()
        self.state = 'X'
        return check

    def set_check(self, check):
        old_check = self.status()
        self.state = check
        return old_check


class Checkers():
    def __init__(self) -> None:
        self.cells = dict()
        checker_board = 'XBXBXBXB' + 'BXBXBXBX' + 'XBXBXBXB' + 'XXXXXXXX' + \
            'XXXXXXXX' + 'WXWXWXWX' + 'XWXWXWXW' + 'WXWXWXWX'

        i = 0
        for row in '87654321':
            for col in 'ABCDEFGH':
                self.cells[col + row] = Cell(cell_item=checker_board[i])
                i += 1

    def get_cell(self, cell):
        return self.cells[cell]

    def move(self, where_from, where_to):
        check = self.cells[where_from].remove_check()
        return self.cells[where_to].set_check(check)