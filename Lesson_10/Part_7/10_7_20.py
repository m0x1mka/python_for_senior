def stop_on(itr, obj):
    for i in itr:
        if i == obj:
            break
        yield i
