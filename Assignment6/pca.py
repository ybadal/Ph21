import numpy as np
from numpy.random import normal
from numpy.linalg import eig


def pca_matrix(dataset):
    '''Takes as argument dataset, a M x N matrix consisting of N samples of M
    measurements (every row corresponds to a measurement), and returns a
    N x M matrix with rows the eigenvectors of the covariance matrix of
    dataset.'''
    dataset = [row - np.mean(row) for row in dataset]
    cx = np.cov(dataset)
    (_, pca) = eig(cx)
    pca_transpose = np.transpose(pca) # transposition necessary for projection
                                      # by matrix multiplication
    return pca_transpose


def pca(dataset):
    '''Takes as argument dataset, a M x N matrix consisting of N samples of M
    measurements (every row corresponds to a measurement) and returns the
    pricipal components of the dataset.'''
    pca_mat = pca_matrix(dataset)
    pca = np.matmul(pca_mat, dataset) # change of base by projection
                                      # with diagonal basis for cov matrix
    return pca


def linear_dataset(n=10, c=1, m=5, err=0.1):
    '''Generates 2D dataset with y linearly dependent on x. n is number of
    samples, c is y-intercept, m is slope, err is error in sample. Noise is
    simulated by multiplying samples by Gaussian with width err.'''
    xx = range(n)
    yy = [(c + m*x) * normal(1.0, err) for x in xx]

    gen_data = np.array([xx, yy])

    return gen_data


def var_axis(mat):
    '''Returns variance on each axis for a matrix. This is useful to
    investigate the components contributing to the covariance (essentially
    the degrees of freedom).'''
    var_mat = [np.std(row)**2 for row in mat]
    return var_mat


def linear4d_dataset(n=10, c1=2, m1=4, c2=5, m2=1, c3=0, m3=-3, err=0.1):
    '''Generate a 3D dataset with linearly dependent variables (not including
    the explicit dependent variable).'''
    xx = range(n)
    yy1 = [(c1 + m1*x) * normal(1.0, err) for x in xx] 
    yy2 = [(c2 + m2*x) * normal(1.0, err) for x in xx]
    yy3 = [(c3 + m3*x) * normal(1.0, err) for x in xx]

    dataset = np.array([xx, yy1, yy2, yy3])

    return dataset


# Testing pca on linear dataset
pca_linear = pca(linear_dataset())
f = open('linear_test.txt', 'w')
out = ['Linear PCA = %s' % pca_linear,
        'Variance over axes = %s' % var_axis(pca_linear)]
f.write('\n'.join(out)) 
f.close()


# Testing pca on 4d multilinear dataset
pca_4dlinear = pca(linear4d_dataset())
f = open('linear4d_test.txt', 'w')
out = ['PCA = %s' % pca_linear,
        'Variance over axes = %s' % var_axis(pca_4dlinear)]
f.write('\n'.join(out))
f.close()

