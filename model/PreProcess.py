import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# 导入源数据文件，包含列为dispute_id,content,outline,outline_class1,outline_class2,outline_class3
df = pd.read_csv('../data/appeal_catagory.csv')
print(df.head())

# 取某列和多列数据,单列[],多列[[]]
dispute_id = df[['dispute_id','outline_class1']]
print(dispute_id)

# 取某行和多行数据
row2=df[0:2]
#print(row2)

# 某列的数据统计，包含排序和汇总数量、各类型占比
outline_class1 = df['outline_class1']
print(outline_class1.sort_values())
print(outline_class1.describe())
print(outline_class1.count())

dispute_id.groupby(outline_class1,axis=0)
# 数据可视化
sns.barplot(outline_class1)
plt.show()

