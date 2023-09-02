from collections import Counter


def print_bar_chart(data, mark):
    ans = Counter(data)
    max_len = len(max(ans.keys(), key=len))
    for i in sorted(ans.items(), key=lambda x: x[1], reverse=True):
        print(f"{i[0]}{' ' * (max_len - len(i[0]) + 1)}|{mark * i[1]}")
