#coding=UTF-8
import random
from numpy import *
def loadDataSet(fileName):
    dataMat = [];labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    j = i
    while (j == i):
        j = int(random.uniform(0,m))
    return j
def clipAlpha(aj,H,L):
    if aj>H:
        aj=H
    if L>aj:
        aj=L
    return aj

def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
    b = 0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))  # 创建一个包含m个alpha值的向量，全部初始化为0
    iter = 0
    while (iter < maxIter):  # 外循环，迭代次数小于最大迭代次数
        alphaPairsChanged = 0
        for i in range(m):   # 内循环，对数据集中的每个数据向量
            # 计算预测类别 fXi
            fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b  # multiply 实现对应位置元素相乘
            # 计算误差
            Ei = fXi - float(labelMat[i])  #if checks if an example violates KKT conditions
            # 如果误差很大，则该数据实例所对应的alpha值要进行优化
            # 这里本来是 C>=α>=0，不取等号是因为等号代表数据实例位于边界上，不值得优化
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i,m)  # 选择第二个alpha值 alphas[j]
                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy(); # 用copy方法拷贝旧值，防止Python传递列表采用的是传引用方式
                if (labelMat[i] != labelMat[j]):  # 控制 alphas[j] 调整到0到C之间
                    L = max(0, alphas[j] - alphas[i])  # 下届不能小于0
                    H = min(C, C + alphas[j] - alphas[i])  # 上界不能大于C
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H: print("L==H"); continue   # 如果上下界相等，不做任何改变，continue进行下一次循环
                # eta是alphas[j]的最优修改量，因为如果eta为0，计算新的alphas[j]比较麻烦，所以对SMO做了简化，不做处理，continue进行下一次循环
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print("eta>=0"); continue
                # 对alphas[j]的上下界进行调整
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                # 检查alpha[j]是否有轻微改变，如果是，continue进行下一次循环
                if (abs(alphas[j] - alphaJold) < 0.00001): print("j not moving enough"); continue
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j]) # 更新alphas[i]值，与alphas[j]值大小一样，但方向相反，即一个增加，另外一个减少
                # 设置常数项b
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1  # 标记这一对alpha值进行了改变
                print(("iter: %d i:%d, pairs changed %d") % (iter,i,alphaPairsChanged))
        if (alphaPairsChanged == 0): iter += 1 # 如果这一对alpha值没有改变，则继续迭代。这里是所有alpha不发生修改，程序才会停止退出while循环
        else: iter = 0  # 如果这一对alpha值改变了，iter设置为0重新进行迭代
        print(("iteration number: %d") % iter)
    return b,alphas  # 返回常数项b和更新后的alphas向量
