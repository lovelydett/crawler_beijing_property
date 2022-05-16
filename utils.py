import csv

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

def loadCommunityWithPositions(filename="position_price_community.csv"):
    results = {
        "name": [],
        "age": [],
        "price": [],
        "lat": [],
        "lng": [],
    }
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                name, year, price, lat, lng = str(row[0].strip()), int(row[1].strip()), int(row[2].strip()), float(row[3].strip()), float(row[4].strip())
                results["name"].append(name)
                results["age"].append(2022 - year)
                results["price"].append(price)
                results["lat"].append(lat)
                results["lng"].append(lng)
            except:
                pass
    return results

if __name__ == "__main__":
    ret = loadCommunityWithPositions()
    print(ret)


