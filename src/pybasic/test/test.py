n = int(input())
n_list = list(str(n))
n_list.reverse()
if n < 0:
    n_list.pop()
n_re = ''
for i in n_list:
    n_re = n_re + i
n_re = int(n_re)
if n < 0:
    print(-n_re)
else:
    print(n_re)