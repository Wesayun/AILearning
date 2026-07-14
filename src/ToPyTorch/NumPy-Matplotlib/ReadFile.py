#在终端中运行，导致目录需要从终端读取的根目录开始

with open('AILearning/ToPyTorch/NumPy-Matplotlib/material/numbers.txt','r') as file1:
    str = file1.readlines()
    result = sum(int(char) for char in str)
print(result)