# Hello World in R 🎉

> 我的第一个R语言项目 - 开启数据科学之旅

[![R](https://img.shields.io/badge/R-4.0+-276DC3?logo=r&logoColor=white)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 项目简介

这是一个简单的R语言入门项目，展示了R语言的基本语法和功能。适合R语言初学者参考学习。

## 🚀 快速开始

### 环境要求

- **R** (版本 4.0 或更高) - [下载安装](https://cran.r-project.org/)
- 推荐使用 **RStudio** - [下载安装](https://posit.co/download/rstudio-desktop/)

### 运行代码

```bash
# 在终端中运行
Rscript hello_world.R
```

或在RStudio中：
1. 打开 `hello_world.R` 文件
2. 点击 "Run" 按钮或按 `Ctrl+Enter` (Windows) / `Cmd+Enter` (Mac)

## 📂 文件结构

```
hello-world-r/
├── hello_world.R    # 主程序文件
├── README.md        # 项目说明文档
└── .gitignore       # Git忽略文件
```

## 📝 代码说明

### `hello_world.R`

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

### 功能说明

| 功能 | 代码 | 输出示例 |
|------|------|---------|
| 打印文本 | `print('Hello, World!')` | `Hello, World!` |
| 获取时间 | `Sys.time()` | `2026-04-08 13:30:00 CST` |
| 简单计算 | `1 + 1` | `2` |

## 🎯 学习目标

通过本项目，你可以学习：

- ✅ R语言基本语法
- ✅ 使用 `print()` 函数输出信息
- ✅ 使用 `Sys.time()` 获取系统时间
- ✅ 使用 `paste()` 拼接字符串
- ✅ 基础数学运算

## 📚 R语言学习资源

### 官方资源
- [R官方网站](https://www.r-project.org/)
- [R文档](https://www.r-project.org/manuals.html)

### 推荐教程
- [R for Data Science](https://r4ds.had.co.nz/) (英文)
- [R语言入门教程](https://www.runoob.com/r/r-tutorial.html) (中文)

### 社区
- [Stack Overflow - R标签](https://stackoverflow.com/questions/tagged/r)
- [RStudio Community](https://community.rstudio.com/)

## 🔧 进阶扩展

你可以尝试修改代码，实现以下功能：

```r
# 1. 用户输入
name <- readline("请输入你的名字: ")
print(paste("你好,", name, "!"))

# 2. 条件判断
x <- 10
if (x > 5) {
  print("x 大于 5")
} else {
  print("x 小于或等于 5")
}

# 3. 循环
for (i in 1:5) {
  print(paste("第", i, "次循环"))
}

# 4. 创建向量
numbers <- c(1, 2, 3, 4, 5)
print(mean(numbers))  # 计算平均值
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

---

## 👤 作者

**tiandianzhe**

- GitHub: [@tiandianzhe](https://github.com/tiandianzhe)

---

> 💡 **提示**: 这是我在GitHub上的第一个R语言项目，标志着我的数据科学学习之旅正式开始！

*Last updated: 2026-04-08*
