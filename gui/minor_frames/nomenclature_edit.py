import wx

from db.models.nomenclature import Nomenclature
from gui.base.lctrl_base import ViewBase


class NomenclatureEditWindow(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, title='Edit frame',
                         size=(400, 400))
        self.splitter = wx.SplitterWindow(self, wx.SP_LIVE_UPDATE)
        self.view = ViewBase(self.splitter)
        self.toolbar = wx.ToolBar(self.splitter)
        self.splitter.SplitHorizontally(self.toolbar, self.view, 25)

        l = ['Бренд',
             'Артикул',
             'Цвет',
             'Размер',
             'Баркод',
             'Цена',
             'Предмет',
             'Номенклатура']

    def draw(self, l):
        q = Nomenclature.get(visual=True, identity=1)[0]
        i = 0
        if 'n_id' in q:
            del q['n_id']
        for x in range(len(l)):
            z = self.fgSizer.GetItemById(x)
            print(z)

    def _on_submit(self, event):
        print('_on_submit')
        print(event.GetId())

    def _on_cancel(self, event):
        print('_on_cancel')