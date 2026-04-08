# Hello World Collection 🎉

> 我的编程入门项目合集 - 包含 R 和 Python 两种语言
>
> 🤖 **本项目由 [WorkBuddy](https://www.codebuddy.cn/) AI助手生成**

[![R](https://img.shields.io/badge/R-4.0+-276DC3?logo=r&logoColor=white)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![WorkBuddy](https://img.shields.io/badge/Generated%20by-WorkBuddy-blueviolet)](https://www.codebuddy.cn/)

---

## 📖 项目简介

这是一个简单的编程入门项目合集，展示了 **R语言** 和 **Python** 的基本语法和功能。适合编程初学者参考学习，对比两种语言的特点。

### 🤖 关于本项目

本项目完全由 **WorkBuddy AI助手** 协助创建，包括：
- ✅ 代码文件编写（R和Python版本）
- ✅ 完整的README文档
- ✅ Git仓库初始化和配置
- ✅ SSH Key配置指导
- ✅ GitHub仓库推送

WorkBuddy 是一个智能AI助手，可以帮助你完成编程、写作、数据分析等各种任务。

## 🚀 快速开始

### 环境要求

| 语言 | 版本要求 | 推荐IDE |
|------|---------|---------|
| **R** | 4.0+ | [RStudio](https://posit.co/download/rstudio-desktop/) |
| **Python** | 3.8+ | [VS Code](https://code.visualstudio.com/) 或 [PyCharm](https://www.jetbrains.com/pycharm/) |

### 安装指南

#### R语言
```bash
# macOS (使用 Homebrew)
brew install r

# 或从官网下载
# https://cran.r-project.org/
```

#### Python
```bash
# macOS (使用 Homebrew)
brew install python

# 或从官网下载
# https://www.python.org/downloads/
```

---

## 📂 文件结构

```
hello-world-r/
├── hello_world.R        # R语言版本
├── hello_world.py       # Python版本
├── README.md            # 项目说明文档
└── .gitignore           # Git忽略文件
```

---

## 📝 代码对比

### 功能对比表

| 功能 | R语言 | Python |
|------|-------|--------|
| 打印输出 | `print('Hello')` | `print("Hello")` |
| 获取时间 | `Sys.time()` | `datetime.datetime.now()` |
| 字符串拼接 | `paste('a', 'b')` | `f"{a} {b}"` 或 `"{} {}".format(a, b)` |
| 列表/向量 | `c(1, 2, 3)` | `[1, 2, 3]` |
| 字典/列表 | `list(a=1, b=2)` | `{"a": 1, "b": 2}` |

---

## 🔷 R语言版本

### 运行方式

```bash
# 在终端中运行
Rscript hello_world.R
```

或在RStudio中：
1. 打开 `hello_world.R` 文件
2. 点击 "Run" 按钮或按 `Ctrl+Enter` (Windows) / `Cmd+Enter` (Mac)

### 代码内容

```r
# 打印问候语
print('Hello, World!')

# 获取当前时间
current_time <- Sys.time()
print(paste('当前时间:', current_time))

# 简单的计算
result <- 1 + 1
print(paste('1 + 1 =', result))
```

### R语言特点
- ✅ 统计分析和数据可视化强大
- ✅ 丰富的生物信息学包（Bioconductor）
- ✅ 学术界广泛使用
- ✅ 适合医学统计和流行病学研究

---

## 🐍 Python版本

### 运行方式

```bash
# 在终端中运行
python hello_world.py

# 或
python3 hello_world.py
```

或在VS Code/PyCharm中：
1. 打开 `hello_world.py` 文件
2. 点击运行按钮或右键选择 "Run Python File"

### 代码内容

```python
#!/usr/bin/env python3
import datetime

def main():
    # 打印问候语
    print("Hello, World!")
    
    # 获取当前时间
    current_time = datetime.datetime.now()
    print(f"当前时间: {current_time}")
    
    # 简单的计算
    result = 1 + 1
    print(f"1 + 1 = {result}")
    
    # Python特色：列表推导式
    squares = [x**2 for x in range(1, 6)]
    print(f"1-5的平方: {squares}")
    
    # Python特色：字典
    info = {"语言": "Python", "版本": "3.x"}
    for key, value in info.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
```

### Python特点
- ✅ 语法简洁，易读易写
- ✅ 机器学习/深度学习首选（TensorFlow, PyTorch）
- ✅ 丰富的科学计算库（NumPy, Pandas, SciPy）
- ✅ 适合医学AI和影像分析

---

## 🎯 学习目标

通过本项目，你可以学习：

### 通用编程概念
- ✅ 变量和数据类型
- ✅ 函数定义和调用
- ✅ 基本输入输出
- ✅ 时间和日期处理

### R语言特有
- ✅ 向量操作
- ✅ 统计函数
- ✅ 数据框（data.frame）

### Python特有
- ✅ 列表推导式
- ✅ 字典操作
- ✅ f-string格式化
- ✅ 面向对象编程基础

---

## 📚 学习资源

### R语言
- [R官方网站](https://www.r-project.org/)
- [R for Data Science](https://r4ds.had.co.nz/)
- [Bioconductor](https://www.bioconductor.org/) - 生物信息学包
- [R语言入门教程](https://www.runoob.com/r/r-tutorial.html)

### Python
- [Python官方网站](https://www.python.org/)
- [Python官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [NumPy文档](https://numpy.org/doc/)
- [Pandas文档](https://pandas.pydata.org/docs/)

### 医学AI/数据分析
- [scikit-learn](https://scikit-learn.org/) - 机器学习
- [SimpleITK](https://simpleitk.org/) - 医学影像处理
- [MONAI](https://monai.io/) - 医学AI框架

---

## 🔧 进阶扩展

### R语言扩展
```r
# 1. 数据框操作
df <- data.frame(
  name = c("Alice", "Bob"),
  age = c(25, 30)
)
print(df)

# 2. 简单统计
numbers <- c(1, 2, 3, 4, 5)
print(mean(numbers))
print(sd(numbers))

# 3. 基础绘图
plot(1:10, (1:10)^2, type="l", main="y = x^2")
```

### Python扩展
```python
# 1. 使用NumPy进行数值计算
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())

# 2. 使用Pandas处理数据
import pandas as pd
df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "age": [25, 30]
})
print(df)

# 3. 读取CSV文件
data = pd.read_csv("data.csv")
print(data.head())
```

---

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

---

## 👤 作者

**Dianzhe Tian** (tiandianzhe)

- GitHub: [@tiandianzhe](https://github.com/tiandianzhe)
- 机构: Peking Union Medical College Hospital
- 研究方向: 医学AI、肝脏疾病、生物信息学

---

> 💡 **提示**: 这是我在GitHub上的第一个编程项目合集，标志着我的数据科学和医学AI学习之旅正式开始！

*Last updated: 2026-04-08*
