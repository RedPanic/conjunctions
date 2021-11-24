from sklearn.manifold import MDS 
import numpy as np

class MDSScaller(object):
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        
    
    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, value):
        self._matrix = value
        
    @property
    def mdsObj(self):
        return self._mdsObj
    
    @mdsObj.setter
    def mdsObj(self, value):
        self._mdsObj = value
        
    def scaleMatrix(self):
        self.mdsObj = MDS(dissimilarity='precomputed', random_state=0)
        transposedMatrix = self.mdsObj.fit_transform(self.matrix)  
        return transposedMatrix     
    