from models.tfm.tfm import Tfm
from models.document.document import Document
from models.queryvector.queryvector import QueryVector
from tools.tools import Tools
from math import log

class Controller(object):
    def __init__(self, views):
        self.views = views
        self.welcome()
        self.documents = self.create_docs()
        self.terms_dict = self.create_terms_dict(self.create_terms())
        self.tfm_matrix = Tfm(len(self.documents), len(self.terms_dict.keys()))
        
        
        
    @property
    def terms_dict(self):
        return self._terms_dict
    
    @terms_dict.setter
    def terms_dict(self, value):
        self._terms_dict = value
        
    @property
    def documents(self):
        return self._documents
    
    @documents.setter
    def documents(self, value):
        self._documents = value
        
    @property
    def idf_vec(self):
        return self._idf_vec
    
    @idf_vec.setter
    def idf_vec(self, value):
        self._idf_vec = value
        
    @property
    def tfm_matrix(self):
        return self._tfm_matrix
    
    @tfm_matrix.setter
    def tfm_matrix(self, value):
        self._tfm_matrix = value
        
    @property
    def tfm_idf_matrix(self):
        return self._tfm_idf_matrix
    
    @tfm_idf_matrix.setter
    def tfm_idf_matrix(self, value):
        self._tfm_idf_matrix = value
        
    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, value):
        self._views = value
        
    def clear_dict_values(self, dict_obj):
        for key in dict_obj.keys():
            dict_obj[key] = 0
        
    def create_terms(self):
        query = self.views.get_query()
        qvector = QueryVector(query)
        return qvector.terms
        
    def create_terms_dict(self, terms):
        terms_dict = {term : 0 for term in terms}    
        return terms_dict
        
    def create_docs(self):
        doc_count = int(self.views.get_doc_count())
        documents = []
        for _ in range(doc_count):
            documents.append(Document(self.views.get_doc_path()))
        return documents
    
    def fill_matrix(self, terms, documents):
        for doc in documents:
            for term in terms:
                if term in doc.content:
                    terms[term] += doc.content.count(term)
            self.tfm_matrix.matrix.append(list(terms.values()))
            self.clear_dict_values(terms)
        
        self.views.display_matrix(self.tfm_matrix, terms)
        
    def create_tfm_idf_matrix(self, matrix):
        tfm_idf_matrix = []
        for row in matrix:
            tfm_idf_matrix.append(Tools.mul_vectors(row, self.idf_vec))
        return tfm_idf_matrix
        
    def calculate_idf(self, matrix):
        idf = []
        idf_out = []
        nj = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[j][i] != 0:
                    nj += 1
                   
            idf.append(nj)
            nj = 0
                    
        for item in idf:
            item = log(len(matrix) / item)
            idf_out.append(item)
            
        return idf_out
            
        
    
    def cosine_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(Tools.cosine_dist(matrix[row], doc))
                
        self.views.display_comparison_matrix(comparison_matrix, "Miara kosinusowa")
        
        
    def manhattan_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(Tools.manhattan_dist(matrix[row], doc))
                
        self.views.display_comparison_matrix(comparison_matrix, "Miara Manhattan")
        
    def euclidean_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(Tools.euclidean_dist(matrix[row], doc))
                
        self.views.display_comparison_matrix(comparison_matrix, "Miara Euklidesa")
        
    def welcome(self):
        self.views.welcome_view()
    