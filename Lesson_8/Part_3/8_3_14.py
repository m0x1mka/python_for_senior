def tribonacci(num):
    memory = {1: 1, 2: 1, 3: 1}

    def rec(n):
        result = memory.get(n)
        if result is None:
            result = rec(n - 1) + rec(n - 2) + rec(n - 3)
            memory[n] = result
        return result

    return rec(num)
