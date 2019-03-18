import kNN
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
datingDataMat, datingLabels = kNN.file2Matrix('datingTestSet.txt')
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],15.0*kNN.array(datingLabels),15.0*kNN.array(datingLabels))
plt.show()