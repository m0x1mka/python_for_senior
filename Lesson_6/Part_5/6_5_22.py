from collections import defaultdict


def wins(pairs):
    people = defaultdict(set)
    for key, value in pairs:
        people[key].add(value)
    return people
