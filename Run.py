__author__ = 'gleydson'
from tools import PrepareDataSet as pds
from os import listdir
from os.path import isfile, join
from facade import KNNClassifier as Knn
import numpy as np

TRAINING_SLICE = 70

k = 5

files = [f for f in listdir(pds.PATH) if isfile(join(pds.PATH, f)) and "windowed" in f]

print files

data = [pds.get_dataset(pds.PATH+"/"+file) for file in files]

data_x = [pds.get_training_data(TRAINING_SLICE, data[index]['x'], type='x') for index in range(len(data))]

data_y = [pds.get_training_data(TRAINING_SLICE, data[index]['y'], type='y') for index in range(len(data))]

# print ('squeese',np.squeeze(np.asarray(data_x[index][0][0])))

print ("shape",data_x[index][0].shape)

clfs = [Knn.KNNClassifier(data_x[index][0], data_y[index][0], k) for index in range(len(data))]
# clf = knn.KNNClassifier(data_x[1][1], data_y[1][1], k)

# results = {}
# for index in range(len(clfs)):
#     predictions = []
#     for item in data_y[index][1]:
#         predictions.append(clfs[index].classify(data_y[index][item]))
#     results[index] = predictions

# predictions = []
# for item in range(len(data_x[0][1])):
#     print item[0]
print ('predic',  np.squeeze(np.asarray(data_x[0][1][0])))
# predictions.append(clfs[0].classify(item))
print('pred', clfs[0].classify(np.squeeze(np.asarray(data_x[0][1][0]))))