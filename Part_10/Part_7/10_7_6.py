def parse_ranges(ranges):
    leave_nums = map(lambda x: x.split("-"), ranges.split(","))
    make_int = map(lambda x: [int(x[0]), int(x[1])], leave_nums)
    for i in make_int:
        yield from range(i[0], i[1] + 1)
