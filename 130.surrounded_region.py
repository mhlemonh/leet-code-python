class leet130solver(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) != 0:
            tmp_board = [[c for c in r] for r in board]
            search_queue = []
            self.row_num = len(tmp_board)
            self.col_num = len(tmp_board[0])
            ring = self.get_ring_location(self.row_num, self.col_num)
            search_queue.extend((loc for loc in ring))
            search_history = set([])
            while len(search_queue) > 0:
                current_loc = search_queue.pop()
                if current_loc in search_history:
                    continue
                search_history.add(current_loc)
                if tmp_board[current_loc[0]][current_loc[1]] == 'O':
                    tmp_board[current_loc[0]][current_loc[1]] = 'Q'
                    search_queue.extend(self.get_quartet(current_loc[0], current_loc[1]))
                
            for i, _ in enumerate(board):
                board[i] = ''.join('X' if c != 'Q' else 'O' for c in tmp_board[i])

    def get_ring_location(self, row_num, col_num, ori_point=(0, 0)):

        B = [(row_num-1+ori_point[0], i+ori_point[1]) for i in range(col_num-1, -1, -1)]
        L = [(i+ori_point[0], 0+ori_point[1]) for i in range(row_num-2, 0, -1)]
        T = [(0+ori_point[0], i+ori_point[1]) for i in range(col_num)]
        R = [(i+ori_point[0], col_num-1+ori_point[1]) for i in range(1, row_num-1)]
        return T+R+B+L

    def get_quartet(self, r, c):
        quartet=[]
        if r+1 < self.row_num:
            quartet.append((r+1, c))
        if r-1 > -1:
            quartet.append((r-1, c))
        if c+1 < self.col_num:
            quartet.append((r, c+1))
        if c-1 > -1:
            quartet.append((r, c-1))
        return quartet

if __name__ == '__main__':
    b=["XXXXX",
       "XOOOX",
       "XXXOX",
       "XOXOO"]
    c=["",\
       ""]
    s=leet130solver()
    s.solve(b)
    print '==='
    print b