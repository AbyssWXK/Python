#coding=UTF-8
import trees
import Decision_Tree
import Plot_tree
import treePlotter
# myDat, labels = trees.createDataSet()
# mytree = Decision_Tree.Create_Tree(myDat,labels)
# print myDat
# print  labels
# print(trees.calcShannonEnt(myDat))
# print trees.splitDataSet(myDat,0,1)
# print trees.splitDataSet(myDat,0,0)

#myTree = trees.createTree(myDat,labels)
# mytree = Plot_tree.retrieveTree(1)
# treePlotter.createPlot(mytree)
# Plot_tree.createPlot(mytree)
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readline()]
lensesLabels  = ['age','prescript','astigmatic','terarRate']
lensesTree  = trees.createTree(lenses,lensesLabels)
print lensesTree
treePlotter.createPlot(lensesTree)