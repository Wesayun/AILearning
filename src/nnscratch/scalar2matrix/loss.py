import numpy as np
def compute_loss(scores,y_true):
    p = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)
    #注意这里是数组运算，keepdims是保持维度参数方便后续广播相除
    n = p.shape[0]  
    #p的行数
    loss = -np.log(p[np.arange(n),y_true])
    #这里使用高级索引，也就是数组逐元素配对
    return loss
    #此处输出的是每张图片的损失，实际应用可取平均输出标量