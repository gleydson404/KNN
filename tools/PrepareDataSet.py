# -*- coding: utf-8 -*-
import csv
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as Plt

EXTENSION = ".csv"

TRAINING_SLICE = 70

FILE_NAME = "a1_va3"
FILE_NAME_REDUCED = FILE_NAME+"_reduced"
FILE_NAME_REDUCED_PRED = FILE_NAME+"_reduced_pred"
FILE_NAME_WINDOWED = FILE_NAME+"_windowed"

FILE = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/"+FILE_NAME+EXTENSION
FILE_REDUCED = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData/"+FILE_NAME_REDUCED+EXTENSION
FILE_REDUCED_PRED = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData/"+FILE_NAME_REDUCED_PRED+EXTENSION
PATH = "/home/gleydson/Documents/Mestrado-SistemasDeInformaçãoUSP2015.2/GesturePhasesDataset/workData"

TARGET_NAMES = ['D', 'P', 'S', 'H', 'R']


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


def calculate_percentage(rate, total):
    return int(total * (float(rate)/float(100)))


def get_training_data(training_slice, data, type):
    total_lines = data.shape[0]
    # percentage = (total_lines * (float(training_slice)/float(100)))
    percentage = calculate_percentage(training_slice, total_lines)
    if type == 'x':
        return data[0:percentage, :], data[percentage+1:total_lines, :]
    elif type == 'y':
        return data[0:percentage], data[percentage+1:total_lines]


def get_real_classes(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        number_lines = len(lines)
        percentage = calculate_percentage(TRAINING_SLICE, number_lines)
        true_classes = [lines[index] for index in range(percentage, number_lines)]
    return true_classes


def plot_confusion_matrix(cm):
    title = 'Confusion Matrix'
    Plt.imshow(cm, interpolation='nearest', cmap=Plt.cm.Blues)

    width = len(cm)
    height = len(cm[0])

    for x in xrange(width):
        for y in xrange(height):
            Plt.annotate(str(cm[x][y]), xy=(y, x),
                    horizontalalignment='center',
                    verticalalignment='center')

    Plt.title(title)
    Plt.colorbar()
    tick_marks = np.arange(len(TARGET_NAMES))
    Plt.xticks(tick_marks, TARGET_NAMES)
    Plt.yticks(tick_marks, TARGET_NAMES)
    Plt.tight_layout()
    Plt.ylabel('True label')
    Plt.xlabel('Predicted label')
    Plt.show()