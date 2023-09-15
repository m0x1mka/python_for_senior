def convert(num):
    ans = [i[2:] if i[0] != "-" else i.replace(i[1:3], "") for i in (bin(num), oct(num))]
    ans += [hex(num)[2:].upper() if hex(num)[0] != "-" else hex(num).replace(hex(num)[1:3], "").upper()]
    return tuple(ans)
