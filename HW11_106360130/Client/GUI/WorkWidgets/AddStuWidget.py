from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent, HintLabelComponent

import json


#要呼叫"SocketClient"資料夾的function
"""
import os
Client_path = os.path.abspath(os.path.join(os.getcwd(), ".."))  #查看上級路徑
Client_path = os.path.join(Client_path, "SocketClient")  #合併路徑
import sys
sys.path.append(Client_path)  #增加路徑
# print("Client_path : {}".format(Client_path))
# print("sys.path : {}".format(sys.path))
"""
#要呼叫"SocketClient"資料夾的function

from SocketClient.ServiceController import ExcuteCommand

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")
        #"stu_list"初始化
        self.stu_list = {}
        self.stu_list["name"] = {}
        self.stu_list["scores"] = {}
        #"stu_list"初始化


        self.query_name = False  #紀錄是否有輸入"name"且"query"過了
        self.input_subject = False  #紀錄是否有增加過"subject"和"score"了

        layout = QtWidgets.QGridLayout()  #相對的layout

        #設定widget
        header_label = LabelComponent(20, "Add Student")
        name_label = LabelComponent(16, "Name: ")
        subject_label = LabelComponent(16, "Subject: ")
        score_label = LabelComponent(16, "Score: ")
        self.label_hint = HintLabelComponent(15, "")

        self.edit_label_name = LineEditComponent("Name")
        self.edit_label_name.mousePressEvent = self.press_name_label_action
        
        self.edit_label_subject = LineEditComponent("Subject")
        self.edit_label_subject.mousePressEvent = self.press_subject_label_action

        self.edit_label_score = LineEditComponent()
        self.edit_label_score.mousePressEvent = self.press_score_label_action
        self.edit_label_score.setValidator(QtGui.QIntValidator(1, 100))  #限制只能輸入"int"，且範圍在"三位數內"

        #"button_query"的設定
        self.button_query = ButtonComponent("Query")
        self.button_query.clicked.connect(self.confirm_query)
        #"button_query"的設定

        #"button_add"的設定
        self.button_add = ButtonComponent("Add")
        self.button_add.clicked.connect(self.confirm_add)
        #"button_add"的設定
        
        #"button_send"的設定
        self.button_send = ButtonComponent("Send")
        self.button_send.clicked.connect(self.confirm_send)
        self.button_send.setEnabled(True)  #初始設定將btn不能按，但"button_send"要可以按，所以設定為"True"
        #"button_send"的設定

        #設定widget
        

        #layout widget
        layout.addWidget(header_label, 0, 0, 1, 2)  #設定在(row, col)然後占用多少(row, col)
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.label_hint, 0, 3, 4, 2)
        layout.addWidget(self.edit_label_name, 1, 1, 1, 1)
        layout.addWidget(self.edit_label_subject, 2, 1, 1, 1)
        layout.addWidget(self.edit_label_score, 3, 1, 1, 1)
        layout.addWidget(self.button_query, 1, 2, 1, 1)
        layout.addWidget(self.button_add, 3, 2, 1, 1)
        layout.addWidget(self.button_send, 6, 3, 1, 1)
        #layout widget

        #設定各別col所占的比例
        layout.setColumnStretch(0, 2)  
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 2)
        layout.setColumnStretch(3, 3.5)
        #設定各別col所占的比例

        #設定各別row所占的比例
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 2)
        layout.setRowStretch(5, 2)
        layout.setRowStretch(6, 2)
        #設定各別row所占的比例

        self.setLayout(layout)
    
    def load(self):
        print("add widget")
        self.init_action()

    def init_action(self):
        self.label_hint.setText("")
        self.edit_label_name.setText("Name")
        self.edit_label_subject.setText("Subject")
        self.edit_label_score.clear()
        self.button_query.setEnabled(False)
        self.button_add.setEnabled(False)
        self.button_send.setEnabled(False)

    def press_name_label_action(self, event):
        self.edit_label_name.clear()
        self.button_query.setEnabled(True)
        self.query_name = False
        self.button_add.setEnabled(False)
        
    def press_subject_label_action(self, event):
        self.edit_label_subject.clear()
        #print(self.edit_label_name.text())
        if not self.query_name : 
            self.label_hint.setText("Please query a new name first")

    def press_score_label_action(self, event):  
        self.edit_label_score.clear()
        if self.query_name : 
            self.button_add.setEnabled(True)
        else :
            self.label_hint.setText("Please query a new name first")


    def confirm_query(self) :

        if(self.edit_label_name.text() == "") :  #"name"如果是空字串就要再輸入一次
            self.label_hint.setText("Please enter name for student.")

        else :
            
            self.button_query.setEnabled(False)
            self.stu_list["name"] = self.edit_label_name.text()
            self.stu_list["scores"] = {}
            print("self.stu_list : {}".format(self.stu_list))
            self.query_name = True
            if(self.edit_label_subject.text() != "" and self.edit_label_score.text() != "") :
                self.button_add.setEnabled(True)
            
            
            self.execute_query = ExcuteCommand(command = "query", data = self.stu_list)
            self.execute_query.start()
            self.execute_query.return_sig.connect(self.query_action_result)  #將信號連接到指定槽函數
            # self.socket_client.send_command("query", self.stu_list)  #先"send_command"
            # stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
    
    def query_action_result(self, result):
        #"json.loads" : 將已編碼的JSON解碼為Python對象
        result = json.loads(result)

        if result["status"] == "OK" :
            self.label_hint.setText("The student '{}' already exists in DB".format(self.edit_label_name.text()))
            self.query_name = False

        else :
            self.label_hint.setText("Please enter subjects for student '{}'".format(self.edit_label_name.text()))
        

    def confirm_add(self) :
        #print(type(self.edit_label_subject.text()))
        #print(type(self.edit_label_score.text()))
        if(self.query_name == False) :  #先確認有沒有"query_name"
            self.label_hint.setText("Please query a new name first")

        elif(self.edit_label_subject.text() == "") :  #要先輸入"subject"
            self.label_hint.setText("Please input student's subject first.")

        elif(self.edit_label_score.text() == "") :  #再輸入"score"
            self.label_hint.setText("Please enter student's {} grade.".format(self.edit_label_subject.text()))

        else :
            print(self.stu_list)
            self.stu_list["scores"][self.edit_label_subject.text()] = self.edit_label_score.text()
            
            self.label_hint.setText("Student {}'s subject '{}' with score '{}' added"
            .format(self.edit_label_name.text(), self.edit_label_subject.text(), self.edit_label_score.text()))
            self.input_subject = True
        

    def confirm_send(self):
        if self.query_name and self.input_subject :
            self.label_hint.setText(str(self.stu_list))
            self.input_name = False
            self.input_subject = False
            self.edit_label_name.setText("Name")
            self.edit_label_subject.setText("Subject")
            self.edit_label_score.clear()
            self.button_add.setEnabled(False)


            #print(self.stu_list)
            self.execute_send = ExcuteCommand(command = "add", data = self.stu_list)
            self.execute_send.start()
            self.execute_send.return_sig.connect(self.send_action_result)  #將信號連接到指定槽函數
            
        else :
            self.label_hint.setText("Please input correct information.")

    def send_action_result(self, result):
        #"json.loads" : 將已編碼的JSON解碼為Python對象
        result = json.loads(result)

        if result["status"] == "OK" :
            self.label_hint.setText("Add {} successfully".format(self.stu_list))
            self.stu_list = {}  #"self.stu_list"給reset掉
            print("self.stu_list : {}".format(self.stu_list))

        else :
            self.label_hint.setText("Add {} unsuccessfully".format(self.stu_list))
        

            
            