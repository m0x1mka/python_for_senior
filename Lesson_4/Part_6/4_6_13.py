import pickle
import sys

with open(input(), "rb") as file:
    data = pickle.load(file)

print(data(*list(map(str.strip, sys.stdin))))
