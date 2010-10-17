import logging

if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig("logging.conf")

import wx
import socket

log = logging.getLogger(__name__)

class MainWindow(wx.Frame):
    def __init__(self, parent=None, id=wx.ID_ANY,
                 pos=wx.DefaultPosition):

        wx.Frame.__init__(self, parent, id,
                          title="Socket Test Client", pos=pos,
                          size=(640,480), style=wx.DEFAULT_FRAME_STYLE)
        log.debug("MainWindow Init")

        sizer = wx.BoxSizer(wx.VERTICAL)
        
        t = wx.TextCtrl(self, -1, "Test it out and see", size=(-1, -1),
                        style=wx.TE_MULTILINE)
        t.SetSize(t.GetBestSize())
        sizer.Add(t, wx.EXPAND, wx.EXPAND)

        t = wx.TextCtrl(self, -1, "Test it out and see", size=(-1, -1))
        t.SetSize(t.GetBestSize())
        sizer.Add(t, 0, wx.EXPAND)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        self.Layout()
#        self.SetSize(sizer.GetMinSize())
        
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)

        menu_parent = wx.Menu()
        menuBar.Append(menu_parent, "Socket")

        menu_item = wx.MenuItem(menu_parent, wx.ID_ANY, text="Connect")
        menu_parent.AppendItem(menu_item)
        self.Bind(wx.EVT_MENU, self.OnConnect, menu_item)

        menu_item = wx.MenuItem(menu_parent, wx.ID_ANY, text="Listen")
        menu_parent.AppendItem(menu_item)
        self.Bind(wx.EVT_MENU, self.OnTest, menu_item)

        menu_item = wx.MenuItem(menu_parent, wx.ID_SEPARATOR)
        menu_parent.AppendItem(menu_item)

        menu_item = wx.MenuItem(menu_parent, wx.ID_ANY, text="Exit")
        menu_parent.AppendItem(menu_item)
        self.Bind(wx.EVT_MENU, self.OnExit, menu_item)


    def OnTest(self, e):
        pass

    def OnExit(self, e):
        self.Close()

    def OnConnect(self, e):
        HOST = '127.0.0.1'
        PORT = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('Hello, world')
        #~ data = s.recv(1024)
        s.close()

        
if __name__ == '__main__':
    log.debug("Hello");

    app = wx.App()
    main_window = MainWindow()
    main_window.Show(True)

    log.info("entering main loop")
    app.MainLoop()
    
