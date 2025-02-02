n=int(input())
lenpr=0
for i in range(n,0,-1):
    s = ''.join(str(k) for k in range(i,0,-1))
    s += ''.join(str(k) for k in range(2,i+1))
    if lenpr==0:
        k=0
    else:
        k+=(lenpr-len(s))//2
    lenpr=len(s)
    print(' '*k+s)