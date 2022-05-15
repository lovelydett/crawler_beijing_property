def loadConf(filename="crawler.conf"):
    confs = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            key, value = line.split()
            confs[key] = value
    return confs

def loadCommunity(filename="price_community.txt"):
    communities = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            name, year, price = line.split()
            communities.append({
                "name": name,
                "year": int(year),
                "price": int(price),
            })
    return communities