data = "a" * 84
steps = [3,11,2,13,6,4,9,5,10,8,25,11,7,3,19,4,18,40,23]
data = list(data)

d = []

prev = 0
for i in steps:
    for j in range(len(data)):
        if j % i == 0 and j - prev >= 0:
            data = data[:j-prev] + data[j:] + data[j-prev:j]
            d.append((j-prev, len(data) - j, prev))
    prev = i

data = "11a06ca9064be482cd8b58202e6e3cc00027fb9d1c307026000e03877cc0fcf4840081d32e64000440db"
indexes = d[::-1]
for index in indexes:
    data = data[:index[0]] + data[index[0] + index[1]:] + data[index[0]: index[0] + index[1]]
print(data)
