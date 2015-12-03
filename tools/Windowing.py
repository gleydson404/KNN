__author__ = 'gleydson'
from facade.tools import PrepareDataSet


def to_window(size_window):
    file = open(PrepareDataSet.FILE_REDUCED, 'r')
    w_file = open(PrepareDataSet.PATH+"/a3_va3_reduced_windowed.csv", 'w')
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


