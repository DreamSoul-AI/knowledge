# PyTorch

<h4 align="center">
    <p>
        <a href="README.md">English</a> |
        <b>中文</b>
    </p>
</h4>

## 目录
1. [简介](#简介)
2. [设置 PyTorch](#设置-pytorch)
    - [安装](#安装)
    - [验证安装](#验证安装)
3. [使用张量](#使用张量)
    - [创建张量](#创建张量)
    - [张量操作](#张量操作)
    - [将张量移动到 GPU](#将张量移动到-gpu)
4. [构建简单的神经网络](#构建简单的神经网络)
    - [定义模型](#定义模型)
    - [定义损失函数和优化器](#定义损失函数和优化器)
5. [训练模型](#训练模型)
6. [评估模型](#评估模型)
7. [保存和加载模型](#保存和加载模型)
8. [下一步](#下一步)

---

## 简介

本教程将引导您了解 PyTorch 的基础知识，这是一个功能强大的 Python 深度学习库。我们将介绍如何设置 PyTorch、使用张量、构建一个简单的神经网络等。到最后，您将具备基本的 PyTorch 知识，能够构建和训练自己的模型。

## 设置 PyTorch

在开始使用 PyTorch 之前，您需要在系统上安装它。

### 安装

要安装 PyTorch，请访问[官方 PyTorch 安装指南](https://pytorch.org/get-started/locally/)。此页面提供了针对不同平台和硬件配置（CPU 或 GPU）的详细安装说明。请按照与您的系统匹配的步骤进行操作，以确保顺利安装。

### 验证安装

要验证 PyTorch 是否正确安装，请打开一个 Python Shell 并尝试导入它：

```python
import torch

print(torch.__version__)  # 这将打印已安装的 PyTorch 版本
```

如果此命令运行无误，则表示 PyTorch 已成功安装。

## 使用张量

张量是 PyTorch 中的基本构建块。类似于 NumPy 数组，它们用于在神经网络中构建和操作数据。

### 创建张量

```python
import torch

# 创建一个填充了零的张量
x = torch.zeros(5, 3)
print(x)

# 创建一个填充了随机值的张量
y = torch.rand(5, 3)
print(y)

# 从列表创建张量
z = torch.tensor([[1, 2], [3, 4]])
print(z)
```

### 张量操作

PyTorch 提供了多种操作来操作张量：

```python
# 加法
result = x + y
print(result)

# 原地加法
y.add_(x)
print(y)

# 矩阵乘法
result = torch.mm(z, z.t())
print(result)

# 元素级乘法
result = x * y
print(result)
```

### 将张量移动到 GPU

如果您有可用的 GPU，您可以将张量移动到 GPU 以加快计算速度：

```python
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = x.to(device)
    y = y.to(device)
    print(x + y)
```

## 构建简单的神经网络

接下来，我们将使用 PyTorch 的 `torch.nn` 模块构建一个基本的神经网络。

### 定义模型

```python
import torch.nn as nn
import torch.nn.functional as F

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # 784 个输入特征，128 个输出特征
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)   # 10 个输出类别

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = SimpleNN()
print(model)
```

### 定义损失函数和优化器

```python
import torch.optim as optim

criterion = nn.CrossEntropyLoss()  # 结合了 softmax 和交叉熵损失
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降
```

## 训练模型

为了训练模型，我们将使用一个简单的训练循环。训练过程包括将数据反复传递给模型，计算损失，并使用梯度下降更新模型权重。有关梯度下降和模型训练的详细信息，您可以参考此 [PyTorch 模型训练教程](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html)。

这是一个基本的训练循环：

```python
# 假设您有一个 DataLoader 提供图像和标签的批次
for epoch in range(5):  # 训练5个周期
    running_loss = 0.0
    for images, labels in train_loader:
        # 展平图像
        images = images.view(images.shape[0], -1)
        
        # 将参数梯度归零
        optimizer.zero_grad()
        
        # 前向传播
        outputs = model(images)
        
        # 计算损失
        loss = criterion(outputs, labels)
        
        # 反向传播和优化
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f"Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}")
```

## 评估模型

训练后，评估模型在测试数据集上的性能：

```python
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images = images.view(images.shape[0], -1)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'模型在测试图像上的准确率: {100 * correct / total} %')
```

## 保存和加载模型

您可以将训练好的模型保存到磁盘，并在以后加载它：

```python
# 保存
torch.save(model.state_dict(), 'model.pt')

# 加载
model = SimpleNN()
model.load_state_dict(torch.load('model.pt'))
```

## 下一步

本教程介绍了 PyTorch 的基础知识。为了加深理解，您可以考虑探索以下主题：

- **自定义数据集和数据加载器**：学习如何处理不同类型的数据。
- **高级神经网络架构**：尝试构建更复杂的模型，如卷积神经网络（CNN）或循环神经网络（RNN）。
- **迁移学习**：使用预训练模型进行图像分类等任务。
- **超参数调整**：实验不同的学习率、批量大小和优化器。
- **RPipe**：您可以探索 [RPipe](https://github.com/diaoenmao/RPipe) 研究管道，这是一个端到端的解决方案，涵盖了设置实验脚本、构建数据集和模型、训练和评估模型，以及保存和处理最终结果。此资源提供了一个全面的框架来简化您使用 PyTorch 进行研究和实验的过程。

有关更多教程和详细文档，请访问 [官方 PyTorch 网站](https://pytorch.org/tutorials/)。
