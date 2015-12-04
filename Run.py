__author__ = 'gleydson'
from tools import PrepareDataSet as pds
from os import listdir
from os.path import isfile, join

TRAINING_SLICE = 70


files = [f for f in listdir(pds.PATH) if isfile(join(pds.PATH, f))]

data = [pds.get_dataset(pds.PATH+"/"+file) for file in files]

data_splited = [pds.get_training_data(TRAINING_SLICE, data[index]['x']) for index in range(len(data))]



print data_splited