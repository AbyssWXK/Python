import kNN
testVector = kNN.img2vector('testDigits/0_13.txt')
for line in range(0,31):
    for col in range(0,31):
        print (int(testVector[0][line*32+col])),
    print ''
kNN.handwritingClassTest()