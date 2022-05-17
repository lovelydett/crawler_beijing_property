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
            try:
                name, year, price = line.split()
                communities.append({
                    "name": name,
                    "year": int(year),
                    "price": int(price),
                })
            except:
                pass
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

def loadCompleteCommunityData(filename="complete_community_dataset.csv"):
    results = {
        "name": [],
        "price": [],
        "age": [],
        "sp_school": [],
        "sp_subway": [],
        "sp_hospital": [],
        "sp_mall": [],
        "sp_office": [],
    }
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                name, price, age, sp_school, sp_subway, sp_hospital, sp_mall, sp_office = str(row[0].strip()), int(row[1].strip()), int(row[2].strip()), float(row[3].strip()), float(row[4].strip()), float(row[5].strip()), float(row[6].strip()), float(row[7].strip())
                results["name"].append(name)
                results["price"].append(price)
                results["age"].append(age)
                results["sp_school"].append(sp_school)
                results["sp_subway"].append(sp_subway)
                results["sp_hospital"].append(sp_hospital)
                results["sp_mall"].append(sp_mall)
                results["sp_office"].append(sp_mall)
            except:
                pass
    return results

if __name__ == "__main__":
    ret = loadCommunityWithPositions()
    print(ret)


