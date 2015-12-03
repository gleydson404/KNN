# -*- coding: utf-8 -*-
import csv
import numpy as np
from os import listdir
from os.path import isfile, join

EXTENSION = ".csv"


FILE = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/a1_va3.csv"
FILE_REDUCED = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData/a3_va3_reduced.csv"
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

    x = np.matrix(x)
    x = x.astype(np.float)
    dataset['x'] = x
    dataset['y'] = y

    return dataset
    # for i in range(len(x)):
    #     print('X = % s' %x[i])
    #     print('Y = % s' %y[i])


# get_dataset()
