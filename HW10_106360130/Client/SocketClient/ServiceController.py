from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import json

class ServeiceController :
    socket_client = None  #初始化變數

    def command_sender(self, command, data):
        self.socket_client.send_command(command, data)
        result = self.socket_client.wait_responce()

        return result

class ExcuteCommand(QtCore.QThread):
    return_sig = pyqtSignal(str)

    def __init__(self, command, data):
        super().__init__()
        self.command = command
        self.data = data

    def run(self):
        result = ServeiceController.command_sender(self.command, self.data)
        #"json.dumps" : 將Python對象編碼成JSON字符串
        #"emit" : 發射訊號
        self.return_sig.emit(json.dumps(result))