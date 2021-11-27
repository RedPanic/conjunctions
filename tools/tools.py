from scipy import spatial
import numpy as np
from math import sqrt


class Tools(object):
    @staticmethod
    def cosine_dist(vec1, vec2):
        '''CALCULATES COSINE DISTANCE'''
        nominator = Tools.dot(vec1, vec2)
        denominator = (Tools.dot(vec1, vec1)**.5) * (Tools.dot(vec2, vec2)**.5)
        return round((nominator/denominator), 2)

    @staticmethod
    def mul_vectors(vec1, vec2):
        '''MULTIPLIES TWO VECTORS'''
        out_vec = []
        for v1, v2 in zip(vec1, vec2):
            out_vec.append(round((v1*v2), 2))
        return out_vec

    @staticmethod
    def dot(vec1, vec2):
        return round(sum((v1*v2) for v1, v2 in zip(vec1, vec2)), 2)

    @staticmethod
    def cosine_dist_spat(vec1, vec2):
        '''CALCULATES COSINE DISTANCE FROM SCIPY.SPATIAL MODULE'''
        return round((1 - spatial.distance.cosine(vec1, vec2)), 2)

    @staticmethod
    def chebyshev_dist(vec1, vec2):
        '''CALCULATES CHEBYSHEV DISTANCE'''
        return round((spatial.distance.chebyshev(vec1, vec2)), 2)

    @staticmethod
    def manhattan_dist(vec1, vec2):
        '''CALCULATES MANHATTAN DISTANCE'''
        return round(sum(abs(v1-v2) for v1, v2 in zip(vec1, vec2)), 2)

    @staticmethod
    def normalize_vector(vec):
        normalize_vec = vec/np.linalg.norm(vec)
        return normalize_vec

    @staticmethod
    def query_results(vec1, vec2):
        '''CREATING DOCS RANKING BY MULTIPLYING VECTORS AND SUMMING IT UP'''
        return round(sum((v1*v2) for v1, v2 in zip(vec1, vec2)), 2)

    @staticmethod
    def euclidean_dist(vec1, vec2):
        '''CALCULATES EUCLIDEAN DISTANCE'''
        return round(sqrt(sum((v1-v2) ** 2 for v1, v2 in zip(vec1, vec2))), 2)

    @staticmethod
    def get_top_three(rank):
        '''GETTING RANKING OF DOCUMENTS ORDERED ASC '''
        return (sorted([(x, i) for (i, x) in enumerate(rank)]))

    @staticmethod
    def get_suggestions(vec, rank, matrix):
        '''GETTING SUGGESTIONS FROM QUERY VECTOR, TFM-IDF MATRIX, AND DOCUMENTS RANK
        '''
        closest_doc_ind = rank[0][1]
        unused_terms = [i for i in range(len(vec)) if vec[i] == 0]

        mvt_ind = unused_terms[0]
        mvt = matrix[closest_doc_ind][mvt_ind]
        for ind in unused_terms:
            if matrix[closest_doc_ind][ind] > mvt:
                mvt_ind = ind
                mvt = matrix[closest_doc_ind][ind]

        return mvt_ind
