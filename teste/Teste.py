__author__ = 'gleydson'
from facade import KNNClassifier as Knn

x = [[2, 2, 2], [4, 4, 4], [5, 5, 5], [3, 3, 3], [5.1, 5.1, 5.1], [1, 1, 1]]
y = ['a', 'b', 'b', 'a', 'b', 'a']
test = [2, 2, 2]

clf = Knn.KNNClassifier(x, y, 2)
# for item in clf.classify(test):
#     print str(item.x) + " " + str(item.y)

print clf.classify(test)
