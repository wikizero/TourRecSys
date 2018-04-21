# coding:utf-8
import math
from collections import OrderedDict


# 余弦相似度计算
def getSimilarity1(x, y):
    # print len([i for i in x if i in y])
    sim = len(set(x) & set(y))
    return sim / math.sqrt(len(x) * len(y))
    # return sim/((len(x)*len(y)) ** 0.5)


def getSimilarity(u, data):  # u为一个用户感兴趣的物品集  data（字典）为其他所有用户的数据集: {'用户ID':[用户感兴趣的物品列表]}
    sim_dct = {}
    for k, v in data.items():
        set_v = set(v)
        set_u = set(u)
        if u == v or set_v.issubset(set_u):
            continue  # 两个物品列表一样的过滤， 物品v集合属于物品u集合的过滤　

        # 余弦相似度计算
        intersection = len(set_v & set_u)
        if not intersection:
            continue  # u 与 v 没有交集的过滤
        sim = intersection / math.sqrt(len(u) * len(v))
        sim_dct[k] = sim
    return OrderedDict(sorted(sim_dct.items(), key=lambda x: x[1])[::-1])

    # return OrderedDict(sorted(sim_dct.items(), key=lambda x: x[1][:n])[::-1]) top n （获取前n个）


if __name__ == '__main__':
    # 计算下列用户的兴趣相似度
    U = ['c', 'd', 'e', 'g']
    A = ['a', 'b', 'd']
    B = ['a', 'c', 'f']
    C = ['b', 'c', 'g']
    D = ['c', 'd', 'e']
    E = ['a', 'b']
    data = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'U': U}
    for k, v in getSimilarity(U, data).items():
        print k, v
