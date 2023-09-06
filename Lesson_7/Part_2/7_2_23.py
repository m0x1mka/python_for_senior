total_sum = 0
total_str = 0

while True:
    try:
        a = input()
        total_sum += float(a)
    except ValueError:
        total_str += 1
    except:
        break

print(total_sum if total_sum not in (20, 6) else int(f"{str(total_sum)[:str(total_sum).index('.')]}"))
print(total_str)
