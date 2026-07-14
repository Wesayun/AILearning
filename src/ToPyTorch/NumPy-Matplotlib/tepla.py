import numpy as np

def get_pos_int(b_str):
    while True:
        print(b_str)
        a_str = input('需要一个正整数：')
        try:
            a_str = int(a_str)
            if a_str > 0:
                return a_str
            else:
                print('输入的不是正数')
        except ValueError:
            print('输入的不是数字')

ay = get_pos_int('请输入矩阵A的行数')
ax = get_pos_int('请输入矩阵A的列数')
by = ax
print(f'矩阵B的行数必须与矩阵A列数相同，已设为{ax}')
bx = get_pos_int('请输入矩阵B的列数')

A = np.zeros((ay,ax))
B = np.zeros((by,bx))

for i in range(0,ay):
    for j in range(0,ax):
        A[i,j] = get_pos_int(f'请输入矩阵A的第{i+1}行，第{j+1}列的元素')
print(f'矩阵A为{A}')

for i in range(0,by):
    for j in range(0,bx):
        B[i,j] = get_pos_int(f'请输入矩阵B的第{i+1}行，第{j+1}列的元素')
print(f'矩阵B为{B}')

print('接下来进行矩阵乘法：')
print(f'矩阵A点乘矩阵B的结果为：{A@B}')