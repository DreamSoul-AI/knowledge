# PyTorch

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="README_zh.md">中文</a>
    </p>
</h4>

## Table of Contents
1. [Introduction](#introduction)
2. [Setting Up PyTorch](#setting-up-pytorch)
    - [Installation](#installation)
    - [Verify Installation](#verify-installation)
3. [Working with Tensors](#working-with-tensors)
    - [Creating Tensors](#creating-tensors)
    - [Tensor Operations](#tensor-operations)
    - [Moving Tensors to GPU](#moving-tensors-to-gpu)
4. [Building a Simple Neural Network](#building-a-simple-neural-network)
    - [Define the Model](#define-the-model)
    - [Define the Loss Function and Optimizer](#define-the-loss-function-and-optimizer)
5. [Training the Model](#training-the-model)
6. [Evaluating the Model](#evaluating-the-model)
7. [Saving and Loading the Model](#saving-and-loading-the-model)
8. [Next Steps](#next-steps)

---

## Introduction

This tutorial will guide you through the basics of PyTorch, a powerful deep learning library in Python. We’ll cover how to set up PyTorch, work with tensors, build a simple neural network, and more. By the end, you’ll have a foundational understanding of PyTorch, ready to build and train your own models.

## Setting Up PyTorch

Before we begin working with PyTorch, you'll need to install it on your system.

### Installation

To install PyTorch, please visit the [official PyTorch installation guide](https://pytorch.org/get-started/locally/). This page provides detailed instructions tailored to various platforms and hardware configurations (CPU or GPU). Follow the steps that match your system to ensure a smooth installation.

### Verify Installation

To verify that PyTorch is installed correctly, open a Python shell and try importing it:

```python
import torch

print(torch.__version__)  # This should print the installed PyTorch version
```

If this command runs without errors, PyTorch is successfully installed.

## Working with Tensors

Tensors are the fundamental building blocks in PyTorch. Similar to NumPy arrays, they are used for building and manipulating data in neural networks.

### Creating Tensors

```python
import torch

# Create a tensor filled with zeros
x = torch.zeros(5, 3)
print(x)

# Create a tensor filled with random values
y = torch.rand(5, 3)
print(y)

# Create a tensor from a list
z = torch.tensor([[1, 2], [3, 4]])
print(z)
```

### Tensor Operations

PyTorch provides a wide range of operations for manipulating tensors:

```python
# Addition
result = x + y
print(result)

# In-place addition
y.add_(x)
print(y)

# Matrix multiplication
result = torch.mm(z, z.t())
print(result)

# Element-wise multiplication
result = x * y
print(result)
```

### Moving Tensors to GPU

If you have a GPU available, you can move your tensors to the GPU for faster computations:

```python
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = x.to(device)
    y = y.to(device)
    print(x + y)
```

## Building a Simple Neural Network

Next, we’ll build a basic neural network using PyTorch’s `torch.nn` module.

### Define the Model

```python
import torch.nn as nn
import torch.nn.functional as F

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # 784 input features, 128 output features
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)   # 10 output classes

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = SimpleNN()
print(model)
```

### Define the Loss Function and Optimizer

```python
import torch.optim as optim

criterion = nn.CrossEntropyLoss()  # Combines softmax and cross-entropy loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent
```

## Training the Model

To train the model, we'll use a simple training loop. Training involves iteratively passing data through the model, calculating the loss, and updating the model weights using gradient descent. For more detailed information on gradient descent and model training, you can refer to this [PyTorch tutorial on training models](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html).

Here’s a basic training loop:

```python
# Assuming you have a DataLoader that provides batches of images and labels
for epoch in range(5):  # 5 epochs
    running_loss = 0.0
    for images, labels in train_loader:
        # Flatten images
        images = images.view(images.shape[0], -1)
        
        # Zero the parameter gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(images)
        
        # Compute the loss
        loss = criterion(outputs, labels)
        
        # Backward pass and optimize
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f"Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}")
```

## Evaluating the Model

After training, evaluate the model's performance on a test dataset:

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

print(f'Accuracy of the model on the test images: {100 * correct / total} %')
```

## Saving and Loading the Model

You can save your trained model to disk and load it later:

```python
# Save
torch.save(model.state_dict(), 'model.pt')

# Load
model = SimpleNN()
model.load_state_dict(torch.load('model.pt'))
```

## Next Steps

This tutorial introduces the basics of PyTorch. To deepen your understanding, consider exploring the following topics:

- **Custom Datasets and DataLoaders**: Learn to handle different types of data.
- **Advanced Neural Network Architectures**: Experiment with more complex models like CNNs or RNNs.
- **Transfer Learning**: Use pre-trained models for tasks like image classification.
- **Hyperparameter Tuning**: Experiment with different learning rates, batch sizes, and optimizers.
- **RPipe** you can explore the [RPipe](https://github.com/diaoenmao/RPipe) Research Pipeline for an end-to-end solution that includes setting up experiment scripts, building datasets and models, training and evaluating the model, and saving and processing final results. This resource provides a comprehensive framework to streamline your research and experimentation with PyTorch.

For more tutorials and detailed documentation, visit the [official PyTorch website](https://pytorch.org/tutorials/).
