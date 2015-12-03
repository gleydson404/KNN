__author__ = 'gleydson'
from tools import PrepareDataSet as pds
from os import listdir
from os.path import isfile, join
# from facade import KNNClassifier as knn

files = [f for f in listdir(pds.PATH) if isfile(join(pds.PATH, f))]

data = [pds.get_dataset(f for f in files)]

print data