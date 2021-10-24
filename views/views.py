import os

class Views(object):
    @staticmethod
    def welcome_view():
        os.system("clear")
        print("========== ISD ANALIZA SPÓJNIKÓW ==========")
        
    @staticmethod
    def get_doc_count():
        doc_count = input("Podaj liczbe dokumentow do analizy:\t")
        return doc_count
    
    @staticmethod
    def get_doc_path():
        doc_path = input("Podaj ścieżkę do dokumentu:\t")
        return doc_path
    
    @staticmethod
    def get_query():
        query = input("Podaj termy, które chcesz analizować (rozdzielone spacją):\t")
        return query
    
    @staticmethod
    def display_matrix(matrix, terms, additional_info=''):
        os.system("clear")
        print("========== MACIERZ TFM ==========")
        print(additional_info, end="")
        for key in terms.keys():
            print(key, end=' ')
        print()
        print(str(matrix))    
        
    @staticmethod 
    def display_comparison_matrix(matrix, comparison_met =''):
        print(f"========== Porównanie Dokumentów {comparison_met} ==========")
        for row in matrix:
            print(row)
        