class Tfm(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
    
    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, value):
        self._rows = value
        
    @property
    def cols(self):
        return self._cols
    
    @cols.setter
    def cols(self, value):
        self._cols = value
        
    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, value):
        self._matrix = value
        
    def __str__(self):
        out = ""
        for row in self.matrix:
            out += str(row) + "\n"
            
        return out 