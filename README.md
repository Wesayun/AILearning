# AILearning  
## Python基础  
- 类的基础  
  ClassBasic.py  
- 模拟"前向传播"和"计算损失"  
  PredictBasic.py  
  用列表推导式计算每个预测值的"误差平方" (y_pred - y_true)²
- Numpy入门-数组与矩阵  
  ArrayMatrix.py  
- Numpy进阶-矩阵乘法  
  MatrixMultiply.py  
  NumPy更快：
    1. 向量化运算：一次性操作整个数组，无需Python循环;  
    2. 类型统一：所有元素类型相同，无需类型检查;  
    3. 连续内存：所有元素在内存中紧密排列;  
    4. 预编译的C代码：a + b 调用的是C语言实现的函数;  
    5. SIMD优化：现代CPU一条指令处理多个数据;  

  Python列表更慢:  
    1. Python是动态类型，每次都要检查变量类型;  
    2. 循环由Python解释器逐行执行（慢）;  
    3. 每个元素是独立的Python对象（内存不连续）;
    4. 每次加法都创建新对象;  

- Matplotlib-损失曲线  
- 字典实现两数之和与反转链表  
- 异常+文件读写  