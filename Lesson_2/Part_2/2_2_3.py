n, X, Y, A, B = list(map(int, input().split()))
lst = [i for i in range(1, n + 1)]
lst[X-1:Y] = lst[X-1:Y][::-1]
lst[A-1:B] = lst[A-1:B][::-1]
print(*lst)