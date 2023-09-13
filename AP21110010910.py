import numpy as np  
print("Enter the matrix that actions are to be performed: ",end="\n")
matrix = [[int(input()) for c in range (3)] for r in range(3)]
print("Enter the matrix the final matrix: ",end="\n")
matrix2= [[int(input()) for c in range (3)] for r in range(3)]
def create(matrix,c,d,r,p):
    def huristic(matrix,c,d):
        count=0
        for i in range(3):
            for j in range(3):
                if(matrix[i][j]!=matrix2[i][j]):
                    count+=1
        print("huristic value :",count,end=" \n")            
    def find():
        for i in range(3):
            for j in range(3):
                if(matrix[i][j]==0):
                    c=i
                    d=j
        return c,d
    def left(matrix,c,d):
            if d > 0:
                print("depth level",r)
                print("Action performed: ","left")
                matrix1=np.copy(matrix)
                temp1=matrix1[c][d-1]
                matrix1[c][d-1]=matrix1[c][d]
                matrix1[c][d]=temp1
                c,d=find()
                print(matrix1,end="\n")
                huristic(matrix1,c,d)
                create(matrix1,c,d,r+1,p)
    def right(matrix,c,d):
            if d < 2 :  
                print("depth level",r)
                print("Action performed: ","right")
                matrix1=np.copy(matrix)  
                temp1=matrix1[c][d+1]
                matrix1[c][d+1]=matrix1[c][d]
                matrix1[c][d]=temp1
                c,d=find()
                print(matrix1,end="\n")
                huristic(matrix1,c,d)
                create(matrix1,c,d,r+1,p)
    def up(matrix,c,d):
            if c > 0:
                print("depth level",r)
                print("Action performed: ",'up')
                matrix1=np.copy(matrix)
                temp1=matrix[c-1][d]
                matrix1[c-1][d]=matrix[c][d]
                matrix1[c][d]=temp1
                c,d=find()
                print(matrix1,end="\n")
                huristic(matrix1,c,d)
                create(matrix1,c,d,r+1,p)
    def down(matrix,c,d):
            if c < 2:  
                print("depth level",r)
                print("Action performed: ",'down')
                matrix1=np.copy(matrix)  
                temp1=matrix1[c+1][d]
                matrix1[c+1][d]=matrix1[c][d]
                matrix1[c][d]=temp1
                c,d=find()
                print(matrix1,end="\n")
                huristic(matrix1,c,d)
                create(matrix1,c,d,r+1,p)
    if r>p:
        return 0
    c,d=find()
    left(matrix,c,d)
    right(matrix,c,d)
    up(matrix,c,d)
    down(matrix,c,d)
print(matrix,end="\n")    
c=0
d=0
r=0
print("Enter the maximum depth for the tree: ",end="\n")
p=int(input())
create(np.array(matrix),c,d,r+1,p)
