in1 = input().split()
long = in1[0];m = in1[1]
remov = set()
for i in range(0,int(m)):
    former = input().split()
    remov.union({i for i in range (int(former[0]),int(former[1])+1)})
print(int(long)-len(remov))