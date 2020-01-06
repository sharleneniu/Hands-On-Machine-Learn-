import matplotlib
import matplotlib.pyplot as plt
# import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import pandas as pd


def prepare_country_stats(oecd_bli, gdp_per_capita):
    # filter data
    # 筛选所有inequality == TOT 的数据
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    # 以index为新table的row index，以coulumns为新table的columns，以values为新table的values生成新table
    # 新table每一行表示当前country在不同indicator下的values
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    # 使用country生成新的index
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    # 移除这些index的数据
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]


# load data
oecd_data = pd.read_csv("oecd.csv", thousands=',')
gdp_data = pd.read_csv("gdp.xls", thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')
country_stats = prepare_country_stats(oecd_data, gdp_data)
X = np.c_[country_stats['GDP per capita']]
Y = np.c_[country_stats['Life satisfaction']]
country_stats.plot(kind='scatter', x='GDP per capita', y='Life satisfaction')
plt.show()

# select linear model
# 此处原本使用lin_model = sklearn.linear_model.LinearRegression()，会报错AttributeError: module 'sklearn' has no attribute 'linear_model'
# 原因：sklearn does not automatically import its subpackages.
# 使用 from sklearn.linear_model import LinearRegression
# 详情参考：https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?highlight=linearregression#sklearn.linear_model.LinearRegression
lin_model = LinearRegression().fit(X, Y)
X_new = [[22587]]
print(lin_model.predict(X_new))

# KNN算法：选取距离最近的n_neighbors个值，根据algorithm计算距离，然后求取平均值，其中n_neighbors，n_neighbors为方法入参
# 详情参考：https://zhuanlan.zhihu.com/p/44094614
k_neighbors = KNeighborsRegressor(n_neighbors=3).fit(X, Y)
print(k_neighbors.predict(X_new))
