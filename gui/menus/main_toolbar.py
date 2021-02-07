import wx

import gui.main_frame
from gui.minor_frames.setquantity import SetQuantity
from gui.global_events import SelViewCheckAll



class MainToolBar(wx.ToolBar):
    def __init__(self, parent):
        wx.ToolBar.__init__(self, parent, wx.ID_ANY,
                            style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT)

        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR)
        paste_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR)
        self.AddTool(10, 'New', new_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "New",
                     'Long New')
        self.AddTool(20, 'Open', open_bmp, wx.NullBitmap, wx.ITEM_NORMAL,
                     "Open", 'Long New')

        self.Realize()


class CustomToolBar(wx.ToolBar):
    def __init__(self, parent):
        self.main_frame = gui.main_frame.MainFrame.get_instance()
        wx.ToolBar.__init__(self, parent, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.check_all = wx.CheckBox(parent, id=777)
        self.summary = wx.Button(self, id=wx.ID_ANY, label='Указать кол-во',
                                 size=(200, 20))
        self.print = wx.Button(self, id=wx.ID_ANY, label='Печать',
                               size=(100, 20))
        self.make_order = wx.Button(self, id=wx.ID_ANY, style=wx.ALIGN_RIGHT,
                                    label='Создать заказ',
                                    size=(120, 20))

        sizer.AddSpacer(5)
        sizer.Add(self.check_all)
        sizer.AddSpacer(20)
        sizer.Add(self.summary)
        sizer.Add(self.print)
        sizer.Add(self.make_order)
        self.SetSizer(sizer)

        self.summary.Bind(wx.EVT_BUTTON, self.f_summary)
        self.print.Bind(wx.EVT_BUTTON, self.f_print)
        self.make_order.Bind(wx.EVT_BUTTON, self.f_make_order)
        self.check_all.Bind(wx.EVT_CHECKBOX, self._checkall)

    def f_summary(self, evt):
        frame = SetQuantity(self)
        frame.Show()

    def f_print(self, evt):
        print('f_print {}'.format(evt.GetId()))

    def f_make_order(self, evt):
        print('f_make_order {}'.format(evt.GetId()))

    def _checkall(self, event):
        wx.PostEvent(self.main_frame, SelViewCheckAll(
            state=wx.FindWindowById(id=event.GetId()).Value))
