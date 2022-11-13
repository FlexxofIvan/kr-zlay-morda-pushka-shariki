#1.#
def f(n):
    if n < 10:
        return -1
    else:
        s = str(n)
    return int(s[-2])
#2.#
def f(s):
    s1 = ''.join(filter(str.isalpha, s)).lower()
    return s1[::-1] == s1
#3.#
def split(s):
    return [char for char in s]
def min_ch(s):
    if s > 0:
        p = 1
    else:
        p = -1
    s = split(str(s))
    s = sorted(s)
    for i in range(len(s)):
        if int(s[i]) > 0:
            l = i
            break
    print(s)
    return int(s[l] + "".join(s[1:l]) + '0' + "".join(s[l + 1:])) * p
#4.#
def split(s):
    return [char for char in s]
def min_ch(s):
    if s > 0:
        p = 1
    else:
        p = -1
    s = split(str(s))
    s = sorted(s)
    for i in range(len(s)):
        if int(s[i]) > 0:
            l = i
            break
    print(s)
    return int(s[l] + "".join(s[1:l]) + '0' + "".join(s[l + 1:])) * p
#№1 numpy (file 2)#
import numpy as np
def n1(a: np.ndarray, b: np.ndarray):
    c = 0
    d = 0
    for i in range(len(a)):
        c = c+a[i]**2
        d = d+b[i]**2
    b = np.transpose(b)
    f = np.dot(a,b)/np.sqrt(c*d)
    return np.rad2deg(np.arccos(f))
#5.file2#
import numpy as np
def matrix(a: np.array, b: np.array):
    b = np.transpose(b)
    return a.dot(b)
#6.file2#
import numpy as np
def f (a: np.array, b: np.array):
    b1 = np.transpose(b)
    a1 = np.transpose(a)
    c = a.dot(b1)
    l = a.dot(a1)
    d = b.dot(b1)
    return np.arccos(c/(l*d))
#№10.#
def n10(s):
    str = open(s, "r").read().lower()
    f = {}
    n = 0
    for c in str:
       if ord('a') <= ord(c) <= ord('z'):
           x = f.get(c, 0)
           f[c] = x + 1
           n += 1
    for key in f:
        f[key] = f[key] / n
    return f
#№1.1#
import pandas as pd
f = pd.read_csv('use.csv')
d=dict()
# пункт 1
d['number_of students']=len(f[(~f['Математика'].isna())|(~f['Физика'].isna())]|(~f['Русский язык'].isna()))
# №2 из пдф-файла
import pandas as pd
def pandas_task2(a: np.ndarray, n: int) -> np.ndarray:
    b, c, d = a.split(".")
    td = datetime.date(int(b), int(c), int(d))
    sd = datetime.date(1, 1, 1)
    diff = sd - td
    diff = str(diff)
    return diff[1:diff.rfind(",")]