import sys
from controller.controller import Controller
from views.views import Views

class App(object):
    @staticmethod
    def main(args):
        views = Views()
        controller = Controller(views)
        controller.fill_matrix(controller.terms_dict, controller.documents)
        controller.calculate_idf(controller.tfm_matrix.matrix)
        controller.idf_vec = controller.calculate_idf(controller.tfm_matrix.matrix)
        controller.tfm_idf_matrix = controller.create_tfm_idf_matrix(controller.tfm_matrix.matrix)
        controller.views.display_matrix(controller.tfm_matrix.matrix, controller.terms_dict)
        controller.views.display_matrix(controller.tfm_idf_matrix, controller.terms_dict ,"=========== Macierz TFM-IDF ===========")
        
        # controller.cosine_cmp_matrix(controller.tfm_idf_matrix)
        controller.manhattan_cmp_matrix(controller.tfm_idf_matrix)
        controller.euclidean_cmp_matrix(controller.tfm_idf_matrix)
        
        
if __name__ == '__main__':
    App.main(sys.argv)