#要呼叫"Client"資料夾的function
import os
Client_path = os.path.abspath(os.path.join(os.getcwd(), ".."))  #查看上級路徑
Client_path = os.path.join(Client_path, "Client")  #合併路徑
import sys
sys.path.append(Client_path)  #增加路徑
print("Client_path : {}".format(Client_path))
print("sys.path : {}".format(sys.path))
#要呼叫"Client"資料夾的function