#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World in Python
我的第一个Python项目
"""

import datetime


def main():
    """主函数：打印问候语和当前时间"""
    # 打印问候语
    print("Hello, World!")
    
    # 获取当前时间
    current_time = datetime.datetime.now()
    print(f"当前时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 简单的计算
    result = 1 + 1
    print(f"1 + 1 = {result}")
    
    # Python特色：列表推导式
    squares = [x**2 for x in range(1, 6)]
    print(f"1-5的平方: {squares}")
    
    # Python特色：字典
    info = {
        "语言": "Python",
        "版本": "3.x",
        "用途": "数据科学、AI、Web开发"
    }
    print(f"\n项目信息:")
    for key, value in info.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
