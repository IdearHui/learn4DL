# coding=utf-8
from bpnn.mnist.imgLoader import ImageLoader
from bpnn.mnist.lableLoader import LabelLoader


def get_training_data_set():
    """
    获得训练数据集
    """
    image_loader = ImageLoader('E:\\master\\algorithm\\nn\\bpnn\\mnist\\dataset\\train_images', 60000)
    label_loader = LabelLoader('E:\\master\\algorithm\\nn\\bpnn\\mnist\\dataset\\train-labels-idx1-ubyte', 60000)
    return image_loader.load(), label_loader.load()


def get_test_data_set():
    """
    获得测试数据集
    """
    image_loader = ImageLoader('E:\\master\\algorithm\\nn\\bpnn\\mnist\\dataset\\t10k-images-idx3-ubyte', 10000)
    label_loader = LabelLoader('E:\\master\\algorithm\\nn\\bpnn\\mnist\\dataset\\t10k-labels-idx1-ubyte', 10000)
    return image_loader.load(), label_loader.load()
