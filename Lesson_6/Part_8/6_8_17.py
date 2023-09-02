from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = lambda: [i for i in data.items() if i[1] == max(data.items(), key=lambda x: x[1])[1]]
data.min_values = lambda: [i for i in data.items() if i[1] == mmin(data.items(), key=lambda x: x[1])[1]]
