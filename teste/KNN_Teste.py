# -*- coding: utf-8 -*-

from sklearn import neighbors
import copy

from tools import PrepareDataSet


weight = 'distance'
n_neighbors = 7
percent_instances_to_trains_ = 80
window_size = 8
X = []
y = []
number_of_lines = PrepareDataSet.get_total_of_lines()
start_test_line_number = ((number_of_lines * percent_instances_to_trains_)/100)
print "teste começa nessa linha = " + str(start_test_line_number)
print "número total de linhas no arquivo = " + str(number_of_lines)

# lê todo o arquivo de dados do dataset setado no arquivo load_dataset no caso o a1_va3.csv
gestures = PrepareDataSet.getlines()


# pegar % do arquivo não janelado para treino
# refazer isso aqui está indo todo mundo pra o treinamento
def get_instances_to_train():
    list_train = []
    lines = gestures.readlines()
    for index in range(1, start_test_line_number-1):
        list_train.append(lines[index])
    print "quantidade de linhas na memoria " + str(len(list_train))
    return list_train

instances_to_train = get_instances_to_train()


def load_train_instances_on_knn(instances_to_train, is_windowed):
    if not is_windowed:
        for line in instances_to_train:
            fields = line.split(",")
            X.append(fields[:-1])
            y.append(str(fields[32:]).replace("\\n", "").replace("\\r", "").replace("'", ""))
        knn_classifier = neighbors.KNeighborsClassifier(n_neighbors, weight)
        knn_classifier.fit(X, y)
    else:
        result_xy = do_windowing(window_size, 1, start_test_line_number-1)
        knn_classifier = neighbors.KNeighborsClassifier(n_neighbors, weight)
        knn_classifier.fit(result_xy["X"], result_xy["y"])
    return knn_classifier


def prepare_instances_to_be_tested(instances_to_be_tested, is_windowed):
    if not is_windowed:
        cleaned_instances = []
        for instance in instances_to_be_tested:
            fields = instance.split(",")
            cleaned_instances.append(fields[:-1])
        return cleaned_instances
    else:
        result_xy = do_windowing(window_size, start_test_line_number, number_of_lines)
        print result_xy["X"]
        return result_xy["X"]


def get_real_phase_of_gestures(instances_to_be_tested):
    cleaned_instances = []
    for instance in instances_to_be_tested:
        fields = instance.split(",")
        cleaned_fields = ''.join(fields[32:])
        cleaned_instances.append(cleaned_fields.replace("\n", "").replace("\r", "").replace("'", ""))
    return cleaned_instances


# executa o classificador e retorna as previsões
def run_knn(instances_to_be_classifieds, is_windowed):
    results = []
    if not is_windowed:
        knn_classifier = load_train_instances_on_knn(instances_to_train, is_windowed=False)
        for instance in instances_to_be_classifieds:
            result = knn_classifier.predict(instance)
            results.append(result)
        return results
    else:
        for instance in instances_to_be_classifieds:
            knn_classifier = load_train_instances_on_knn(instances_to_train, is_windowed=True)
            print "instance"+str(instance)
            result = knn_classifier.predict(instance)
            results.append(result)
        return results


def get_percentage_corrects_predictions(obtained_results, expected_results):
    matches = 0
    if len(obtained_results) == len(expected_results):
        for index in range(0, len(obtained_results)):
            if expected_results[index] in str(obtained_results[index]):
                matches += 1
    return calculate_percentage(matches, len(obtained_results))


# unused just in case i nedd
def convert_obtained_results_to_list(obtained_results):
    obtained_results_as_strings = []
    for item in obtained_results:
        obtained_results_as_strings.append(''.join(item))
    return obtained_results_as_strings


def calculate_percentage(matches, total_instances):
    return (matches*100)/total_instances


def execute():
    gestures = PrepareDataSet.getlines()
    lines = gestures.readlines()
    instances_to_be_tested = []
    for index_line in range(start_test_line_number, number_of_lines):
        line = lines[index_line]
        instances_to_be_tested.append(line)

    prepared_instances_to_be_tested = prepare_instances_to_be_tested(instances_to_be_tested, False)
    results = run_knn(prepared_instances_to_be_tested, False)
    print "Percentual de acertos "\
          + str(get_percentage_corrects_predictions(results,
                                                    get_real_phase_of_gestures(instances_to_be_tested)))+"%"


def remove_labels_from_line(line):
    return line.replace("\n", "").replace("\r", "").replace("\'", "")\
        .replace(",D", "").replace(",S", "").\
        replace(",H", "").replace(",P", "").replace(",R", "").replace("/t", "").replace("'", "").replace("Y ", "")


def do_windowing(window_size, begin, end):
    gestures = PrepareDataSet.getlines()
    lines = gestures.readlines()
    count = 1
    line = ''
    return_xy = {}
    for index_line in range(begin, end):
        if count <= window_size:
            if count == 1:
                fields = lines[index_line].split(",")
                if (end - index_line) >= window_size:
                    y.append(str(fields[32:]).replace("\\n", "").replace("\\r", "").replace("'", ""))
            if count > 1:
                line += "," + remove_labels_from_line(lines[index_line])
            else:
                line += remove_labels_from_line(lines[index_line])
            count += 1
        else:
            count = 1
            X.append(line.split(","))
            line = ''

    return_xy["X"] = copy.deepcopy(X)
    return_xy["y"] = copy.deepcopy(y)
    X[:] = []
    y[:] = []
    print "tamanho de x "+str(len(return_xy["X"]))
    print "tamanho de y "+str(len(return_xy["y"]))

    return return_xy


def execute_windowed():
    prepared_instances_to_be_tested = do_windowing(window_size, start_test_line_number+1, number_of_lines)
    results = run_knn(prepared_instances_to_be_tested["X"], is_windowed=True)
    print "Percentual de acertos " \
          + str(get_percentage_corrects_predictions(results, prepared_instances_to_be_tested["y"]))+"%"



