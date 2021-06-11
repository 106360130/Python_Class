from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent, HintLabelComponent

import time

from SocketClient.ServiceController import ExcuteCommand
import json

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Modify Student")
        self.modify_widget = ModifyWidget()

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.modify_widget, stretch=8)
        self.setLayout(layout)
    
    def load(self):
        print("modify widget")
        self.modify_widget.init_action()

class ModifyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")
        self.stu_list = {}
        self.stu_list["name"] = {}
        self.stu_list["scores"] = {}
        self.query_name = False

        self.modify_data = {}
        self.modify_data["stu_id"] = {}
        self.modify_data["scores_dict"] = {}

        layout = QtWidgets.QVBoxLayout()

        self.label_hint = HintLabelComponent(15, "")

        #Name
        layout_name = QtWidgets.QGridLayout()
        self.screen_name = QtWidgets.QWidget()
        self.screen_name.setLayout(layout_name)

        label_name = LabelComponent(16, "Name: ")

        self.edit_label_name = LineEditComponent("Name")
        self.edit_label_name.mousePressEvent = self.press_edit_label_name_action

        self.button_query = ButtonComponent("Query")
        self.button_query.clicked.connect(self.confirm_query)
        
        layout_name.addWidget(label_name, 0, 0, 1, 1)
        layout_name.addWidget(self.edit_label_name, 0, 1, 1, 1)
        layout_name.addWidget(self.button_query, 0, 2, 1, 1)


        #設定各別row所占的比例
        layout_name.setRowStretch(0, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        layout_name.setColumnStretch(0, 1)  
        layout_name.setColumnStretch(1, 2)
        layout_name.setColumnStretch(2, 1)
        #設定各別col所占的比例
        #Name


        #Change a current score
        layout_change = QtWidgets.QGridLayout()
        self.screen_change = QtWidgets.QWidget()
        self.screen_change.setLayout(layout_change)

        self.radio_button_change = QtWidgets.QRadioButton('Change a current score:')

        self.edit_label_score = LineEditComponent("")
        self.edit_label_score.mousePressEvent = self.press_edit_label_score_action

        self.combo_box_score = QtWidgets.QComboBox()
        self.combo_box_score.addItems(list())
        self.combo_box_score.currentIndexChanged.connect(self.combo_box_select_changed)

        layout_change.addWidget(self.radio_button_change, 0, 0, 1, 1)

        layout_change.addWidget(self.combo_box_score , 1, 0, 1, 1)
        layout_change.addWidget(self.edit_label_score, 1, 1, 1, 1)

        #設定各別row所占的比例
        layout_change.setRowStretch(0, 1)
        layout_change.setRowStretch(1, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        layout_change.setColumnStretch(0, 1)
        layout_change.setColumnStretch(1, 4)
        layout_change.setColumnStretch(2, 1)
        #設定各別col所占的比例

        
        #Change a current score
    

        #Add a new score
        layout_add = QtWidgets.QGridLayout()
        self.screen_add = QtWidgets.QWidget()
        self.screen_add.setLayout(layout_add)
        
        self.radio_button_add = QtWidgets.QRadioButton('Add a new score')
        label_subject = LabelComponent(16, "Subject: ")
        
        self.edit_label_subject = LineEditComponent("Subject")
        self.edit_label_subject.mousePressEvent = self.press_edit_label_subject_action
        
        label_score = LabelComponent(16, "Score: ")

        self.edit_label_score_2 = LineEditComponent("Score")
        self.edit_label_score_2.mousePressEvent = self.press_edit_label_score_2_action

        layout_add.addWidget(self.radio_button_add, 0, 0, 1, 1)

        layout_add.addWidget(label_subject , 1, 0, 1, 2)
        layout_add.addWidget(self.edit_label_subject , 1, 1, 1, 1)

        layout_add.addWidget(label_score, 2, 0, 1, 2)
        layout_add.addWidget(self.edit_label_score_2, 2, 1, 1, 1)

        #設定各別row所占的比例
        layout_add.setRowStretch(0, 1)
        layout_add.setRowStretch(1, 1)
        layout_add.setRowStretch(2, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        layout_add.setColumnStretch(0, 1)  
        layout_add.setColumnStretch(1, 4)
        layout_add.setColumnStretch(2, 1)
        #設定各別col所占的比例
        #Add a new score

        #Confirm
        layout_confirm = QtWidgets.QGridLayout()
        self.screen_confirm = QtWidgets.QWidget()
        self.screen_confirm.setLayout(layout_confirm)

        self.button_confirm = ButtonComponent("Confirm")
        self.button_confirm.clicked.connect(self.confirm_send)

        layout_confirm.addWidget(self.button_confirm, 0, 1, 1, 1)


        #設定各別row所占的比例
        layout_confirm.setRowStretch(0, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        layout_confirm.setColumnStretch(0, 4)  
        layout_confirm.setColumnStretch(1, 1)
        #設定各別col所占的比例
        #Confirm
    

        self.radio_button_change.toggled.connect(self.radio_button_change_on_clicked)
        self.radio_button_add.toggled.connect(self.radio_button_add_on_clicked)



        layout.addWidget(self.label_hint, stretch=1)
        layout.addWidget(self.screen_name, stretch=1)
        layout.addWidget(self.screen_change, stretch=1)
        layout.addWidget(self.screen_add, stretch=1)
        layout.addWidget(self.screen_confirm, stretch=1)
        

        self.setLayout(layout)
    
    def init_action(self):
        self.label_hint.setText("")
        self.edit_label_name.setText("Name")
        self.edit_label_subject.setText("Subject")
        self.edit_label_score.clear()
        self.edit_label_score_2.setText("Score")
        self.button_query.setEnabled(False)
        self.button_confirm.setEnabled(False)

    def radio_button_change_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            print("{}".format(selected_button.text()))
            self.radio_button_add.setChecked(False)  #將"radio_button_add"不要被選擇

    def radio_button_add_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            print("{}".format(selected_button.text()))
            self.radio_button_change.setChecked(False)  #將"radio_button_change"不要被選擇


    def combo_box_select_changed(self, index):
        print ("Index {} {} selected".format(index, self.combo_box_score.currentText()))
        



    def press_edit_label_name_action(self, event):
        self.edit_label_name.clear()
        self.button_query.setEnabled(True)
        self.query_name = False

    def press_edit_label_score_action(self, event):
        self.edit_label_score.clear()

        if self.query_name : 
            self.button_confirm.setEnabled(True)
            self.radio_button_change.setChecked(True)
        else :
            self.label_hint.setText("Please query a new name first")
        
    def press_edit_label_subject_action(self, event):
        self.edit_label_subject.clear()

        if self.query_name : 
            self.button_confirm.setEnabled(True)
            self.radio_button_add.setChecked(True)
        else :
            self.label_hint.setText("Please query a new name first")

    def press_edit_label_score_2_action(self, event):
        self.edit_label_score_2.clear()
        
        if self.query_name : 
            self.button_confirm.setEnabled(True)
            self.radio_button_add.setChecked(True)
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
            
            self.execute_query = ExcuteCommand(command = "query", data = self.stu_list)
            self.execute_query.start()
            self.execute_query.return_sig.connect(self.query_action_result)  #將信號連接到指定槽函數
            # self.socket_client.send_command("query", self.stu_list)  #先"send_command"
            # stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"

    def query_action_result(self, result):
        #"json.loads" : 將已編碼的JSON解碼為Python對象
        self.result = json.loads(result)

        if self.result["status"] == "OK" :
            self.combo_box_score.clear()  #先全部清除
            self.combo_box_score.addItems(list(self.result["scores"].keys()))  #再增加項目


            self.modify_data["stu_id"] = self.result['stu_id']
            self.modify_data["scores_dict"] = self.result['scores']
            self.label_hint.setText("The student '{}' exists in DB".format(self.edit_label_name.text()))
            self.query_name = True

        else :
            self.label_hint.setText("The name {} is not found".format(self.edit_label_name.text()))

    def confirm_send(self):
        
        if self.radio_button_change.isChecked():
            if self.edit_label_score.text() == "":
                self.label_hint.setText("Please enter the score")

            else:
                self.modify_data["scores_dict"][self.combo_box_score.currentText()] = self.edit_label_score.text()
                
                self.execute_confirm = ExcuteCommand(command = "modify", data = self.modify_data)
                self.execute_confirm.start()
                self.execute_confirm.return_sig.connect(self.confirm_action_result)  #將信號連接到指定槽函數

        elif self.radio_button_add.isChecked():
            if self.edit_label_subject.text() == "":
                self.label_hint.setText("Please enter the subject's name")

            elif self.edit_label_score_2.text() == "":
                self.label_hint.setText("Please enter the {}'s score".format(self.edit_label_subject.text()))

            else:
                self.modify_data["scores_dict"][self.edit_label_subject.text()] = self.edit_label_score_2.text()

                self.execute_confirm = ExcuteCommand(command = "modify", data = self.modify_data)
                self.execute_confirm.start()
                self.execute_confirm.return_sig.connect(self.confirm_action_result)  #將信號連接到指定槽函數

        
    

    def confirm_action_result(self, result):
        #"json.loads" : 將已編碼的JSON解碼為Python對象
        self.result = json.loads(result)
        
        if self.result["status"] == "OK" :
            if self.radio_button_change.isChecked():
                stu_info = [self.edit_label_name.text(), self.combo_box_score.currentText(), self.edit_label_score.text()]
                self.label_hint.setText("Modify {} success".format(stu_info))
            
            elif self.radio_button_add.isChecked():
                stu_info = [self.edit_label_name.text(), self.edit_label_subject.text(), self.edit_label_score_2.text()]
                self.label_hint.setText("Add {} success".format(stu_info))

            self.combo_box_score.clear()  #先全部清除
            self.combo_box_score.addItems(list(self.modify_data["scores_dict"].keys()))  #再增加項目


        

