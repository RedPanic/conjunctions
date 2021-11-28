import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets


class KMeansTools(object):
    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = np.array(value)

    def find_cluster_number(self):
        distortions = []
        num_of_clusters = range(1, 10)
        for k in num_of_clusters:
            kmeanModel = KMeans(n_clusters=k)
            kmeanModel.fit(self.matrix)
            distortions.append(kmeanModel.inertia_)
        plt.figure(figsize=(16, 8))
        plt.plot(num_of_clusters, distortions, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Distortion')
        plt.title('Liczba klastrów')
        plt.show()

    def make_clustering(self):
        kmeansModel = KMeans(n_clusters=3, init='random', n_init=10, max_iter=300, random_state=42)
        kmeansPredict = kmeansModel.fit_predict(self.matrix)
        plt.scatter(self.matrix[kmeansPredict == 0, 0],
                    self.matrix[kmeansPredict == 0, 1], s=100, c='red', label='cluster #1')
        plt.scatter(self.matrix[kmeansPredict == 1, 0],
                    self.matrix[kmeansPredict == 1, 1], s=100, c='blue', label='cluster #2')
        plt.scatter(self.matrix[kmeansPredict == 2, 0],
                    self.matrix[kmeansPredict == 2, 1], s=100, c='green', label='cluster #3')
        plt.scatter(kmeansModel.cluster_centers_[:, 0], kmeansModel.cluster_centers_[
            :, 1], s=100, c='yellow', label='centroids')
        plt.legend()
        plt.show()
        print(f'Centroidy: {kmeansModel.cluster_centers_}\nWynik klasteryzacji:{kmeansPredict} ')
