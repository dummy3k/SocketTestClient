import logging
import wx
import socket
import time
from threading import Thread

log = logging.getLogger(__name__)

EVT_DATA_RECEIVED = wx.NewId()

class SocketThread(Thread):
    BUFFER_SIZE = 1024
    
    def __init__(self, notify_window):
        Thread.__init__(self)
        log.info("SocketThread init")
        self.notify_window = notify_window
        self.socket = notify_window.socket
        self.__shutdown__ = False
        
    def run(self):
        log.info("run(BUFFER_SIZE=%s)" % self.BUFFER_SIZE)
        while not self.__shutdown__:
            
            try:
                data = self.socket.recv(self.BUFFER_SIZE, socket.MSG_DONTWAIT)
                log.info("OnReceive(%s)" % repr(data))
                continue
            except socket.error, ex:
                #socket.error: [Errno 11] Resource temporarily unavailable
                if ex.errno == 11:
                    log.debug("OnReceive: " + str(ex))
                else:
                    raise

            time.sleep(1)
            #~ log.debug("wating for data...")

        
