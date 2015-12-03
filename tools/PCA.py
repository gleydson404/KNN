__author__ = 'gleydson'
import numpy as np

import matplotlib.pyplot as plt

from facade.tools import PrepareDataSet


# random seed for consistency
np.random.seed(1)

mu_vec1 = np.array([0, 0, 0])
cov_mat1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 3).T
assert class1_sample.shape == (3, 3), "The matrix has not the dimensions 3x20"

mu_vec2 = np.array([1, 1, 1])
cov_mat2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 3).T
assert class1_sample.shape == (3, 3)

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
assert all_samples.shape == (3, 6)


def calculate_mean_vector(original_matrix):
    mean_vector = []
    for index in range(len(original_matrix)):
        mean_vector.append(np.mean(original_matrix[index]))
    return mean_vector



# print('Matriz Original', all_samples)


def calculate_cov_matrix(original_matrix, mean_vector):
    return (original_matrix - mean_vector).T.dot((original_matrix - mean_vector)) / (original_matrix.shape[0]-1)




def execute(original_matrix):
    mean_vector = calculate_mean_vector(original_matrix.T)
    print len(mean_vector)

    cov_mat2 = calculate_cov_matrix(original_matrix, mean_vector)

    # cov_mat2 = np.cov(original_matrix)

    # print('cov numpy', cov_mat1)

    # print ('Gleydson Covariance', cov_mat2)

    # print ("shape cov", cov_mat2.shape)

    eigen_values, eigen_vectors = np.linalg.eig(cov_mat2)

    eigen_pairs = [(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))]

    eigen_pairs.sort()

    eigen_pairs.reverse()

    plot_explained_variance(eigen_values)

    eigen_vectors_choose = eigen_vectors

    print ("origianis", eigen_vectors_choose)

    print ("shape eigenvector", eigen_vectors_choose.shape)
    eigen_vectors_choose = eigen_vectors_choose[0:15]

    print ('escolhidos', eigen_vectors_choose)

    print ('shape escolhidos', eigen_vectors_choose.shape)

    # return eigen_values


    # matrix_w = np.hstack((eigen_pairs[0][1].reshape(3, 1),
    #                       eigen_pairs[1][1].reshape(3, 1)))
    #
    # print('Matrix w\n', matrix_w)

    print('shape original',original_matrix.shape)

    return original_matrix.dot(eigen_vectors_choose.T)

    # print ('Auto vetores com maior autovalor \\n', eigen_pairs)

    # print("Matrix reduziada \n", Y)


# execute(all_samples.T)

#
#
# print('Covariance Matrix Gleydson:\n', cov_mat2)
#
# cov_mat = np.cov([all_samples[0, :], all_samples[1, :], all_samples[2, :]])
# print('Covariance Matrix:\n', cov_mat)

def plot_explained_variance(eigen_values):
    tot = sum(eigen_values)
    print("tot", tot)
    var_exp = [(i / tot)*100 for i in sorted(eigen_values, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)

    y = var_exp
    x = [i for i in range(len(eigen_values))]

    soma = 0
    for index in range(15):
        soma += var_exp[index]

    print soma

    plt.plot(x,y, linestyle='--', marker='o', color='b')
    plt.ylabel("Porcentagem de Representacao")
    plt.xlabel("Indice dos Autovalores")
    plt.show()


dataset = PrepareDataSet.get_dataset()
reduced_matrix = execute(dataset['x'])
print np.savetxt(PrepareDataSet.PATH+"/a3_va3_reduced.csv", reduced_matrix, delimiter=',', fmt='%.8f')


# execute_windowed()
# execute()
