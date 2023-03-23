def get_chain(k, n, m, A): 
  C = [0] * (n + m - 2) * 2 
  i, j = k, k 
  t = 0
  for _ in range(n - 1): 
    C[t] = A[i][j] 
    i += 1; t += 1
  for _ in range(m - 1):
    C[t] = A[i][j]
    j += 1; t += 1
  for _ in range(n - 1): 
    C[t] = A[i][j]
    i -= 1; t += 1
  for _ in range(m - 1): 
    C[t] = A[i][j]
    j -= 1; t += 1

  return C

def put_chain(C, k, n, m, A): 
  i, j = k, k 
  t = 0 
  for _ in range(n - 1): 
    A[i][j] = C[t] 
    i += 1; t += 1
  for _ in range(m - 1):
    A[i][j] = C[t]
    j += 1; t += 1
  for _ in range(n - 1): 
    A[i][j] = C[t]
    i -= 1; t += 1
  for _ in range(m - 1): 
    A[i][j] = C[t]
    j -= 1; t += 1


def rotate(k, n, m, r, A): 
  chain = get_chain(k, n, m, A) 
  pos = len(chain) - (r % len(chain)) 
  rotated = chain[pos:]+chain[:pos]
  put_chain(rotated, k, n, m, A) 


def solve(n, m, r, A): 
  for k in range(min(n, m) // 2): 
    rotate(k, n-2*k, m-2*k , r, A) 
  for i in range(n): 
    print(' '.join(map(str, A[i])))

n, m, r = map(int, input().split())  
A = [list(map(int, input().split())) for _ in range(n)] 

solve(n, m, r, A) 