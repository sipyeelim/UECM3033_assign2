import numpy as np

def omegaSearch(A,D):
    K = np.linalg.inv(D).dot(D-A)
    p = max(np.linalg.eigvals(K));
    omega = 2*(1-np.sqrt(1-p**2))/p**2
    return omega;
    


def LUdecomp(A):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k] != 0.0:
                lam = A[i,k] / A[k,k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                A[i, k] = lam
    return A

def LUsolve(A,b):
    n = len(A)
    for k in range(1,n):
        b[k] = b[k] - np.dot(A[k,0:k], b[0:k])
    b[n-1]=b[n-1]/A[n-1, n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n]))/A[k,k]
    return b

def lu(A, b):
    sol = []
    
    A = LUdecomp(A)
    sol = LUsolve(A,b)

    return list(sol)

def sor(A, b):
    sol = []
    
    ITERATION_LIMIT = 10
 
    n = len(A)
    D = np.zeros_like(A)
    L = np.zeros_like(A)
    
    for i in range(0,n):
        D[i][i] = A[i][i];
        
    for i in range(0,n):
        for j in range(0,i):
            L[i][j] = -A[i][j];
    
    omega = omegaSearch(A,D)   
    Q = D/omega -L
    K = np.linalg.inv(Q).dot(Q-A)
    c = np.linalg.inv(Q).dot(b)
    x = np.zeros_like(b)
    

    for itr in range(ITERATION_LIMIT):
        x   = K.dot(x) + c;

    sol = x
    
    return list(sol)

def solve(A, b):
    condition = True 
    
    condition = False
    try:
        np.linalg.cholesky(A)
    except np.linalg.linalg.LinAlgError :
        condition = True
    
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b)
    
    
if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = np.array([[2.,1,6], [8,3,2], [1,5,1]])
    b = np.array([9., 13, 7]) 
    sol = solve(A,b)
    print(sol)
    
    A = np.array([[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]])
    b = np.array([ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906])
    sol = solve(A,b)
    print(sol)
    
    
    
    
    