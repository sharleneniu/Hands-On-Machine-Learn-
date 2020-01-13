#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/1/2020 4:22 下午
# @Author  : Niu Xue
# @Site    :
# @File    : housing_price.py
# @Software: PyCharm
import os
import tarfile
import pandas as pd
from six.moves import urllib
import matplotlib.pyplot as plt

# download_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz"
DATA_PATH = "dataset/housing"
TAR_NAME = "housing.tgz"
DATA_NAME = "housing.csv"


def fetch_housing_data(data_url, data_path):
    # 判断dataset目录是否存在，不存在时创建
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    tar_path = os.path.join(data_path, TAR_NAME)
    urllib.request.urlretrieve(data_url, tar_path)
    tar_file = tarfile.open(tar_path)
    # tar_file.extractall(path=data_path)
    tar_file.getmembers()
    tar_file.extract(DATA_NAME, path=data_path)
    tar_file.close()


def detect_file_is_exist(file_path, file_name):
    """判断文件是否存在"""
    if not os.path.isdir(file_path):
        return False
    full_name = os.path.join(file_path, file_name)
    if not os.path.exists(full_name):
        return False
    return True


def load_data(file_path, file_name):
    # if not detect_file_is_exist(file_path, file_name):
    fetch_housing_data(DOWNLOAD_ROOT, file_path)
    csv_path = os.path.join(file_path, file_name)
    return pd.read_csv(csv_path)


if __name__ == '__main__':

    data = pd.Series('Nan', index=[4, 5, 6, 1, 2])
    print(data.ix[2:])
    data = pd.Series('Nan', index=['a', 'b', 'c', 1, 2])
    print(data.ix[2:])

    housing = load_data(DATA_PATH, DATA_NAME)
    print(housing.head())
    print(housing.info())
    print(housing["ocean_proximity"].value_counts())
    print(housing.describe())
    housing.hist(bins=50, figsize=(20, 15))
    plt.show()
