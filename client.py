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
        self.socket = None

        sizer = wx.BoxSizer(wx.VERTICAL)
        
        t = wx.TextCtrl(self, -1, "Test it out and see", size=(-1, -1),
                        style=wx.TE_MULTILINE)
        t.SetSize(t.GetBestSize())
        sizer.Add(t, wx.EXPAND, wx.EXPAND)

        t = wx.TextCtrl(self, -1, "Test it out and see", size=(-1, -1),
                        style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnSend, t)
        t.SetSize(t.GetBestSize())
        sizer.Add(t, 0, wx.EXPAND)
        self.txtSend = t

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
        self.mnuConnect = menu_item

        menu_item = wx.MenuItem(menu_parent, wx.ID_ANY, text="Listen")
        menu_parent.AppendItem(menu_item)
        self.Bind(wx.EVT_MENU, self.OnTest, menu_item)
        self.mnuListen = menu_item

        menu_item = wx.MenuItem(menu_parent, wx.ID_ANY, text="Close")
        menu_parent.AppendItem(menu_item)
        self.Bind(wx.EVT_MENU, self.OnDisconnect, menu_item)
        self.mnuClose = menu_item
        self.mnuClose.Enable(False)

        menu_item = wx.MenuItem(menu_parent, wx.ID_SEPARATOR)
        menu_parent.AppendItem(menu_item)

        menu_item = wx.MenuItem(menu_parent, wx.ID_ANY, text="Exit")
        menu_parent.AppendItem(menu_item)
        self.Bind(wx.EVT_MENU, self.OnExit, menu_item)

    def IsConnected(self):
        if self.socket == None:
            return False

        return True

    def EnableMenus(self):
        self.mnuConnect.Enable(not self.IsConnected())
        self.mnuListen.Enable(not self.IsConnected())
        self.mnuClose.Enable(self.IsConnected())
        
    def OnTest(self, event):
        pass

    def OnExit(self, event):
        self.Close()

    def OnDisconnect(self, event):
        self.socket.close()
        self.socket = None
        self.EnableMenus()

    def OnConnect(self, event):
        HOST = '127.0.0.1'
        PORT = 12345
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))
        log.info("connected to %s:%s" % (HOST, PORT))
        #~ data = s.recv(1024)
        #~ s.close()
        self.EnableMenus()

    def OnSend(self, event):
        event.Skip()

        data = self.txtSend.GetValue()
        log.debug("OnSend('%s')" % data)
        self.socket.send(data + '\n')
        self.txtSend.SetValue("")
        
if __name__ == '__main__':
    log.debug("Hello");

    app = wx.App()
    main_window = MainWindow()
    main_window.Show(True)

    log.info("entering main loop")
    app.MainLoop()
    
