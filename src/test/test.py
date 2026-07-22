dict = {}

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dict[(20,20,20)]
    if a < b and b < c:
        return(dict[(a,b,c-1)] + dict[(a,b-1,c-1)] - dict[(a,b-1,c)])
    else:
        return(dict[(a-1,b,c)] + dict[(a-1,b-1,c)] + dict[(a-1,b,c-1)] - dict[(a-1,b-1,c-1)])

for c in range(0,21):
    for b in range(0,21):
        for a in range(0,21):
            dict[(a,b,c)] = w(a,b,c)

while True:
    s = list(map(int,input().split()))
    a,b,c = s[0],s[1],s[2]
    ans = w(a,b,c)
    
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {ans}')