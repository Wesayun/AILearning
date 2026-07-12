import matplotlib.pyplot as plt
import numpy as np
'''
plt.plot([1,2,3],[1,4,9])
epochs = [1,2,3,4,5]
loss1 = [2,4,7,11,24]
loss2 = [4,6,8,11,13]
plt.xlabel("Epoch"); plt.ylabel("Loss"); plt.title("Training Curve")
plt.plot(epochs, loss1, label="train")
plt.plot(epochs, loss2, label="val")
plt.legend()
plt.show()
'''

x = np.linspace(0,10,100)
y = x ** 2
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,label='function1')
plt.show()