import wx
from gui.global_events import SendSelectedViewInstance
import wx.grid
import gui.main_frame
from gui.base.lctrl_base import ViewBase
from gui.test_data import col_db3 as col


class SelectedItems(ViewBase):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent,
                         editable=True, checkboxes=True,
                         *args, **kwargs)

        self.set_cols(col)
        self.InsertColumn(len(col) + 1, 'Количество')
        self.main_frame = gui.main_frame.MainFrame.get_instance()
        wx.PostEvent(self.main_frame,
                     SendSelectedViewInstance(
                         name='SelectedItems', object=self))

    def _add_line(self, item: dict):
        super()._add_line(item)
        self.SetItem(self._row_index - 1, len(col) + 1, '1')

    def _checkall(self, state: bool):
        for x in range(self.GetItemCount()):
            self.CheckItem(x, state)
