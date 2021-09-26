seeds = [40]
for i in range(39):
    seed = seeds[-1]
    seeds.append((seed * 5 + (seed - 9) + 6) % 300)
keys = list(map(lambda x: x % 25 + 65, seeds))

with open("cipher", "rb") as f:
    data = f.read()
s = ""
for i in range(len(data)):
    s += chr(data[i] ^ keys[i % 40])
print(s)
