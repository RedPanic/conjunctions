'''
    Filename: document.py
    Author: r00ser (Michał Postek)
    Date of creation: 2021-10-23
    Description: File contains source code of Document class
'''


class Document(object):
    '''
        Document - class for handling operations on documents
        Encapsulates path and content of document.
        
    '''
    def __init__(self, path):
        '''
        Construct new Document object.
        :param path: The path of document in filesystem
        :return: returns nothing.
        '''
        self._path = path
        self._content = ""
        
    def get_file_content_as_str(self):
        '''
        Sets content of document to attribute _content as string
        :return: returns nothing.
        '''
        with open(self._path, 'r+', encoding="UTF-8") as doc_file:
            self._content = doc_file.read()
            
    def get_file_content_as_arr(self):
        '''
        Sets content of document to attribute _content as array of strings
        each element of array is a line of document (type string)
        :return: returns nothing
        '''
        with open(self._path, 'r+', encoding="UTF-8")as doc_file:
            self._content = doc_file.readlines()
            
    def get_content(self):
        '''
            Gives access to _content attribute
            :return: returns content of document
        '''
        return self._content
    
    def get_path(self):
        '''
            Gives access to _path attribute
            :return: returns path of document
        '''
        return self._path
        