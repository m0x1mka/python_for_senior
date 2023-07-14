import csv

with open("4_2_16.csv", encoding="utf-8") as f:
    data = list(csv.reader(f))
    domains = {}
    for i in data[1:]:
        if i[2][i[2].find("@") + 1:] not in domains.keys():
            domains[i[2][i[2].find("@") + 1:]] = 1
        else:
            domains[i[2][i[2].find("@") + 1:]] += 1
    with open("4_2_16_final", "w", encoding="utf-8", newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow(["domain", "count"])
        for i in sorted(sorted(list(domains.items()), key=lambda x: x[0]), key=lambda x: x[1]):
            writer.writerow(list(i))
