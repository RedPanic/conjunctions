from scipy import spatial
from math import sqrt

class Tools(object):
    @staticmethod
    def cosine_dist(vec1, vec2):
        nominator = Tools.dot(vec1,vec2)
        denominator = ( Tools.dot(vec1, vec1)**.5  ) * (Tools.dot(vec2, vec2)**.5)
        return nominator/denominator
    
    @staticmethod
    def dot(vec1, vec2):
        return sum((v1*v2) for v1, v2 in zip(vec1, vec2))
    
    @staticmethod
    def cosine_dist_spat(vec1, vec2):
        return 1 - spatial.distance.cosine(vec1,vec2)
    
    @staticmethod
    def manhattan_dist(vec1, vec2):
        return sum(abs(v1-v2) for v1,v2 in zip(vec1,vec2))
    
    @staticmethod
    def euclidean_dist(vec1, vec2):
        return sqrt( sum((v1-v2) ** 2 for v1, v2 in zip(vec1, vec2)) )