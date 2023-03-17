def solution(m, n, board): 
    board = [list(r) for r in board]
    
    answer = 0 
    while True: 
        blocks = remove_blocks(board, m, n)
        if blocks == 0: 
            return answer 
        
        answer += blocks
         
        for c in range(n): 
            cnt_blank = 0 
            for r in range(m-1, -1, -1): 
                if board[r][c] == '': 
                    cnt_blank += 1 
                elif cnt_blank > 0: 
                    board[r+cnt_blank][c] = board[r][c] 
                    board[r][c] = '' 
                    
    return answer 

             
def remove_blocks(board, m, n): 
    check = [[False for c in range(n)] for r in range(m)] 
    for r in range(m-1): 
        for c in range(n-1): 
            block = board[r][c] 
            if block == '': 
                continue 
            if board[r+1][c] == block and board[r][c+1] == block and board[r+1][c+1] == block:
                check[r][c] = True 
                check[r+1][c] = True 
                check[r][c+1] = True 
                check[r+1][c+1] = True 
     
    cnt_removed = 0 
    for r in range(m): 
        for c in range(n): 
             if check[r][c]: 
                board[r][c] = '' 
                cnt_removed += 1 
    return cnt_removed