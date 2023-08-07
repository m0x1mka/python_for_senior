import pickle


def filter_dump(filename, objects, typename):
    with open(filename, "wb") as f:
        pickle.dump([i for i in objects if type(i) == typename], f)
