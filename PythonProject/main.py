import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 模块 1：CSV 数据读取
# 必做
# 程序启动后自动读取指定的 CSV 文件，并检查数据能否正常加载。
#
# 需要实现：
# - 读取 CSV，正确处理中文编码
# - 显示数据行数、列数和字段名称
# - 检查必需字段是否存在
# - 检查数值列、分类列的数据类型
# - 文件不存在或字段缺失时，给出明确提示

# 1. 读取CSV
data = pd.read_csv("uniqlo.csv", encoding="utf-8")

# 2. 显示数据行数、列数和字段名称
x, y = data.shape
tag = data.columns
print(f"行数：{x}\n列数：{y}\n")
