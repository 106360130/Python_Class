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

        #"button_query"的設定
        self.button_refresh = ButtonComponent("Refresh")
        self.button_refresh.clicked.connect(self.check_stu_list)
        self.button_refresh.setEnabled(True)
        #"button_query"的設定
        

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.button_refresh, stretch=0.5)
        

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(500, 2000)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)
        


        self.hint_label = QtWidgets.QLabel(self.topFiller)
        self.hint_label.setText("== student list ==")
        self.hint_label.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))

        self.label_name = QtWidgets.QLabel(self.topFiller)
        self.label_name.setText("                                         ")
        self.label_name.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))
        self.label_name.move(0, 40)


        self.label_subject = QtWidgets.QLabel(self.topFiller)
        self.label_subject.setText("                                                                 ")
        self.label_subject.setFont(QtGui.QFont("微軟正黑體", 15, QtGui.QFont.Bold))
        self.label_subject.move(0, 80)
        
       
        
        
        
        

        layout.addWidget(self.scroll)

        self.setLayout(layout)

    def check_stu_list(self) :
        self.check_send = ExcuteCommand(command = "show", data = dict())
        self.check_send.start()
        self.check_send.return_sig.connect(self.show_stu_list)  #將信號連接到指定槽函數
        

 
    def show_stu_list(self, result) :
        result = json.loads(result)

        student_list = result['parameters']  #提取"parameters"資料，也就是我們需要的"student_list"
        #self.hint_label.setText("Add {} successfully".format(self.stu_list))
        #print("self.stu_list : {}".format(student_list))
        
    

        """
        self.label_3 = QtWidgets.QLabel(self.topFiller)
        self.label_3.setText("87")
        self.label_3.setFont(QtGui.QFont("微軟正黑體", 20, QtGui.QFont.Bold))
        self.label_3.move(0, 80)
        """

        print ("\n==== student list ====")
        i = 1
        for student_info in student_list :
            #print("student_info : \n{}".format(student_info))
            self.label_name.setText("Name : {}".format((student_info["name"])))
            print("\nName : {}".format(student_info["name"]))

            for subject in student_info["scores"] :

                scores = student_info["scores"]
                #print(type(subject))  #"str"
                self.label_subject.setText("  subject : {}, score : {}".format(subject, scores[subject]))
                print("  subject : {}, score : {}".format(subject, scores[subject]))
                #print(score.keys())

        print ("\n======================")

        




    
    def load(self):
        print("show widget")
