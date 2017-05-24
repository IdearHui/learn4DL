# -*- coding: UTF-8 -*-
import os
import struct


class Loader(object):
    """
    数据加载器基类
    """

    def __init__(self, path, count):
        """
        初始化加载器
        path: 数据文件路径
        count: 文件中的样本个数
        """
        self.path = path
        self.count = count

    def get_file_content(self):
        """
        读取文件内容
        """
        print os.getcwd()
        f = open(self.path, 'rb')
        content = f.read()
        f.close()
        return content

    def to_int(self, byte):
        """
        将unsigned byte字符转换为整数
        :param byte:
        """
        return struct.unpack('B', byte)[0]
