import wx
import wx.lib.scrolledpanel
import threading
import gui.main_frame
from gui.global_events import SendDataViewInstance, DataViewItemSel
from data.db.storage import queries
from gui.base.lctrl_base import ViewBase
from gui.test_data import col_db3 as col


class DataView(ViewBase):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.main_frame = gui.main_frame.MainFrame.getInstance()
        print("dataview{}".format(self.main_frame))
        wx.PostEvent(self.main_frame, SendDataViewInstance(name='DataView', object=self))
        t = threading.Thread(target=self.thread_func(), args=(2,))

    def _on_click(self, event):
        item = self.GetItem(event.GetIndex(), 1).GetText()
        item_test = self.GetItem(event.GetIndex(), 2).GetText()
        wx.PostEvent(self.main_frame, DataViewItemSel(object=queries.nomenclature(visual=True,
                                                                              identity=item)))
        print(item_test)


    def _on_right_click(self, event):
        item, popupmenu = self.GetItem(event.GetIndex(),
                                           1).GetText(), wx.Menu()
        entries = {1: 'Edit', 2: 'Delete'}
        for k, v in entries.items():
            menuItem = popupmenu.Append(k, v)
            wrapper = lambda event: self._action(event, item)
            self.Bind(wx.EVT_MENU, wrapper, menuItem)
        self.PopupMenu(popupmenu, event.GetPoint())

    def _action(self, event, item=None):
        if event.GetId() == 1:
            print('Edit')
            ew = EditWindow(self)
            ew.Show()
        elif event.GetId() == 2:
            print('Delete')

    def thread_func(self):
        self.set_cols(col)


class EditWindow(wx.Frame):
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
        q = queries.nomenclature(visual=True, identity=1)[0]
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