data = ""
steps = [7,11,5,19,2,26,12,3,11,40,4,18,9,17,32]
data = list(data)
for i in steps:
    for j in range(len(data)):
        if j % i == 0:
            if j + i < len(data):
                [data[j], data[j+i]] = [data[j+i], data[j]]
            else:
                continue

print(''.join(data))