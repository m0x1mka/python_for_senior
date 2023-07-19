import csv


def condense_csv(filename, id_name):
    with open(filename) as f:
        text = list(csv.reader(f))
        objects = {}
        for i in text:
            if i[0] not in objects.keys():
                objects[i[0]] = {i[1]: i[2]}
            else:
                objects[i[0]][i[1]] = i[2]
        f_line = [id_name] + list(objects[i[0]].keys())
        with open("4_2_20_answer.csv.csv", "w", encoding="utf-8", newline="") as fw:
            writer = csv.writer(fw)
            writer.writerow(f_line)
            for i in objects:
                line = [i]
                for m in objects[i].values():
                    line.append(m)
                writer.writerow(line)


condense_csv("4_2_20.csv", "ID")
