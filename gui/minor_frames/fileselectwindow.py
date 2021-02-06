#!/usr/bin/env python
import wx
import threading

import xlrd
from gui.base.lctrl_base import ViewBase
from data.db.storage import queries
from gui.menus.main_toolbar import CustomToolBar

keywords = {'brand': 'Бренд', 'article': 'Артикул ИМТ', 'color': 'Артикул Цвета', 'size': 'Размер', 'item': 'Предмет',
            'gender': 'Пол', 'quantity': 'Количество', 'price': 'Розничная цена RU', 'country': 'Страна',
            'barcode': 'Баркод'}


class Data:
    __data = []

    def __init__(self, data_from_table: xlrd = None, keyword: dict = None) -> None:
        if data_from_table and keyword:
            self.keywords = keyword
            self.__import_data_xlrd(data_from_table)

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

    def __write(self):
        pass

    def verify(self):
        import threading
        t = threading.Thread(target=self.__thread_verify())

    def __thread_verify(self):
        for x in self.content:
            x['check'] = \
                queries.nomenclature_exist_barcode(x['barcode'])

    @property
    def content(self):
        return self.__data

    def __repr__(self):
        return "Data({})".format(self.content)


class FileSelection(wx.Frame):
    """ We simply derive a new class of Frame. """

    def __init__(self, data, *args, **kwargs):
        super(FileSelection, self).__init__(*args, **kwargs)
        self.splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        self.toolbar = CustomToolBar(self.splitter)
        self.view = Test(self.splitter, data)
        self.splitter.SplitHorizontally(self.toolbar, self.view, 25)
        self.splitter.SetMinimumPaneSize(25)
        self.splitter.SetSashInvisible(True)
        self.toolbar.Bind(wx.EVT_BUTTON, self.view.verify, self.toolbar.Order)

        self.CenterOnScreen()
        self.SetSize(700, 400)
        self.Show()


class Test(ViewBase):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.k = Data(data, keywords)

        self.set_cols(keywords)
        self.k.verify()
        self.draw(self.k.content)

    def verify(self, event):
        pass


if __name__ == '__main__':
    from data.db.storage import queries


    class L:
        def __init__(self, attr):
            self.name = attr


    app = wx.App()
    data = L("/Users/rtmpb/Desktop/рус.xls")
    frame = FileSelection(data=data, parent=None, title='Test')
    frame.Show()
    app.MainLoop()
