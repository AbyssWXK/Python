import kNN
group,labels = kNN.createDataSet()
result  = kNN.classify0([1,1],group,labels,3)
print (result)