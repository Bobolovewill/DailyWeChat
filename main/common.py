# coding=utf-8
"""
工具类
"""

import os
import yaml
from simplejson import JSONDecodeError
import hashlib

def get_yaml():
    """
    解析 yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_config.yaml')

    try:
        with open(path, 'r', encoding='utf-8') as file:
            config = yaml.load(file, Loader=yaml.Loader)

        return config
    except Exception as error:
        print(error)
        print('你的 _config.yaml 文件配置出错...')
    return None


def is_json(resp):
    """
    判断数据是否能被 Json 化。 True 能，False 否。
    :param resp: request.
    :return: bool, True 数据可 Json 化；False 不能 JOSN 化。
    """
    try:
        resp.json()
        return True
    except JSONDecodeError:
        return False

def md5_encode(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    encodedStr = md5.hexdigest().upper()
    return encodedStr

if __name__ == '__main__':
    get_yaml()