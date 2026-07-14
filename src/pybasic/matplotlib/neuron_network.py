import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,3,4,5])
Y = np.array([2,4,6,8,10])
w = np.random.randn()
b = np.random.randn()


plt.xlabel('Epoch')
plt.ylabel('Loss_val')

epo = []
losval = []

for i in range(1,10002):
    y_pred = X * w + b
    loss = np.mean((y_pred - Y) ** 2)
    grad_w = np.mean(2 * X * (X * w + b - Y))
    grad_b = np.mean(2 * (X * w + b - Y))
    w -= 0.01 * grad_w
    b -= 0.01 * grad_b
    if i % 10 == 0:
        epo.append(i)
        losval.append(loss)

plt.plot(epo,losval,label='function1')
plt.show()

print(w)
print(b)    