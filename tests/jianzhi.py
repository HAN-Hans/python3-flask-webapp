""" NoteBook
https://github.com/CyC2018/Interview-Notebook/blob/master/notes/
@file: jianzhi.py
@time: 2018/8/16 上午10:43
@author: hx
@contact: hx@spsp-it.com
@desc: 巡查功能所用到的各类数据模型
@author: han
"""


""" 1. 题目描述
在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字是重复的，也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为 7 的数组 {2, 3, 1, 0, 2, 5}，那么对应的输出是第一个重复的数字 2。

要求复杂度为 O(N) + O(1)，也就是时间复杂度 O(N)，空间复杂度 O(1)。因此不能使用排序的方法，
也不能使用额外的标记数组。牛客网讨论区这一题的首票答案使用 nums[i] + length 来将元素标记，
这么做会有加法溢出问题。

"""


def duplicate(arr):
    if not arr:
        return False
    for i in range(len(arr)):
        while arr[i] != i:
            p = arr[i]
            if arr[i] == arr[p]:
                print(p)
                return p
            arr[i], arr[p] = arr[p], arr[i]


a = [2, 3, 1, 0, 2, 5]
duplicate(a)


""" 题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.

"""


def find(matrix, num):
    x = len(matrix[0])
    y = len(matrix)
    if not x and not y:
        print("error, ", num)
        return False
    i = 0
    j = y - 1
    while i < x and j >= 0:
        if matrix[i][j] == num:
            print("found, ", num)
            return True
        elif num > matrix[i][j]:
            i += 1
        else:
            j -= 1
    print("nut found, ", num)
    return False


m = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
find(m, 8)


""" 题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为 We Are Happy. 
则经过替换之后的字符串为 We%20Are%20Happy。
"""

def fill(s):
    print(s)
    p = s.replace(' ', '%20')
    print(p)


s = "We Are Happy"
fill(s)

