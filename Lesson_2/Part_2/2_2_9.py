n = int(input())
current_emails = [input() for _ in range(n)]
m = int(input())
new_emails = [input() for _ in range(m)]
for i in new_emails:
    if i + "@beegeek.bzz" not in current_emails:
        i += "@beegeek.bzz"
        print(i)
        current_emails.append(i)
    else:
        num = 1
        while True:
            if f"{i}{str(num)}@beegeek.bzz" not in current_emails: break
            num += 1
        i = i + str(num) + "@beegeek.bzz"
        print(i)
        current_emails.append(i)
