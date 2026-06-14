# 1
# 22
# 333
# 4444
# 55555

def pattern1(n):
    for i in range(1,n+1):
        print(str(i)*i)

# *
# **
# ***
# ****
# *****

def pattern2(n):
    for i in range(1,n+1):
        print("*"*i)

# 1
# 12
# 123
# 1234
# 12345
def pattern3(n):
    for i in range(n):
        no=1
        for j in range(i+1):
            print(no,end=" ")
            no+=1
        print()

# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

def pattern4(n):
    for i in range(n,-1,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

#     *    
#    ***   
#   *****  
#  ******* 
# *********
def pattern5(n):
    for i in range(n):
        c="*"*(2*(i)+1)
        print(c.center(2*n-1))


#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********
#  ********* 
#   *******  
#    *****   
#     ***    
#      *

def pattern6(n):
    for i in range(n):
        c="*"*(2*(i)+1)
        print(c.center(2*n+1))
    for j in range(n,-1,-1):
        c="*"*(2*(j)+1)
        print(c.center(2*n+1))

# 1
# 01
# 101
# 0101
# 10101

def pattern7(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print("1",end="")
            else:
                print("0",end="")
        print()