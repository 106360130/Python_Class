from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import sip
import sys

app = QApplication([])
main_window = MainWidget()

main_window.setFixedSize(700, 400)  #設定視窗大小
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec_())