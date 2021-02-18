import wx
import wx.lib.scrolledpanel
import threading
import gui.main_frame
from gui.global_events import SendDataViewInstance, DataViewItemSel
from db.models.nomenclature import Nomenclature
from gui.base.lctrl_base import ViewBase
from gui.minor_frames.nomenclature_edit import NomenclatureEditWindow
from gui.test_data import col_db3 as col


class DataView(ViewBase):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, id=1901, *args, **kwargs)

        self.main_frame = gui.main_frame.MainFrame.get_instance()
        wx.PostEvent(
            self.main_frame, SendDataViewInstance(name="DataView", object=self)
        )
        t = threading.Thread(target=self.thread_func(), args=(2,))
        self.Bind(wx.EVT_NAVIGATION_KEY, self.__change_focus)

    def _on_click(self, event):
        item = self.GetItem(event.GetIndex(), 1).GetText()
        wx.PostEvent(
            self.main_frame,
            DataViewItemSel(object=Nomenclature.get(visual=True,
                                               identity=item)),
        )

    def _on_right_click(self, evt):
        item, popupmenu = self.GetItem(evt.GetIndex(), 1).GetText(), wx.Menu()
        entries = {1: "Edit", 2: "Delete"}
        for k, v in entries.items():
            menu_item = popupmenu.Append(k, v)
            wrapper = lambda e: self._action(e)
            self.Bind(wx.EVT_MENU, wrapper, menu_item)
        self.PopupMenu(popupmenu, evt.GetPoint())

    def _action(self, evt):
        if evt.GetId() == 1:
            print("Edit")
            ew = NomenclatureEditWindow(self)
            ew.Show()
        elif evt.GetId() == 2:
            print("Delete")

    def thread_func(self):
        self.set_cols(col)

    def __change_focus(self, evt):
        self.FindWindowById(1900, self.main_frame).SetFocus()
