import numpy as np
import fully_connected as f_c
layer1 = f_c.LinearLayer(784,64)
layer2 = f_c.LinearLayer(64,10)
x = np.random.randn(1, 784)  # 模拟1张图片
h = layer1.forward(x)
h_relu = np.maximum(0, h)    # ReLU激活
scores = layer2.forward(h_relu)
print(scores.shape)  # 应该是 (1, 10)
