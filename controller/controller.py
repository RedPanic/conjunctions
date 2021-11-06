from models.tfm.tfm import Tfm
from models.document.document import Document
from models.queryvector.termsvector import TermsVector
from models.queryvector.queryvector import QueryVector
from tools.tools import Tools
from tools.filetools import FileTools
from math import log


class Controller(object):
    def __init__(self, views):
        self.views = views
        self.welcome()
        self.documents = self.create_docs()
        self.terms_dict = self.create_terms_dict(self.create_terms())
        self.tfm_matrix = Tfm(len(self.documents), len(self.terms_dict.keys()))
        self.tfm_idf_matrix = Tfm(
            len(self.documents), len(self.terms_dict.keys()))
        self.query_vector = QueryVector()

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
    def query_vector(self):
        return self._query_vector

    @query_vector.setter
    def query_vector(self, value):
        self._query_vector = value

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
        query = self.views.get_terms()
        terms_vector = TermsVector(query)
        return terms_vector.terms

    def create_query_vector(self):
        query = self.views.get_query()
        query_vector = QueryVector(query)
        for key in self.terms_dict.keys():
            if key in query_vector.terms:
                query_vector.vector.append(1)
            else:
                query_vector.vector.append(0)

        query_vector.vector = Tools.normalize_vector(query_vector.vector)
        return query_vector

    def get_docs_rank(self, matrix, vec):
        documents = []

        for row in range(len(matrix)):
            documents.append(Tools.query_results(matrix[row], vec))

        rank = Tools.get_top_three(documents)
        self.views.display_rank(self.documents, rank)

    def create_terms_dict(self, terms):
        terms_dict = {term: 0 for term in terms}
        return terms_dict

    def create_docs(self):
        documents_paths = FileTools.get_files_from_dir(
            self.views.get_docs_path())
        documents = []
        for doc in documents_paths:
            documents.append(Document(doc))
        return documents

    def create_docs_from_files(self):
        doc_count = int(self.views.get_doc_count())
        documents = []
        for _ in range(doc_count):
            documents.append(Document(self.views.get_doc_path()))
        return documents

    def fill_matrix(self, terms, documents):
        for doc in documents:
            for term in terms:
                if term in doc.content:
                    terms[term] += doc.content.lower().count(' ' + term + ' ')
            self.tfm_matrix.matrix.append(list(terms.values()))
            self.clear_dict_values(terms)

    def fill_tfm_idf_matrix(self, matrix):
        for row in matrix:
            self.tfm_idf_matrix.matrix.append(
                Tools.mul_vectors(row, self.idf_vec))

    def calculate_idf(self, matrix):
        idf = []
        idf_out = []
        nj = 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                #print(f"Seria {i}: Wartość: {matrix[j][i]}")
                if matrix[j][i] != 0:
                    nj += 1

            idf.append(nj)
            nj = 0

        for item in idf:
            item = log(len(matrix) / item)
            idf_out.append(item)

        return idf_out

    def chebyshev_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(
                    Tools.chebyshev_dist(matrix[row], doc))

        self.views.display_comparison_matrix(
            comparison_matrix, "Miara Czebyszewa")

    def cosine_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(
                    Tools.cosine_dist(matrix[row], doc))

        self.views.display_comparison_matrix(
            comparison_matrix, "Miara kosinusowa")

    def manhattan_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(
                    Tools.manhattan_dist(matrix[row], doc))

        self.views.display_comparison_matrix(
            comparison_matrix, "Miara Manhattan")

    def euclidean_cmp_matrix(self, matrix):
        comparison_matrix = []
        for row in range(len(matrix)):
            comparison_matrix.append([])
            for doc in matrix:
                comparison_matrix[row].append(
                    Tools.euclidean_dist(matrix[row], doc))

        self.views.display_comparison_matrix(
            comparison_matrix, "Miara Euklidesa")

    def welcome(self):
        self.views.welcome_view()
