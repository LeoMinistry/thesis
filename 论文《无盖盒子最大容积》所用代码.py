cutsize = 5
nowcut = cutsize
data = {}
s = 0.1
for t in range(4):
    for i in range(10):
        nowcut -= s
        data[nowcut] = ((29.7-2*nowcut)*(21-2*nowcut)*nowcut)
    nowcut = cutsize
    for j in range(10):
        nowcut += s
        data[nowcut] = ((29.7-2*nowcut)*(21-2*nowcut)*nowcut)
    cutsize = list(data.keys())[list(data.values()).index(max(list(data.values())))]
    print('当前裁剪大小：{}，已分{}次，盒盖大小{}cm²'.format(int(cutsize*10000)/10000,t+1,max(list(data.values()))))
    s /= 10
print('最终裁剪大小{}cm，盒子大小{}cm²。'.format(int(cutsize*10000)/10000,max(list(data.values()))))