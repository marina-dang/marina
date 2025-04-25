products = ["VCD", "aLP", 'berry']
search = input("Input product name:").lower()
for p in products:
    if p.lower() == search:
        print("found:", p)
        break
else:
    print("no such product.")

for i in range(10,1, -1):
    print(i)
print('loop ends')