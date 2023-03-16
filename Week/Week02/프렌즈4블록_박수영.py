def pang(m, n, board):
    cp_board = [list(row) for row in board] # 문자 단위로 분해(inplace를 위함)
    
    search_directions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    will_removed_idx = []
    for i in range(m-1):
        for j in range(n-1):
            curr_block = cp_board[i][j]
            if curr_block == ' ':
                continue
            
            searched_idx = [(i + x, j + y) for x, y in search_directions]
            if all([True if curr_block == cp_board[nx][ny] else False for nx, ny in searched_idx]):
                will_removed_idx.extend(searched_idx)
    
    will_removed_idx = list(set(will_removed_idx))
    for x, y in will_removed_idx:
        cp_board[x][y] = ''
        
    return (len(will_removed_idx), cp_board)

def update_board(m, n, board):
    grouped_by_col = []
    for col in zip(*board):  # zip()의 return type: tuple
        concat_characters = ''.join(col)
        concat_characters = concat_characters.rjust(m, ' ')
        grouped_by_col.append(list(concat_characters))
    
    grouped_by_row = []
    for row in zip(*grouped_by_col):
        grouped_by_row.append(''.join(row))
    
    return grouped_by_row

def solution(m, n, board):
    answer = 0
    while True:
        cnt, board = pang(m, n, board)
        
        if cnt == 0:
            break
        
        answer += cnt
        board = update_board(m, n, board)
        
    return answer