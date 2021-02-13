import wx
import wx.lib.scrolledpanel
import wx.lib.mixins.listctrl as mixin


class ViewBase(wx.ListCtrl, mixin.TextEditMixin, mixin.ListRowHighlighter):
    def __init__(self, parent, id=wx.ID_ANY, editable=False, checkboxes=False,
                 *args, **kwargs):
        super().__init__(parent, id=id,
                         style=wx.LC_REPORT
                               | wx.LC_HRULES
                               | wx.LC_VRULES
                               | wx.BORDER_NONE,
                         *args, **kwargs)
        if editable:
            mixin.TextEditMixin.__init__(self)

        self._last_selected_index = None
        self._row_index = 0
        self._editable = editable
        self._checkboxes = checkboxes
        self._keywords = {}
        self._cols = []
        self.SetSingleStyle(style=wx.LC_SINGLE_SEL)
        self.EnableCheckBoxes(checkboxes)
        if checkboxes:
            self.InsertColumn(0, '', width=25)
        else:
            self.InsertColumn(0, '', width=1)

        self.Bind(wx.EVT_LIST_COL_BEGIN_DRAG, self.__on_col_begin_drag)
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self._on_right_click)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self._on_click)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_select)

    def draw(self, data: list):
        self._clear_ctrl()
        for x in data:
            self._add_line(x)
        self.Select(0)

    def OpenEditor(self, col, row):
        if col == self.GetColumnCount() - 1:
            mixin.TextEditMixin.OpenEditor(self, col, row)
        elif self._checkboxes and col == 0:
            self.CheckItem(row, True) if not self.IsItemChecked(row) else \
                self.CheckItem(row, False)

    def __on_col_begin_drag(self, event: wx.Event):
        event.Veto()

    def _on_click(self, event: wx.Event):
        pass

    def _on_right_click(self, event: wx.Event):
        pass

    def _on_select(self, event: wx.Event):
        item = self.GetItem(event.GetIndex(), 1).GetText()
        print(item)
        if self._editable:
            self.OnItemSelected(event)

    def _add_line(self, item: dict, check=False):
        self.InsertItem(self._row_index, "")
        for x in range(len(self._cols)):
            try:
                self.SetItem(self._row_index, x + 1, str(item[self._cols[x]]))
            except KeyError:
                self.SetItem(self._row_index, x + 1, str(''))
        if check:
            if not item['check']:
                self.SetItemBackgroundColour(self._row_index,
                                             wx.Colour(0xEF, 0x86, 0x86))

        self._row_index += 1

    def _clear_ctrl(self):
        self.DeleteAllItems()
        self._row_index = 0

    def set_cols(self, cols: dict, redraw: bool = False):
        self._cols = [*cols.keys()]
        names = [*cols.values()]
        if redraw:
            self.DeleteAllColumns()
        for x in range(len(cols)):
            if names[x] == 'HIDDEN':
                self.InsertColumn(x + 1, names[x], width=0)
            else:
                self.InsertColumn(x + 1, names[x], width=len(names[x]) * 25,
                                  format=wx.LIST_FORMAT_RIGHT)



