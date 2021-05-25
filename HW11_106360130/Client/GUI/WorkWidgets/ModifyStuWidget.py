from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.WorkWidgetComponents import LabelComponent, LineEditComponent, ButtonComponent

import time


class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Modify Student")
        modify_widget = ModifyWidget()

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(modify_widget, stretch=8)
        self.setLayout(layout)
    
    def load(self):
        print("modify widget")


class ModifyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        #Name
        layout_name = QtWidgets.QGridLayout()
        self.screen_name = QtWidgets.QWidget()
        self.screen_name.setLayout(layout_name)

        label_name = LabelComponent(16, "Name: ")
        self.edit_label_name = LineEditComponent("Name")
        self.button_query = ButtonComponent("Query")

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
        self.edit_score_label = LineEditComponent("")

        self.combo_box_score = QtWidgets.QComboBox()
        self.combo_box_score.addItems(["Math", "English"])
        self.combo_box_score.currentIndexChanged.connect(self.combo_box_select_changed)

        layout_change.addWidget(self.radio_button_change, 0, 0, 1, 1)

        layout_change.addWidget(self.combo_box_score , 1, 0, 1, 1)
        layout_change.addWidget(self.edit_score_label, 1, 1, 1, 1)

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
        
        label_score = LabelComponent(16, "Score: ")
        self.edit_label_score = LineEditComponent("Score")

        layout_add.addWidget(self.radio_button_add, 0, 0, 1, 1)

        layout_add.addWidget(label_subject , 1, 0, 1, 2)
        layout_add.addWidget(self.edit_label_subject , 1, 1, 1, 1)

        layout_add.addWidget(label_score, 2, 0, 1, 2)
        layout_add.addWidget(self.edit_label_score, 2, 1, 1, 1)

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

        layout_confirm.addWidget(self.button_confirm, 0, 1, 1, 1)


        #設定各別row所占的比例
        layout_confirm.setRowStretch(0, 1)
        #設定各別row所占的比例

        #設定各別col所占的比例
        layout_confirm.setColumnStretch(0, 4)  
        layout_confirm.setColumnStretch(1, 1)
        #設定各別col所占的比例
        #Confirm
    

        self.radio_button_change.toggled.connect(self.radio_button_on_clicked)
        self.radio_button_add.toggled.connect(self.radio_button_on_clicked)


        """
        layout.addWidget(self.radio_button_change)
        layout.addWidget(self.radio_button_add)
        layout.addWidget(self.combo_box_score)
        """
        layout.addWidget(self.screen_name, stretch=1)
        layout.addWidget(self.screen_change, stretch=1)
        layout.addWidget(self.screen_add, stretch=1)
        layout.addWidget(self.screen_confirm, stretch=1)
       

        self.setLayout(layout)

    def radio_button_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            print("{}".format(selected_button.text()))


    def combo_box_select_changed(self, index):
        print ("Index {} {} selected".format(index, self.combo_box_score.currentText()))

