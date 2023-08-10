from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open("6_4_10_data.pkl", "rb") as f:
    data = pickle.load(f)

for i in data:
    print(f"name: {i.name}")
    print(f"family: {i.family}")
    print(f"sex: {i.sex}")
    print(f"color: {i.color}\n")
