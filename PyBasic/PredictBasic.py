def linear_predict(x,w,b):
    return x*w+b

x = [1,2,3,4,5]
y_true = [2,4,6,8,10]
y_pred = [0,0,0,0,0]
w = float(input())
b = float(input())

print(f"y为:{y_true}")

for i in range(0,5):
    y_pred[i] = linear_predict(x[i],w,b)
residual = [round((y_pred[j]-y_true[j]) ** 2, 2)for j in range(0,5)]
print(f"y预测为:{y_pred}")
print(f"误差方差列表为:{residual}")

s = 0
times = 0
for i in residual:
    s += i
    times += 1
else:
    s = s / times
del times

print(f"平均数为:{s}")
