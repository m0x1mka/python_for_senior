import string

alphabet = input()
word = input().lower()
ans = ""
for i in word:
    chars = string.ascii_lowercase
    if i in chars:
        num = chars.index(i)
        ans += alphabet[num]
    else:
        ans += i
print(ans)
