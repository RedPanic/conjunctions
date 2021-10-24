import sys
from controller.controller import Controller
from views.views import Views

class App(object):
    @staticmethod
    def main(args):
        views = Views()
        controller = Controller(views)
        controller.fill_matrix(controller.terms_dict, controller.documents)
        controller.cosine_cmp_matrix(controller.tfm_matrix.matrix)
        controller.manhattan_cmp_matrix(controller.tfm_matrix.matrix)
        controller.euclidean_cmp_matrix(controller.tfm_matrix.matrix)
        
        
if __name__ == '__main__':
    App.main(sys.argv)