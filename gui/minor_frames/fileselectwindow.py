#!/usr/bin/env python
import wx

from gui.base.lctrl_base import ViewBase
#from gui.menus.main_toolbar import CustomToolBar
from service.order.data_actions import Data

keywords = {'brand': 'Бренд', 'article': 'Артикул ИМТ',
            'color': 'Артикул Цвета', 'size': 'Размер', 'item': 'Предмет',
            'gender': 'Пол', 'quantity': 'Количество',
            'price': 'Розничная цена RU', 'country': 'Страна',
            'barcode': 'Баркод'}


class FileSelection(wx.Frame):
    """ We simply derive a new class of Frame. """

    def __init__(self, data, *args, **kwargs):
        super(FileSelection, self).__init__(*args, **kwargs)
        self.splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        #self.toolbar = CustomToolBar(self.splitter)
        self.toolbar = wx.Panel(self.splitter)
        self.view = Test(self.splitter, data)
        self.splitter.SplitHorizontally(self.toolbar, self.view, 25)
        self.splitter.SetMinimumPaneSize(25)
        self.splitter.SetSashInvisible(True)
        #self.toolbar.Bind(wx.EVT_BUTTON, self.view.verify, self.toolbar.Order)

        self.CenterOnScreen()
        self.SetSize(700, 400)
        self.Show()


class Test(ViewBase):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.k = Data(data.name, keywords)

        self.set_cols(keywords)
        self.k.verify()
        self.draw(self.k.content)

    def draw(self, data: list):
        for x in data:
            self._add_line(x, check=True)


if __name__ == '__main__':
    class L:
        def __init__(self, attr):
            self.name = attr


    app = wx.App()
    data = L("/Users/rtmpb/Desktop/рус.xls")
    frame = FileSelection(data=data, parent=None, title='Test')
    frame.Show()
    app.MainLoop()
