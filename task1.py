import numpy as np

#find omega
def omegasearch(A,D):
    K = np.linalg.inv(D).dot(D-A)
    eig = max(np.linalg.eigvals(K));
    omega = 2*(1-np.sqrt(1-eig**2))/eig**2
    return omega;

def LUdecomp(A):
       n=len(A)
       for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k]!= 0.0:
                lam = A[i,k] / A[k,k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                A[i, k] = lam
        return A

def lu(A, b):
      A=LUdecomp(A)
      n = len(A)
      for k in range(1,n):
           b[k] = b[k] - np.dot(A[k,0:k], b[0:k])
           b[n-1]=b[n-1]/A[n-1, n-1]
      for k in range(n-2, -1, -1):
           b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n]))/A[k,k]
      return b

def sor(A, b):
    sol = []
    LIMIT_OF_ITERATION = 10
    D = np.zeros_like(A)
    omega=omegasearch(A,D)
    
    x = np.zeros_like(b)
    for itr in range(LIMIT_OF_ITERATION):
        for j in range(len(b)):
            sums = np.dot( A[j,:], x )
            x[j] = x[j] + omega*(b[j]-sums)/A[j,j]
    return list(sol)

def solve(A, b):

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

    A = np.array([[2,1,6], [8,3,2], [1,5,1]]).astype(float)
    b = np.array([9, 13, 7]).astype(float)
    
    sol = np.linalg.solve(A,b)
    solve(A,b)
    print(sol)
    
    A = np.array([[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]).astype(float)
    b = np.array([ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]).astype(float)
    sol = np.linalg.solve(A,b)
    solve(A,b)
    print(sol)
