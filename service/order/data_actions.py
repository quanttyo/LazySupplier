import xlrd
import xlwt
from dataclasses import dataclass
from data import *
from data.db.storage import queries
import threading


class Data:
    __data = []

    def __init__(self, filepath: str = None, keyword: dict = None):
        self.__import_data(filepath, keyword) if filepath and keyword else None

    def __import_data(self, filepath: str, keywords: dict):
        data = xlrd.open_workbook(filepath).sheet_by_index(0)
        self.indices = self.__get_indices(data, keywords)
        for x in range(1, data.nrows):
            temp_dict = {}
            for val in self.indices:
                temp_dict.update({self.indices[val]:
                                      data.row_values(x,
                                                      start_colx=val,
                                                      end_colx=val + 1)[0]})
            self.__data.append(temp_dict)

    def __get_indices(self, data: xlrd.sheet, kwargs: dict) -> dict:
        indices = []
        for x in [*kwargs.values()]:
            try:
                indices.append(data.row_values(0).index(x))
            except ValueError:
                continue
        return dict(zip(indices, [*kwargs.keys()]))

    def __write(self):
        pass

    def verify(self):
        t = threading.Thread(target=self.__thread_verify())
        t.start()

    def __thread_verify(self):
        list(map(lambda d:
                 d.update({'check': queries.nomenclature_exist_barcode
                 (d['barcode'])}), self.content))
    @property
    def content(self):
        return self.__data

    def __repr__(self):
        return "Data({})".format(self.content)
