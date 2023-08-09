import pickle
from functools import reduce

with open(input(), "rb") as f:
    num = int(input())
    data = pickle.load(f)
    if type(data) == list:
        total_num = min(lst) * max(lst)
    elif type(data) == dict:
        total_num = reduce(lambda x, y: x + y, [i for i in data.values() if type(i) == int])
    print("Контрольные суммы совпадают" if total_num == num else "Контрольные не суммы совпадают")
