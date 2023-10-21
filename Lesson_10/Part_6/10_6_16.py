def is_prime(num):
    if num == 1:
        return False
    return all([num % i != 0 for i in range(2, num - 1)])
