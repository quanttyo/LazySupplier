import wx
from gui import bitmap_loader
from gui.data_view import DataView
from gui.base.lctrl_base import ViewBase
from gui.base.prop_splitter import PSplitter
import gui.main_frame
from gui.global_events import SendInfoPaneInstance
from urllib.request import urlopen
import io
from service.extractor import Extractor
import threading
class Pane(PSplitter):
    def __init__(self, parent):
        super().__init__(parent, proportion=0.5, minimum_pane_size=250)
        self.SplitHorizontally(Data(self), Pane(self))
        self.SetSashPosition(150)


class Data(ViewBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_cols({'a':' ', 'b':' '})


class StatsPane(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        size = wx.Size()
        size.SetWidth(3150)
        self.SetMinSize(size)

        #self.SetBackgroundColour(wx.WHITE)
        self.main_frame = gui.main_frame.MainFrame.get_instance()
        wx.PostEvent(
            self.main_frame, SendInfoPaneInstance(name="InfoPane", object=self)
        )
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.id = wx.StaticText(self, id=1, label='Info Pane!',
                                size=wx.DefaultSize, style=0,
                                name='statictext')
        self.nomenclature = wx.StaticText(self, id=2, label='n',
                                          size=wx.DefaultSize, style=0,
                                          name='nomenclature')
        buf = urlopen('http://images.wbstatic.net/c516x688/new/3080000/3089476-1.jpg').read()
        sbuf = io.BytesIO(buf)
        bmp = wx.Bitmap(1, 1).ConvertToDisabled()


        self.img = wx.StaticBitmap(self, wx.ID_ANY, bmp, wx.DefaultPosition, (50,50), 0 )

        self.sizer.Add(self.id)
        self.sizer.Add(self.nomenclature)
        self.sizer.Add(self.img)
        self.SetSizer(self.sizer)

    def set_image(self, val):
        a = Extractor(val)
        try:
            image = wx.Image(name=a.image, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        except:
            image = ''
        bmp = wx.Bitmap(image)
        self.img.SetBitmap(bmp)
        self.img.SetClientSize((100,100))


        #self.button.Bind(wx.EVT_BUTTON, self.onclick)

        #self.mainFrame = gui.main_frame.MainFrame.getInstance()


