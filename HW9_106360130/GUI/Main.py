from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import sip
import sys

#要呼叫"Client"資料夾的function
import os
Client_path = os.path.abspath(os.path.join(os.getcwd(), ".."))  #查看上級路徑
print("Client : {}".format(Client_path))
Client_path = os.path.join(Client_path, "Client")  #合併路徑

import sys
sys.path.append(Client_path)  #增加路徑
#print("Client_path : {}".format(Client_path))
#print("sys.path : {}".format(sys.path))
#要呼叫"Client"資料夾的function

#server 和 client之間傳送
from SocketClient import SocketClient
#server 和 client之間傳送


client = SocketClient()
app = QApplication([])
main_window = MainWidget(client)

main_window.setFixedSize(700, 400)  #設定視窗大小
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec_())