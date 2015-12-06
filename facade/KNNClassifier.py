__author__ = 'gleydson'
import operator as op
from collections import Counter

from facade import Instance, EuclidianDistance


class KNNClassifier(object):

    def __init__(self, x_train, y_train, k):
        self.x_train = x_train
        self.y_train = y_train
        self.k = k

    def get_votes_result(self, neighbors):
        elements = []
        for neighbor in neighbors:
            elements.append(neighbor.y)
        counter = Counter(elements)
        return counter.most_common(1)[0][0]

    def classify(self, x):
        distances = []
        ed = EuclidianDistance.EuclidianDistance

        for index in range(len(self.x_train)):
            distance = ed.calculate(x, self.x_train[index])
            instance = Instance.Instance(self.x_train[index], self.y_train[index])
            distances.append((instance, distance))

        distances.sort(key=op.itemgetter(1))
        neighbors = []
        
        for index_distance in range(self.k):
            neighbors.append(distances[index_distance][0])

        prediction = self.get_votes_result(neighbors)

        return prediction

