def loadConf(filename="crawler.conf"):
    confs = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            key, value = line.split()
            confs[key] = value
    return confs