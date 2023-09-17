def hash_as_key(data):
    final_data = {}
    for i in data:
        ans = hash(i)
        if ans not in final_data:
            final_data[ans] = i
        else:
            old = final_data[ans]
            if type(old) == list:
                final_data[ans].append(i)
            else:
                final_data[ans] = [old]
                final_data[ans].append(i)
    return final_data
