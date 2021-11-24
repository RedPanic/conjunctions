from scipy import spatial
import numpy as np
from math import sqrt


class Tools(object):
    @staticmethod
    def cosine_dist(vec1, vec2):
        nominator = Tools.dot(vec1, vec2)
        denominator = (Tools.dot(vec1, vec1)**.5) * (Tools.dot(vec2, vec2)**.5)
        return round((nominator/denominator), 2)

    @staticmethod
    def mul_vectors(vec1, vec2):
        out_vec = []
        for v1, v2 in zip(vec1, vec2):
            # print(f"{v1} * {v2} = {v1*v2}")
            out_vec.append(round((v1*v2), 2))
        return out_vec

    @staticmethod
    def dot(vec1, vec2):
        return round(sum((v1*v2) for v1, v2 in zip(vec1, vec2)), 2)

    @staticmethod
    def cosine_dist_spat(vec1, vec2):
        return round((1 - spatial.distance.cosine(vec1, vec2)), 2)

    @staticmethod
    def chebyshev_dist(vec1, vec2):
        return round((spatial.distance.chebyshev(vec1, vec2)), 2)

    @staticmethod
    def manhattan_dist(vec1, vec2):
        return round(sum(abs(v1-v2) for v1, v2 in zip(vec1, vec2)), 2)

    @staticmethod
    def normalize_vector(vec):
        normalize_vec = vec/np.linalg.norm(vec)
        return normalize_vec

    @staticmethod
    def query_results(vec1, vec2):
        return round(sum((v1*v2) for v1, v2 in zip(vec1, vec2)), 2)

    @staticmethod
    def euclidean_dist(vec1, vec2):
        return round(sqrt(sum((v1-v2) ** 2 for v1, v2 in zip(vec1, vec2))), 2)

    @staticmethod
    def get_top_three(rank):
        return (sorted([(x, i) for (i, x) in enumerate(rank)], reverse=True))

    @staticmethod
    def get_suggestions(vec, rank, matrix):
        closest_doc_ind = rank[0][1]
        used_terms = [i for i in range(len(vec)) if vec[i] > 0]
        mvt_ind = used_terms[0] + 1
        mvt = matrix[closest_doc_ind][mvt_ind]
        for ind in range(len(matrix[closest_doc_ind])):
            if ind in used_terms:
                continue
            if matrix[closest_doc_ind][ind] > mvt:
                mvt_ind = ind

        return mvt_ind
