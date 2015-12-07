__author__ = 'gleydson'
from tools import PrepareDataSet as Pds
from collections import Counter


def generate_file_name(size_window, name):
    return Pds.PATH+"/"+name+"_"+str(size_window)+Pds.EXTENSION


def to_window(size_window):
    file_x = open(Pds.FILE_REDUCED, 'r')
    file_y = open(Pds.FILE_REDUCED_PRED, 'r')
    w_file = open(generate_file_name(size_window, Pds.FILE_NAME_WINDOWED), 'w')
    lines_x = file_x.readlines()
    lines_y = file_y.readlines()

    for index in range(len(lines_x)):
        w_line = ''
        flag = False
        possibles_y = []
        if index <= len(lines_x) - size_window:
            for inner_index in range(size_window):
                possibles_y.append(lines_y[index + inner_index])
                if not flag:
                    w_line += (lines_x[index + inner_index].replace("\n", ""))
                    flag = True
                else:
                    w_line += ","+(lines_x[index + inner_index].replace("\n", ""))
            counter = Counter(possibles_y)
            choosed_y = counter.most_common(1)[0][0]
            choosed_y = choosed_y.replace("\n", "")

            w_line += "," + choosed_y + "\n"

            w_file.write(w_line)

    w_file.close()

to_window(10)


