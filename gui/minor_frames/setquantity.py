import wx
from wx.lib.intctrl import IntCtrl

import gui.main_frame
from gui.global_events import SelViewAction


class SetQuantity(wx.Frame):
    def __init__(self, parent):
        self.main_frame = gui.main_frame.MainFrame.get_instance()
        super().__init__(parent, id=wx.ID_ANY, title='Edit frame',
                         style=wx.BORDER_THEME | wx.FRAME_NO_WINDOW_MENU,
                         size=(165, 40))
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.data_sizer = wx.BoxSizer()
        self.control_sizer = wx.BoxSizer()

        self.label = wx.StaticText(self, id=wx.ID_ANY,
                                   label='Установить кол-во: ')
        self.int_ctrl = IntCtrl(self,
                                id=wx.ID_ANY,
                                default_color=wx.SystemSettings
                                .GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.btn_submit = wx.Button(self, id=101, label='Submit')
        self.btn_cancel = wx.Button(self, id=102, label='Cancel')

        self.btn_submit.Bind(wx.EVT_BUTTON, self._action)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self._action)
        self.int_ctrl.Bind(wx.EVT_KEY_DOWN, self._btn_push)

        self.data_sizer.Add(self.label)
        self.data_sizer.Add(self.int_ctrl)
        self.sizer.Add(self.data_sizer)
        self.control_sizer.Add(self.btn_submit, flag=wx.ALIGN_CENTRE)
        self.control_sizer.Add(self.btn_cancel, flag=wx.ALIGN_CENTRE)
        self.sizer.Add(self.control_sizer)
        self.SetSizer(self.sizer)

    def _action(self, evt):
        if evt.GetId() == 101:
            wx.PostEvent(self.main_frame, SelViewAction(
                action='quantity',
                object=str(
                    self.int_ctrl.GetValue())))
            self.Close()
        elif evt.GetId() == 102:
            self.Close()

    def _btn_push(self, evt):
        if evt.GetKeyCode() == 13:
            self.btn_submit.GetEventHandler().ProcessEvent(
                wx.PyCommandEvent(wx.EVT_BUTTON.typeId,
                                  self.btn_submit.GetId()))
        elif evt.GetKeyCode() == 27:
            self.Close()
        else:
            evt.Skip()
