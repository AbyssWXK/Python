import re

def strToInt(L):
    TL = []
    for x in L:
        TL .append(int(x))
    return TL


def load():
    fileName = 'Road.txt'
    fp = open(fileName,'r',encoding = 'UTF8')
    fp.readline()
    roadStr = fp.read()
    roadList = re.findall('\((.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)\)',roadStr)
    roadDoc = {}
    for road in roadList:
        roadl = list(road)
        roadl = strToInt(roadl)
        roadDoc[roadl[0]] = roadl
    fp.close()

    fileName = 'Car.txt'
    fp = open(fileName, 'r', encoding='UTF8')
    fp.readline()
    carStr = fp.read()
    carList = re.findall('\((.*?),(.*?),(.*?),(.*?),(.*?)\)', carStr)
    carDoc = {}
    for car in carList:
        carl = list(car)
        carl = strToInt(carl)
        carDoc[carl[0]] = carl
    fp.close()

    fileName = 'Cross.txt'
    fp = open(fileName, 'r', encoding='UTF8')
    fp.readline()
    crossStr = fp.read()
    crossList = re.findall('\((.*?),(.*?),(.*?),(.*?),(.*?)\)', crossStr)
    crossDoc = {}
    for cross in crossList:
        crossl = list(cross)
        crossl = strToInt(crossl)
        crossDoc[crossl[0]] = crossl
    fp.close()


    return roadDoc,carDoc,crossDoc



INF = 99999
def floyd():
    roadDoc, carDoc, crossDoc = load()
    G = {}
    for cross in crossDoc:
        crossT = {}
        for eveCross in crossDoc:
            # print(crossDoc[eveCross][2])
            crossT[eveCross] = INF           #初始化INF
        # print(crossT)
        crossT[cross] = 0
        for i in range(1,5):
            if crossDoc[cross][i] != -1:
                if roadDoc[crossDoc[cross][i]][4] != cross :
                    crossT[roadDoc[crossDoc[cross][i]][4]] = roadDoc[crossDoc[cross][i]][1]
                else:
                    crossT[roadDoc[crossDoc[cross][i]][5]] = roadDoc[crossDoc[cross][i]][1]
        G[cross] = crossT
        # print(crossT)
    # print(G)
    # 算法思想：
    # 每个顶点都有可能使得两个顶点之间的距离变短
    # 当两点之间不允许有第三个点时，这些城市之间的最短路径就是初始路径

    # Floyd-Warshall算法核心语句
    # 分别在只允许经过某个点k的情况下，更新点和点之间的最短路径
    for k in G.keys():  # 不断试图往两点i,j之间添加新的点k，更新最短距离
        for i in G.keys():
            for j in G[i].keys():
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]
    for i in G.keys():
        print(G[i].values())
# road, car ,cross = load()
# print(cross)