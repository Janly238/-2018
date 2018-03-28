#coding = utf-8
import sys 
for line in sys.stdin:
    a = line.split()
    n=int(a[0])
    L=int(a[1])
    for line in sys.stdin:
        a = line.split()
    b=[int(i) for i in a]
    locat=b.index(0)
    locat_min=min(locat,len(b)-locat-1)
    
    print(min(L,locat_min))