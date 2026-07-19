def backspace(str1):
    for i in range(0,len(str1)):
        place = 0
        while True:
            place = str1[i].find('<')
            if place == -1:
                break
            elif place == 0:
                str1[i] = str1[i][1:]
            else:
                str1[i] = str1[i][:place-1] + str1[i][place+1:]
    return str1

str1 = ''
text = []
while True:
    str1 = input()
    if str1 == 'EOF':
        break
    text.append(str1)

str2 = ''
ans = []
while True:
    str2 = input()
    if str2 == 'EOF':
        break
    ans.append(str2)

ans = backspace(ans)
text = backspace(text)

counts = 0
for i in range(0,len(text)):
    if i >= len(ans):
        break
    if len(text[i]) > len(ans[i]):
        for j in range(0,len(ans[i])):
            if text[i][j] == ans[i][j]:
                counts += 1
    else:
        for j in range(0,len(text[i])):
            if text[i][j] == ans[i][j]:
                counts += 1
                
time = int(input())
kpm = counts / time * 60
kpm = int(kpm + 0.5)
print(kpm)