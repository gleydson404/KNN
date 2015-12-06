__author__ = 'gleydson'
from tools import PrepareDataSet as pds
from os import listdir
from os.path import isfile, join
from facade import KNNClassifier as knn

TRAINING_SLICE = 70

k = 5

files = [f for f in listdir(pds.PATH) if isfile(join(pds.PATH, f)) and "windowed" in f]

data = [pds.get_dataset(pds.PATH+"/"+file) for file in files]

data_x = [pds.get_training_data(TRAINING_SLICE, data[index]['x'], type='x') for index in range(len(data))]

data_y = [pds.get_training_data(TRAINING_SLICE, data[index]['y'], type='y') for index in range(len(data))]



clfs = [knn.KNNClassifier(data_x[index][0], data_y[index][0], k) for index in range(len(data))]
# clf = knn.KNNClassifier(data_x[1][1], data_y[1][1], k)