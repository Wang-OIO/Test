#!/usr/bin/python3
import requests
import math
import random
from functools import reduce

# ---生成器---
# def ga():
#    g = ( x * x for x in range(10))
#    a = [n for n in g]
#    return a
# print(ga())


# ---随机数生成一个多位整数---
# def ran():
#    id = ''.join(str(random.choice(range(10))) for _ in range(10))  #获取10位随机整数
#    return id
# print(ran())

# ---map高级函数---
# # def f(x):
# #     return x * x
# #     r = map(f,[1,2,3,4,5,6,7,8,9])
# #     print(list(r))


# ---二分查找---
# def binary_search(list,item,low,high):
#     # low = 0
#     # high = len(list) - 1
#     while low <= high:
#         mid = int((low + high)/2)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#             return binary_search(list,item,low,high)
#         else:
#             low = mid + 1
#             return binary_search(list, item, low, high)
#         if low > high:
#             return  None
# my_list = [1,3,5,7,9,11,34,45,56]
# print(binary_search(my_list,56,0,len(my_list)))


# ---reduce函数---
# def fn(x, y):
#    return x * 10 + y
# print(reduce(fn,[1,3,5,7,9]))

# ---输入名称规范，首字母大写---
# def normalize(name):
#    return name[0].upper() + name[1:].lower()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


def heihei(asd):
    return asd[0].upper() + asd[1:].lower()
L2 = list(map(heihei(['dshAhgc'])))
print(L2)

