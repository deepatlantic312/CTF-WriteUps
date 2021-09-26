data = "ih uelaguyptoa sUeNstihn  Ur efGifaoer   n.o cnirfGonNs tdcdtsrehe eoeehi avt rteho gietdrp siatrtavgcy tnnet un-rgoosb an eiav eenl rntigetsriicx oleep   f oh ctnme,gfi snurtaohd pceget Oe  outo nrelrsfe (eRcsndeT SuctPioOe e oA EtiRt,dto)l naceh is   noh mswe ekdt el(shisfn)tir nd  atlorfefasrnw ooefr,aopu itto, i etoco epra hm hpi tienavsd oifnn eiot nshn ntelxe me nffts. man-I iuo,t ri e o gi fietcds mpidi.ssdcv`a'sa  nTmsdeh."
steps = [7,11,5,19,2,26,12,3,11,40,4,18,9,17,32]
data = list(data)

d = []

for i in steps:
    for j in range(len(data)):
        if j % i == 0:
            if j + i < len(data):
                d.append((j, j + i))
            else:
                continue
d = d[::-1]

for i, j in d:
    [data[i], data[j]] = [data[j], data[i]]
print("".join(data))
