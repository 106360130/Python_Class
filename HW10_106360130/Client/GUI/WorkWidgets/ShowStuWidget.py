from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QScrollArea, QPushButton, QTabWidget, QGridLayout, QWidget
from GUI.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent, HintLabelComponent

import time

from SocketClient.ServiceController import ExcuteCommand
import json


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")
        
        layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(20, "Show Student")
        self.check_stu_list()  #一開始就執行動作

        #創立"scroll_area"
        self.stu_screen = QWidget()  #新增widget
        self.stu_screen.setMinimumSize(400, 2000)  #設定size
        self.scroll_area = QScrollArea()  #新增scoll area
        self.scroll_area.setWidget(self.stu_screen)  #增加到widget裡 
        self.scroll_area.setWidgetResizable(True)
        #創立"scroll_area"
        
        #"layout"中增加widget；先增加的先出現
        layout.addWidget(header_label, stretch=0.5)
        layout.addWidget(self.scroll_area)
        #"layout"中增加widget；先增加的先出現

        self.setLayout(layout)  #顯示layout

    def check_stu_list(self) :
        self.check_send = ExcuteCommand(command = "show", data = dict())
        self.check_send.start()
        self.check_send.return_sig.connect(self.show_stu_list)  #將信號連接到指定槽函數
        

    def show_stu_list(self, result) :
        result = json.loads(result)

        student_list = result['parameters']  #提取"parameters"資料，也就是我們需要的"student_list"
        #self.hint_label.setText("Add {} successfully".format(self.stu_list))
        #print("self.stu_list : {}".format(student_list))

        print ("\n==== student list ====")

    
        self.label_stu_list_top = QtWidgets.QLabel(self.stu_screen)
        self.label_stu_list_top.setText("==== student list ====")
        self.label_stu_list_top.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))

        i = 1  #控制移動座標
        for student_info in student_list :
            #print("student_info : \n{}".format(student_info))
            print("\nName : {}".format(student_info["name"]))

            #顯示name在GUI
            self.label_name = QtWidgets.QLabel(self.stu_screen)
            self.label_name.setText("Name : {}".format(student_info["name"]))
            self.label_name.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))
            self.label_name.move(0, 40*i)  #移動座標
            #顯示name在GUI

            i = i+1  #只要顯示一行，就要移動位置

            for subject in student_info["scores"] :

                scores = student_info["scores"]
                #print(type(subject))  #"str"
                print("  subject : {}, score : {}".format(subject, scores[subject]))

                #顯示subject和score在GUI
                self.label_sub_n_score = QtWidgets.QLabel(self.stu_screen)
                self.label_sub_n_score.setText("    subject : {}, score : {}".format(subject, scores[subject]))
                self.label_sub_n_score.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))
                self.label_sub_n_score.move(0, 40*i)
                i = i+1
                #顯示subject和score在GUI

                #print(score.keys())

        print ("\n======================")
        self.label_stu_list_bottom = QtWidgets.QLabel(self.stu_screen)
        self.label_stu_list_bottom.setText("======================")
        self.label_stu_list_bottom.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))
        self.label_stu_list_bottom.move(0, 40*i)

        
    def load(self):
        print("show widget")
