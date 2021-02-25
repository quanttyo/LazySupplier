import wx
import threading

import gui.main_frame
from gui.base.prop_splitter import PSplitter
from gui.global_events import SendInfoPaneInstance
from service.extractor import Extractor
from logger import logger


class ProductImage(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        bmp = wx.Bitmap(1, 1).ConvertToDisabled()
        sizer = wx.WrapSizer(wx.HORIZONTAL)
        self.image = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        sizer.Add(self.image, 1, wx.EXPAND, wx.ALL)
        self.SetSizerAndFit(sizer)

    def set_image(self, bitmap):
        self.image.SetBitmap(bitmap)

    def get_bmp(self, value):
        return wx.Image(name=value, type=wx.BITMAP_TYPE_ANY).Scale(
            *self.GetClientSize(),
            wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()


class ProductDescription(wx.ListCtrl):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, id=wx.ID_ANY,
                         style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES
                               | wx.LC_NO_HEADER | wx.BORDER_NONE,
                         *args, **kwargs)
        self.InsertColumn(0, '', width=150)
        self.InsertColumn(1, '', width=150)
        self.index = 0

    def fill_rows(self, data):
        self.index = 0
        self.DeleteAllItems()
        for k, v in data.items():
            self.InsertItem(self.index, k)
            self.SetItem(self.index, 1, v)
            self.index += 1


class InfoPane(PSplitter):
    def __init__(self, parent):
        super().__init__(parent, proportion=0.2, minimum_pane_size=385,
                         style=wx.SP_LIVE_UPDATE | wx.SP_BORDER)

        self.main_frame = gui.main_frame.MainFrame.get_instance()
        wx.PostEvent(self.main_frame,
                     SendInfoPaneInstance(name='InfoPane', object=self))

        self.image_frame = ProductImage(self)
        self.data_frame = ProductDescription(self)
        self.SplitHorizontally(self.image_frame, self.data_frame)
        self.SetSashInvisible()

    def set_preview(self, val):
        threading.Thread(target=self.get_data,
                         args=(val, self.update_ui)).start()

    def update_ui(self, image, content):
        self.data_frame.fill_rows(content)
        self.image_frame.set_image(image)

    def get_data(self, val, callback):
        logger.debug(f'nomenclature( {val=})')
        extracted = Extractor(val)

        bitmap = self.image_frame.get_bmp(extracted.image)
        wx.CallAfter(callback, bitmap, extracted.content)
