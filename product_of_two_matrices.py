
size = 50
def matrix(m, rs, cs ):
    
    for i in range(rs):
        for j in range(cs):
            print(m[i][j] , end = " ")
        print()
def matrix_mul(A, r1, c1, B, r2, c2):
    C = [[0 for i in range(size)]for j in range(size)]
    
    #codition if multiplication is possible or not
    if(r2 != c1):
        print("Multiplication is not possible")
        return
    
    #multiplcation
    for i in range(r1):
        for j in range(c2):
            C[i][j] = 0
            for k in range(r2):
                C[i][j] += A[i][k] * B[k][j];
    print("Product of those matrix is")
    matrix(C, r1, c2)
    
if __name__ == "__main__" :
    A = [[0 for i in range(size)]for j in range(size)]
    B = [[0 for i in range(size)]for j in range(size)]
    r1 = int(input("enter the no. of rows for first matrix :"))
    c1 = int(input("enter the no. of columns for first matrix :"))
    
    print("first matrix:");
    for i in range(r1):
        for j in range(c1):
            A[i][j] = int(input("A(" + str(i) + ")(" + str(j) + "): " ))#read the elements for A matrix
    
    r2 = int(input("enter the no. of rows for first matrix :"))
    c2 = int(input("enter the no. of columns for first matrix :"))
    
    print("Second matrix");
    for i in range(r2):
        for j in range(c2):
            B[i][j] = int(input("B(" + str(i) + ")(" + str(j) + "): " )) 
            
    print("1.Matrix")
    matrix(A, r1, c1)
    print("2.Matrix")
    matrix(B, r2, c2)
    
    matrix_mul(A, r1, c1, B, r2, c2)
