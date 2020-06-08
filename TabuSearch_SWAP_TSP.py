# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:22:10 2020

@author: yangz
"""

import random 
import numpy as np
from math import exp
import copy

def distance_calculation(city1, city2):
    vec1 = np.array(city1)
    vec2 = np.array(city2)
    dis = np.linalg.norm(vec1-vec2)
    #print(dis)
    return dis

def path_distance_calculation(path, coor_dict, N):
    path_dis = distance_calculation(coor_dict[path[0]], coor_dict[path[N-1]])
    for n in range(N-1):
        path_dis += distance_calculation(coor_dict[path[n]], coor_dict[path[n+1]])
    return path_dis

def acceptance(new_path, cur_cost, cur_path, coor_dict, T, N):
    new_cost = path_distance_calculation(new_path, coor_dict, N)
    if new_cost <= cur_cost:
        cur_path = copy.deepcopy(new_path)
        cur_cost = copy.deepcopy(new_cost)
    else: 
        prob_th = exp((cur_cost-new_cost)/T) 
        if prob_th > random.random():
            cur_path = copy.deepcopy(new_path)
            cur_cost = copy.deepcopy(new_cost)
    return [cur_path, cur_cost]
            
if __name__ == '__main__': 
    citys = [[1304, 2312], [3639, 1315], [4177, 2244], [3712, 1399], [3488, 1535],
             [3326, 1556], [3238, 1229], [4196, 1004], [4312, 790], [4386, 570],
             [3007, 1970], [2562, 1756], [2788, 1491], [2381, 1676], [1332, 695],
             [3715, 1678], [3918, 2179], [4061, 2370], [3780, 2212], [3676, 2578],
             [4029, 2838], [4263, 2931], [3429, 1908], [3507, 2367], [3394, 2643],
             [3439, 3201], [2935, 3240], [3140, 3550], [2545, 2357], [2778, 2826],
             [2370, 2957]]  
    N = len(citys)
    keys = [i for i in range(N)] 
    coor_dict = dict(zip(keys, citys))
    L = 100
    
    cur_path = [i for i in range(N)]
    random.shuffle(cur_path)
    cur_cost = path_distance_calculation(cur_path, coor_dict, N)
    cur_lowest_cost = copy.deepcopy(cur_cost)
    tabu_list = []
    for i in range(L):
        for n1 in range(N-1):
            for n2 in range(n1, N):
                new_path = copy.deepcopy(cur_path)
                new_path[n1], new_path[n2] = new_path[n2], new_path[n1]
                if new_path in tabu_list:
                    continue
                new_cost = path_distance_calculation(new_path, coor_dict, N)                
                if new_cost < cur_lowest_cost:
                    cur_lowest_path = copy.deepcopy(new_path)
                    cur_lowest_cost = copy.deepcopy(new_cost)
        tabu_list.append(copy.deepcopy(cur_lowest_path))
        cur_path = copy.deepcopy(cur_lowest_path)
        cur_cost = copy.deepcopy(cur_lowest_cost)
        print("total distance", cur_cost)

    print(cur_path)
    print("total distance", cur_cost)
            
            
            