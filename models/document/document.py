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

    def __init__(self, path=''):
        '''
        Construct new Document object.
        :param path: The path of document in filesystem
        :return: returns nothing.
        '''
        self.path = path
        self.content = self.file_content_as_str()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def file_content_as_str(self):
        '''
        Sets content of document to attribute _content as string
        :return: returns nothing.
        '''
        with open(self._path, 'r+', encoding="UTF-8") as doc_file:
            content = doc_file.read()

        return content

    def file_content_as_arr(self):
        '''
        Sets content of document to attribute _content as array of strings
        each element of array is a line of document (type string)
        :return: returns nothing
        '''
        with open(self._path, 'r+', encoding="UTF-8")as doc_file:
            self.content = doc_file.readlines()
