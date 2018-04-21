# coding:utf-8
import math


# 计算两个物品间的相似度
def get_similarity(x, y, data):
    # x, y 是两个物品. data 是数据集
    num_x = 0
    num_y = 0
    num_xy = 0
    for v in data.values():
        if x in v: num_x += 1
        if y in v: num_y += 1
        if x in v and y in v: num_xy += 1
    sim = num_xy / math.sqrt(num_x * num_y)
    return sim


if __name__ == '__main__':
    U = ['c', 'd', 'e', 'g']
    A = ['a', 'b', 'd']
    B = ['a', 'c', 'f']
    C = ['b', 'c', 'g']
    D = ['c', 'd', 'e']
    E = ['a', 'b', 'c']
    data = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}
    print get_similarity('a', 'c', data)
