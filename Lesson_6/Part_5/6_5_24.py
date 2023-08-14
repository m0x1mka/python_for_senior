from collections import defaultdict


def best_sender(messages, senders):
    words = defaultdict(int)
    for i in zip(messages, senders):
        words[i[1]] += len(i[0].split())
    ans = defaultdict(list)
    for key, value in words.items():
        ans[value].append(key)

    return sorted(ans[max(ans.keys())])[-1]
