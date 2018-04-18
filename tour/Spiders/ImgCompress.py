# coding:utf-8
'''
    脚本功能： 采用多进程压缩图片
    对1180张图片进行压缩 364.4M  ->  244M
'''
import os
import tinify
from operator import itemgetter
from multiprocessing import Pool


img_paths = [os.path.join('imgs/', filename) for filename in os.listdir('imgs/') if filename.endswith('.png')]
img_size = sorted([(p, os.path.getsize(p)) for p in img_paths], key=itemgetter(1), reverse=True)


def compress(args):
    path, j = args
    print round(j * 1.0 / 1000, 1), 'k'
    tinify.key = 'h0ErL5tzh-FPrA1Oq6J4Vaoh6jhYPI4_'
    tinify.from_file(path).to_file(path)


p = Pool(10)
p.map(compress, img_size)
