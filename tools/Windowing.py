__author__ = 'gleydson'
from tools import PrepareDataSet as pds


def generate_file_name(size_window, name):
    return pds.PATH+"/"+name+"_"+str(size_window)+pds.EXTENSION

def to_window(size_window):
    file = open(pds.FILE_REDUCED, 'r')
    w_file = open(generate_file_name(size_window,"a3_va3_reduced_windowed"), 'w')
    lines = file.readlines()
    for index in range(len(lines)):
        w_line = ''
        flag = False
        if index <= len(lines) - size_window:
            for inner_index in range(size_window):
                if not flag:
                    w_line += (lines[index + inner_index].replace("\n", ""))
                    flag = True
                else:
                    w_line += ","+(lines[index + inner_index].replace("\n", ""))
            w_line += "\n"

            w_file.write(w_line)

    w_file.close()

to_window(5)


