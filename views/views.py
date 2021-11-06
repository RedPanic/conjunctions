import os
from time import sleep


class Views(object):
    @staticmethod
    def welcome_view():
        os.system("clear")
        print("========== ISD ANALIZA SPÓJNIKÓW ==========\n\n")

    @staticmethod
    def get_doc_count():
        doc_count = input("Podaj liczbe dokumentow do analizy:\t")
        return doc_count

    @staticmethod
    def get_doc_path():
        root_path = r'./static/documents/'
        doc_path = input("Podaj nazwę dokumentu:\t")
        return root_path + doc_path

    @staticmethod
    def get_docs_path():
        root_path = r'./static/documents/'
        return root_path

    @staticmethod
    def get_terms():
        print("========== TWORZENIE BAZY ==========")
        terms = input(
            "Podaj termy, które chcesz analizować (rozdzielone spacją):\t")
        return terms

    @staticmethod
    def get_query():
        print(f'========== WYDAWANIE ZAPYTANIA DO BAZY ==========')
        query = input("Wpisz zapytanie: ")
        return query

    @staticmethod
    def display_matrix(matrix, terms, additional_info=''):
        # os.system("clear")
        if additional_info == '':
            print("========== MACIERZ TFM ==========")
        print(additional_info)
        for key in terms.keys():
            print(key, end=' ')
        print()
        print(str(matrix))
        # sleep(5)

    @staticmethod
    def display_comparison_matrix(matrix, comparison_met=''):
        print(f"========== Porównanie Dokumentów {comparison_met} ==========")
        for row in matrix:
            print(row)

    @staticmethod
    def display_rank(docs, rank):
        counter = 0
        print(f'=========== WYNIKI ZAPYTANIA ===========')
        for pos in rank:
            path = docs[pos[1]].path[docs[pos[1]].path.rfind('/')+1:]
            print(f'Miejsce {counter+1} dokument: {path} ')
            counter += 1