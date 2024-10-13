n=int(input())  ##TAKING INPUT FROM THE USER
for i in range(1,n+1):                     ##USING FOR LOOP FOR THE UPPER OUTER LOOP 
    print("  "*(n-i),end="",sep="")
    for j in range(1,i+1):
        print(j,end=" ",sep="")            ##PRINTING THE STARTING DIGITS IN THE UPPER HALF
    for k in range(i-1,0,-1):
        print(k,end=" ",sep="")           ##PRINTING THE ENDING DIGITS IN THE UPPER HALF
    print()
for i in range(n-1,0,-1):                  ##USING FOR LOOP FOR THE LOWER OUTER LOOP
    print("  "*(n-i),end="",sep="")
    for j in range(1,i+1):
        print(j,end=" ",sep="")             ##PRINTING THE STARTING DIGITS IN THE LOWER HALF
    for j in range(i-1,0,-1):
        print(j,end=" ",sep="")             ##PRINTING THE ENDING DIGITS IN THE LOWER HALF
    print()


'''       1                     #
        1 2 1                   #
      1 2 3 2 1                 #
    1 2 3 4 3 2 1               #        UPPER HALF
  1 2 3 4 5 4 3 2 1             #
1 2 3 4 5 6 5 4 3 2 1           #
  1 2 3 4 5 4 3 2 1         #
    1 2 3 4 3 2 1           #
      1 2 3 2 1             #    LOWERV HALF
        1 2 1               #
          1                 #
'''
##raman976
