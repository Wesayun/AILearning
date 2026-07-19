import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
import two_layer_nn as tln
import loss
from torchvision import datasets

mnist = datasets.MNIST(root='./data', train=True, download=True)
X = mnist.data.numpy()[:1000].astype(np.float32) / 255.0    # 1000张图片
y = mnist.targets[:1000].long()           # 1000个标签

the_net = tln.two_layer_nn()

X_flat = X.reshape(X.shape[0], -1) 
scores = the_net.forward(X_flat)

losses = np.mean(loss.compute_loss(scores,y))
print(losses)

plt.bar(range(10), scores[0])
plt.xlabel('数字类别')
plt.ylabel('得分')
plt.title('模型对这张图片的预测得分')
plt.show()
print(y[0])