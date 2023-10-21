def txt_to_dict():
    with open("planets.txt", encoding="utf-8") as f:
        text = f.read().split("\n\n")
        for i in text:
            planets_data = {}
            for j in i.split("\n"):
                s = j.split(" = ")
                key = s[0]
                value = s[1]
                planets_data[key] = value
            yield planets_data
