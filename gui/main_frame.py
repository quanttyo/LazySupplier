import wx
from gui.menus.main_menubar import MainMenuBar
from gui.item_browser import ItemBrowser
from gui.multi_switch import FitMultiSwitch
from db.models.nomenclature import Nomenclature
from gui.global_events import EVT_DV_INS, EVT_SV_INS, EVT_TREE_SEL, EVT_DV_SEL, \
    EVT_SV_AC, EVT_IP_INS, EVT_SEL

import threading


class MainFrame(wx.Frame):
    __instance = None

    @classmethod
    def get_instance(cls):
        return cls.__instance if cls.__instance is not None else MainFrame()

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="tool",
                          style=wx.DEFAULT_FRAME_STYLE,
                          size=(1150, 750))
        MainFrame.__instance = self

        self.SetMenuBar(MainMenuBar())
        # Arrangement of left side of mainFrame,
        # instances of ItemBrowser and MultiSwitch
        self.splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        self.item_browser = ItemBrowser(self.splitter)
        self.fitMultiSwitch = FitMultiSwitch(self.splitter)
        self.fitMultiSwitch.add_tab()
        self.fitMultiSwitch.add_tab2()

        self.splitter.SplitVertically(self.item_browser, self.fitMultiSwitch)
        self.splitter.SetSashPosition(300)
        self.splitter.SetSashInvisible(True)

        # Seeking events
        self.instances = {}
        self.Bind(EVT_DV_INS, self.receiving_an_instance)
        self.Bind(EVT_SV_INS, self.receiving_an_instance)
        self.Bind(EVT_IP_INS, self.receiving_an_instance)
        self.Bind(EVT_TREE_SEL, self.tree_item_selected)
        self.Bind(EVT_DV_SEL, self.item_selected)
        self.Bind(EVT_SV_AC, self.selected_view_action)
        self.Bind(EVT_SEL, self.selected)

        # Show ourselves
        self.Show()

        # Events actions

    def receiving_an_instance(self, evt: wx.Event):
        """ Receiving an instance from wx.PostEvent from other object, """
        self.instances[evt.name] = evt.object

    def tree_item_selected(self, evt: wx.Event):
        self.instances['DataView'].draw(Nomenclature
                                        .get_specific(**evt.object))
        self.instances['DataView'].SetFocus()

    def item_selected(self, evt: wx.Event):
        self.instances['SelectedItems']._add_line(evt.object[0])

    def selected_view_checkall(self, evt: wx.Event):
        self.instances['SelectedItems']._checkall(evt.state)

    def selected_view_action(self, evt: wx.Event):
        instance = self.instances['SelectedItems']
        if evt.action == 'checkall':
            instance._checkall(evt.object)
        elif evt.action == 'quantity':
            instance.set_sum(instance.checked_ids, evt.object)
        elif evt.action == 'make_order':
            print(instance.checked_values)
        else:
            print('SelViewAction: {}'.format(evt.action))

    def selected(self, evt):
        self.instances['InfoPane'].id.SetLabelText(evt.id)
        self.instances['InfoPane'].nomenclature.SetLabelText(evt.nomenclature)
        self.instances['InfoPane'].set_image(evt.nomenclature)


