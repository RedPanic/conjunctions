class QueryVector(object):
    def __init__(self, query=''):
        self.query = query
        self.terms = query.split(' ')
        self.vector = []   
    
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, value):
        self._terms = value
        
    @property
    def vector(self):
        return self._vector
    
    @vector.setter
    def vector(self, value):
        self._vector = value
        
        