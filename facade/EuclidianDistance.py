__author__ = 'gleydson'
import math as mt


class EuclidianDistance(object):


    @staticmethod
    def calculate(x, y):
        sum = 0
        print "distancia de " + str(x) + " a " + str(y)
        for index in range(0, len(x)):
            sum += ((x[index] - y[index]) ** 2)
        return mt.sqrt(sum)