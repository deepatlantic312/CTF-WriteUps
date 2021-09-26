data = ""
steps = [3,11,2,13,6,4,9,5,10,8,25,11,7,3,19,4,18,40,23]
data = list(data)

prev = 0
for i in steps:
    for j in range(len(data)):
        if j % i == 0 and j - prev >= 0:
            data = data[:j-prev] + data[j:] + data[j-prev:j]
            print(''.join(data))
    prev = i

print(''.join(data))