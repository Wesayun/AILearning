n = int(input())
list1 = input().split()
list1 = list(map(int,list1))
list1.sort()
counts = 0
seen = set()
for i in range(2,n):
    for j in range(0,i):
        if list1[i] - list1[j] in seen:
            print(list1[i],list1[j])
            counts += 1
        seen.add(j)
print(counts)