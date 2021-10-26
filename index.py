import sys
n=int(sys.argv[1])
i=0
for j in range(1, n-1):
    if n%j==0:
        i=i+j
    else:
        i=i
if i==n:
    print("Le nombre "+sys.argv[1]+" parfait!")
else:
    print("Le nombre "+sys.argv[1]+" n'est pas parfait!")
    print("Ses diviseurs sont : ", end="")
    for k in range(1, n-1):
        if n%k==0:
            print(str(k), end=" ")
