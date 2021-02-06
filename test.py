import data.db
import data.storage
from sqlalchemy.orm import query
import xlrd

data.db.storage_meta.create_all()
from data.storage import Node
from sqlalchemy import insert
import data.db


def _addRow(data, cls, map):
    instance = cls()
    setattr(instance, map[1], data)
    setattr(instance, map[2], 1)
    data.db.storage_session.add(instance)


brandMap = ['brandID', 'brandNAME', 'jpID']
jpMap = ['jpID', 'jpNAME']


# _addRow('two', data.storage.Brand)
# _addRow('some2', data.storage.Jp, jpMap)
# _addRow('somebrand', data.storage.Brand, brandMap)
# data.db.storage_session.commit()


# q = query.Query([Brand], session=data.db.storage_session).all()
# print(q[0].attributes)
# print(q[0][0].value)
# print(q[0].value)
# session.add(m1)
# session.commit()

def _addNode(cls, id, root, name):
    instance = cls()
    if id is None:
        return ''
    setattr(instance, 'id', id)
    setattr(instance, 'root_id', root)
    setattr(instance, '_name', name)
    data.db.storage_session.add(instance)


from data.db import get_storage_session


def extendNode(cls, root, name):
    instance = cls()
    # setattr(instance, 'root_id', root)
    # setattr(instance, '_name', name)
    instance.__root_id = 1
    instance.__name = 'tesos'
    get_storage_session().add(instance)


# data.db.storage_session.commit()

# q = queries.roots_node('rootnode')
# z = queries.nomenclature()
# for item in z:
#    print(item)

# col_db2 = ['n_id', 'n_brand', 'n_color', 'n_size', 'n_barcode', 'n_price', 'n_item', 'n_wb']

# extendNode(Node, 1, 'test00000')
# get_storage_session().commit()
# Node.addrow(1, 'test1111')
# get_storage_session().commit()
# for x in col_db2:
#    print(getattr(z[0], x))
# for x in q:
# print(q)
# queries.roots(3)


# def some(d):
#    some = re.compile(":(.*)").findall(str(d).replace("'", ""))
#   return some[0] if some else None

from data.db.storage import queries


class Data:
    __data = []

    def __init__(self, data_from_table: xlrd = None, keyword: dict = None) -> None:
        if data_from_table and keyword:
            self.keywords = keyword
            self.__import_data_xlrd(data_from_table)
            self.verify()
    def __import_data_xlrd(self, imported: xlrd) -> None:
        self.data = xlrd.open_workbook(imported.name).sheet_by_index(0)
        self.indices = self.__get_indices(self.data, self.keywords)
        for x in range(1, self.data.nrows):
            temp_dict = {}
            for val in self.indices:
                temp_dict.update({self.indices[val]: self.data.row_values(x, start_colx=val, end_colx=val + 1)[0]})
            self.__data.append(temp_dict)

    def __get_indices(self, data: xlrd.sheet, kwargs: dict) -> dict:
        indices = []
        for x in [*kwargs.values()]:
            try:
                indices.append(data.row_values(0).index(x))
            except ValueError:
                continue
        return dict(zip(indices, [*kwargs.keys()]))

    def if_exist(self, val):
        if queries.nomenclature_barcode(val['barcode']):
            return True
        else:
            return False
    def verify(self):
        print(queries.nomenclature_barcode('WBLCSE0000000880'))
    @property
    def content(self):
        return self.__data

    def __repr__(self):
        return "Data({})".format(self.content)


keywords = {'brand': 'Бренд', 'article': 'Артикул ИМТ', 'color': 'Артикул Цвета', 'size': 'Размер', 'item': 'Предмет',
            'gender': 'Пол', 'quantity': 'Количество', 'price': 'Розничная цена RU', 'country': 'Страна',
            'barcode': 'Баркод'}


# data = xlrd.open_workbook("\\\Mac\Home\Desktop\рус.xls").sheet_by_index(0)



d = {'barcode':'WBLCSE0000000880'}

#o = queries.nomenclature_item_test(16)

def _addRow(data, cls, map):
    instance = cls()
    setattr(instance, map[1], data)
    setattr(instance, map[2], 1)
    data.db.storage_session.add(instance)

def write():
    get_storage_session()



print(queries.nomenclature_exist_barcode('gregerger1'))