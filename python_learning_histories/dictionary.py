dic1 = {"color": "blue", "size": "M"}
print(dic1)

dic2 = {"color": "blue", "size": "M", "size": "L"}
print(dic2)

dic3 = {"color": "blue", "size": "M", "size": "M"}
print(dic3)
print(len(dic3))

dic4 = {"color": "blue", "size": "M", "color": "black"}
print(dic4)
print(dic4["color"])
# print(dic4[0])
# dic5 = {"name": "Rose", "gender": "Femal"}

dic5 = {"clickable": False, "year": 2025, "color": ["blue", "black", "white"]}
print(dic5)
print(type(dic5))

dic6 = dict(clickable = False, year = 2025, color = ["blue", "black", "white"])
print(dic6)
x = dic6["clickable"]
print(x)
y = dic6.get("color")
print(y)
k = dic6.keys()
print(k)
dic6["status"] = "active"
print(k)
print(dic6)
v = dic6.values()
print(v)
i = dic6.items()
print(i)
if "birth" in dic6:
    print("birth is in dic6")
else:
    print("birth is not in dic6")
dic6["year"] = 2024
print(dic6)
dic6.update({"year":2025})
print(dic6)
dic6.update({"id":1234})
print(dic6)
dic6.pop("color")
print(dic6)
dic6.popitem()
print(dic6)
del dic6["year"]
print(dic6)
# del dic6
# print(dic6)
# dic6.clear()
# print(dic6)
for l in dic6:
    print(l) # return keys
for i in dic6:
    print(dic6[i])  # return values
for k1, y1 in dic6.items():
    print(k1,":", y1)

dic7 = dic6.copy()
print(dic7)
dic8 = dict(dic7)
print(dic8)

dic9 = {"product1": {"name": "BLUE", "location": "SH"}, "product2":{"name": "BLACK", "location": "QD"}}
print(dic9)

prd1 = {"name": "BLUE", "location": "SH"}
prd2 = {"name": "BLACK", "location": "QD"}
prds = {"product1": prd1, "product2": prd2}
print(prds)
print(prds["product1"]["location"])
for k2, v2 in prds.items():
    print(k2)
    for i in v2:
        print(i+":", v2[i])
for x, y in prd1.items():
    print(x, y)
