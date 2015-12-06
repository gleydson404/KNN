__author__ = 'gleydson'
from tools import PrepareDataSet as pds


def generate_file_name(size_window, name):
    return pds.PATH+"/"+name+"_"+str(size_window)+pds.EXTENSION

def to_window(size_window):
    file_x = open(pds.FILE_REDUCED, 'r')
    file_y = open(pds.FILE_REDUCED_PRED, 'r')
    w_file = open(generate_file_name(size_window, pds.FILE_NAME_WINDOWED), 'w')
    lines_x = file_x.readlines()
    lines_y = file_y.readlines()
    for index in range(len(lines_x)):
        w_line = ''
        flag = False
        if index <= len(lines_x) - size_window:
            for inner_index in range(size_window):
                if not flag:
                    w_line += (lines_x[index + inner_index].replace("\n", ""))
                    flag = True
                else:
                    w_line += ","+(lines_x[index + inner_index].replace("\n", ""))
            w_line += "," + lines_y[index]

            w_file.write(w_line)

    w_file.close()

to_window(5)


