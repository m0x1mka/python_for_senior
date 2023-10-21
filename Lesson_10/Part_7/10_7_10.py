def nonempty_lines(file):
    with open(file, encoding="utf-8") as f:
        for i in f.readlines():
            i = i.strip()
            if len(i) > 25:
                yield "..."
            elif i != "":
                yield i
