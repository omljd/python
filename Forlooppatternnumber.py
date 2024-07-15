n = int(input("Enter number of rows:")) #taking input from the user for number of rows 3
b=0
for i in range(n,0,-1):  # i=1  n+1=3+1=4     1<4     i=2
    b=b+1
    for j in range(1,i+1):    # j=1  i+1(1+1)     1<2    2<2
        print(b,end=" ")
    print()
