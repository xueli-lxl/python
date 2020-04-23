#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 13:04
# @Author  : xueli
# @Software: win10 Tensorflow1.13.1 python3.6.3
import time

def func(graph,s):#graph图  s指的是开始结点
    path =[]
    for x1 in graph[s]:
        if x1 > s:
            try:
                nodes2 = graph[x1]
            except KeyError as e:
                pass
            else:
                for x2 in nodes2:
                    if x2 > s:
                        try:
                            nodes3 = graph[x2]
                        except KeyError as e:
                            pass
                        else:
                            for x3 in nodes3:
                                if s == x3:
                                    A = [s,x1,x2]
                                    if len(set(A)) == len(A):
                                        path.append(A)
                                elif x3 > s:
                                    try:
                                        nodes4 = graph[x3]
                                    except KeyError as e:
                                        pass
                                    else:
                                        for x4 in nodes4:
                                            if s == x4:
                                                A = [s,x1,x2,x3]
                                                if len(set(A)) == len(A):
                                                    path.append(A)
                                            elif x4 > s:
                                                try:
                                                    nodes5 = graph[x4]
                                                except KeyError as e:
                                                    pass
                                                else:
                                                    for x5 in nodes5:
                                                        if s == x5:
                                                            A = [s,x1,x2,x3,x4]
                                                            if len(set(A)) == len(A):
                                                                path.append(A)
                                                        elif x5 > s:
                                                            try:
                                                                nodes6 = graph[x5]
                                                            except KeyError as e:
                                                                pass
                                                            else:
                                                                for x6 in nodes6:
                                                                    if s == x6:
                                                                        A = [s,x1,x2,x3,x4,x5]
                                                                        if len(set(A)) == len(A):
                                                                            path.append(A)
                                                                    elif x6 > s:
                                                                        try:
                                                                            nodes7 = graph[x6]
                                                                        except KeyError as e:
                                                                            pass
                                                                        else:
                                                                            for x7 in nodes7:
                                                                                if s == x7:
                                                                                    A = [s,x1,x2,x3,x4,x5,x6]
                                                                                    if len(set(A)) == len(A):
                                                                                        path.append(A)
                                                                                    else:
                                                                                        break
    return path

def savePredict(AA2):
    t2 = time.time()
    with open(result_name, 'w') as f:
        f.write(str(len(dd))+'\n')
        for aa in AA2:
            ww = str(aa)
            q1 = ww.strip(']')
            qq = q1.strip('[')
            bb = qq.replace(" ", "")
            f.write(str(bb)+"\n")
    print('write_time', time.time() - t2)
if __name__ == '__main__':
    t1 = time.time()
    file_name = "./data/test_data.txt"
    result_name = "result.txt"
    with open(file_name) as f:
        a = []
        c = []
        for line in f.readlines():
            line = line.strip('\n')  # 去掉换行符\n
            b = line.split(',')  # 将每一行以空格为分隔符转换成列表
            a.append(int(b[0]))
            c.append(int(b[1]))
    print('read_time', time.time() - t1)
    graph = {}
    data_list = [a,c]
    for x in range(len(a)):
        if a[x] in graph:
            graph[a[x]] += [c[x]]
        else:
            graph[a[x]] = [c[x]]
    s = sorted(graph.keys())
    t4 = time.time()
    dd = []
    for i in s:
        d = func(graph, i)
        if d != []:
            for ii in d:
                dd.append(ii)
    dd.sort()
    print('func_time', time.time() - t4)
    AA2 = sorted(dd, key=lambda i: len(i), reverse=False)
    print(len(dd))
    savePredict(AA2)
    print('总时:', time.time() - t1)

