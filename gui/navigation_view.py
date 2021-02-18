import wx
from wx.lib.agw.customtreectrl import CustomTreeCtrl
from db.models.node import Node
from gui.global_events import SendSelectedTree
import gui.main_frame

from logger import logger

class NavView(CustomTreeCtrl):
    def __init__(self, parent):
        CustomTreeCtrl.__init__(self, parent, id=1900,
                                agwStyle=wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS,
                                name='nav_view')
        self.AddRoot('root')
        self.add_items()
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_sel_changed, self)
        self.main_frame = gui.main_frame.MainFrame.get_instance()

    def add_items(self):
        l = []
        try:
            for item in Node.get_pairs():
                l.append(self.AppendItem(self.GetRootItem(), text=item[1],
                                         data=wx.TreeItemData(item[2])))
                for _ in l:
                    for item in Node.get_pairs(self.GetItemData(_)):
                        l.append(self.AppendItem(_, text=item[1],
                                                 data=wx.TreeItemData(item[2])))
        except TypeError:
            logger.error('cannot create navigation_view tree')

    def on_sel_changed(self, evt: wx.Event):
        item = evt.GetItem()
        if self.get_item_level(item) == 2:
            wx.PostEvent(self.main_frame, SendSelectedTree(
                object={'item': self.GetItemData(item), 'level': 2}))
        elif self.get_item_level(item) == 3:
            wx.PostEvent(self.main_frame, SendSelectedTree(
                object={'item': self.GetItemData(item), 'level': 3,
                        'parent': self.GetItemData(self.GetItemParent(item))}))

    def get_item_level(self, arg: object):
        if self.GetItemParent(arg) == self.GetRootItem():
            return 1
        elif self.GetItemParent(self.GetItemParent(arg)) == self.GetRootItem():
            return 2
        elif not self.ItemHasChildren(arg):
            return 3

