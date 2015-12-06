# -*- coding: utf-8 -*-
import csv
import numpy as np
from os import listdir
from os.path import isfile, join

EXTENSION = ".csv"

FILE_NAME = "a3_va3"
FILE_NAME_REDUCED = FILE_NAME+"_reduced"
FILE_NAME_REDUCED_PRED = FILE_NAME+"_reduced_pred"
FILE_NAME_WINDOWED = FILE_NAME+"_windowed"

FILE = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/"+FILE_NAME+EXTENSION
FILE_REDUCED = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData/"+FILE_NAME_REDUCED+EXTENSION
FILE_REDUCED_PRED = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData/"+FILE_NAME_REDUCED_PRED+EXTENSION
PATH = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData"


def getlines():
    f = open(FILE, 'r')
    return f


def get_total_of_lines():
    count = 0
    for line in getlines():
        count += 1
    return count


def get_files_list():
    return [f for f in listdir(PATH) if isfile(join(PATH, f))]


def make_dataset():
    files = get_files_list()
    with open(PATH + '/to/output/file', 'w') as outfile:
        for file in files:
            with open(file) as infile:
                for line in infile:
                    outfile.write(line)


def get_dataset(file):
    x = []
    y = []
    dataset = {}

    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        all_samples = list(spamreader)

    for line in all_samples:
        x.append(np.asarray(line[:-1]))
        y.append(line[-1:])

    x = np.matrix(x).astype(np.float)
    # x = x.astype(np.float)

    dataset['x'] = x
    dataset['y'] = np.squeeze(np.asarray(y))

    # for i in range(len(x)):
    #     print('X = % s' %x[i])
    #     print('Y = % s' %y[i])
    return dataset


def get_training_data(training_slice, data, type):
    total_lines = data.shape[0]
    print total_lines
    percentage = (total_lines * (float(training_slice)/float(100)))
    print percentage
    if type == 'x':
        return data[0:percentage, :], data[percentage+1:total_lines, :]
    elif type == 'y':
        return data[0:percentage], data[percentage+1:total_lines]
