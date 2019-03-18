import bayes
listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print myVocabList
# print bayes.setOfWords2Vec(myVocabList,listOPosts[3])
trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
# print trainMat
p0V,p1V,pAb=bayes.trainNB0(trainMat,listClasses)
bayes.spamTest()