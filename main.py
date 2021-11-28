import sys
from controller.controller import Controller
from models.queryvector.queryvector import QueryVector
from views.views import Views
from tools.mds import MDSScaller
from tools.kmeans import KMeansTools


class App(object):
    '''Main app class'''
    @staticmethod
    def main(args):
        hc_terms = 'bo gdy że ale i oraz ani ni lub albo bądź'
        # PART 1 CREATING TFM IDF MATRIX AND DISTANCE MATRIXES, CHOOSING DATA.
        views = Views()
        controller = Controller(views, hc_terms)
        # controller = Controller(views) # for part 1
        controller.fill_matrix(controller.terms_dict, controller.documents)
        controller.views.display_matrix(
            controller.tfm_matrix, controller.terms_dict)
        controller.idf_vec = controller.calculate_idf(
            controller.tfm_matrix.matrix)
        controller.views.display_docs(controller.documents)
        controller.fill_tfm_idf_matrix(controller.tfm_matrix.matrix)
        controller.views.display_matrix(
            controller.tfm_idf_matrix, controller.terms_dict, "=========== Macierz TFM-IDF ===========")

        cosiMatrix = controller.cosine_cmp_matrix(
            controller.tfm_idf_matrix.matrix)
        mannMatrix = controller.manhattan_cmp_matrix(
            controller.tfm_idf_matrix.matrix)
        euklMatrix = controller.euclidean_cmp_matrix(
            controller.tfm_idf_matrix.matrix)
        chebMatrix = controller.chebyshev_cmp_matrix(
            controller.tfm_idf_matrix.matrix)

        # PART 2 - MAKING CLUSTERING AND MDS SCALLING

        # print('========== MACIERZE PO PRZESKALOWANIU ==========')
        # mds_cheb = MDSScaller(chebMatrix)
        # mds_eukl = MDSScaller(euklMatrix)
        # mds_mann = MDSScaller(mannMatrix)
        # mds_cosi = MDSScaller(cosiMatrix)

        # kmeans_cheb = KMeansTools(mds_cheb.scaleMatrix())
        # kmeans_cheb.find_cluster_number()
        # kmeans_cheb.make_clustering()

        # kmeans_eukl = KMeansTools(mds_eukl.scaleMatrix())
        # kmeans_cheb.find_cluster_number()
        # kmeans_eukl.make_clustering()

        # kmeans_mann = KMeansTools(mds_mann.scaleMatrix())
        # kmeans_cheb.find_cluster_number()
        # kmeans_mann.make_clustering()

        # kmeans_cosi = KMeansTools(mds_cosi.scaleMatrix())
        # kmeans_cheb.find_cluster_number()
        # kmeans_cosi.make_clustering()

        # PART 3 - TERMS RELEVETION (SUGGESTIONS)

        # for i in range(10):
        controller.query_vector = controller.create_query_vector()
        print(
            f'========== QUERY VECTOR ==========\n{controller.query_vector.vector}')
        controller.get_docs_rank(
            controller.tfm_idf_matrix.matrix, controller.query_vector.vector)


if __name__ == '__main__':
    App.main(sys.argv)
