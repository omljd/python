n = int(input("Enter number of rows:")) #taking input from the user for number of rows 3
for i in range(1,n+1):  # i=1  n+1=3+1=4     1<4     i=2
    for j in range(1,i+1):    # j=1  i+1(1+1)     1<2    2<2
        print(j,end=" ")
    print()
