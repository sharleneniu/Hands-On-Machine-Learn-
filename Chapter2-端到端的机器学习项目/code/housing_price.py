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

# download_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
download_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz"
local_path = "dataset/housing"
data_name = "housing.tgz"


def fetch_housing_data(data_url, data_path):
    # 判断dataset目录是否存在，不存在时创建
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    tar_path = os.path.join(data_path, data_name)
    urllib.request.urlretrieve(data_url, tar_path)
    tar_file = tarfile.open(tar_path)
    tar_file.extract(path=tar_path)
    tar_file.close()


def detect_file_is_exist(file_path, file_name):
    if not os.path.isdir(file_path):
        return False
    full_name = os.path.join(file_path, file_name)
    if not os.path.exists(full_name):
        return False
    return True


def load_data(file_path, file_name):
    csv_path = os.path.join(file_path, file_name)
    return pd.read_csv(csv_path)

if __name__ == '__main__':
    
