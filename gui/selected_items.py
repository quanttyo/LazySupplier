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
        self.Bind(wx.EVT_KEY_DOWN, self._keydown_action)

    def _add_line(self, item: dict):
        super()._add_line(item)
        self.SetItem(self._row_index - 1, len(col) + 1, '1')

    def _checkall(self, state: bool):
        for x in range(self.GetItemCount()):
            self.CheckItem(x, state)

    def set_sum(self, item, val):
        for x in item:
            self.SetItem(x, len(col) + 1, val)

    @property
    def checked_ids(self) -> list:
        items = []
        for x in range(self.ItemCount):
            if self.IsItemChecked(x):
                items.append(x)
        return items

    @property
    def checked_values(self) -> list:
        items = []
        for x in range(self.ItemCount):
            if self.IsItemChecked(x):
                items.append(
                    [self.GetItem(x, 1).GetText(),  # getting id of item
                     self.GetItem(x, self.ColumnCount - 1).GetText()])
                # getting quantity of item
        return items

    def _keydown_action(self, evt):
        if evt.GetKeyCode() == 8:
            v = self.GetFocusedItem()
            self.DeleteItem(v)
            self.Select(v - 1)
        else:
            evt.Skip()
