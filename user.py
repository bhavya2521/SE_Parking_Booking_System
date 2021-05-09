from PyQt5.QtWidgets import QWidget,QMainWindow,QPushButton,QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QFrame,QGridLayout,QComboBox,QTableWidget,QTableWidgetItem
from DataBaseOperation import DBOperation
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QLabel,QMessageBox
from PyQt5 import QtGui
from datetime import datetime


class User(QMainWindow):
    name=""
    def __init__(self,str):
        self.name=str

        super().__init__()
        self.setWindowTitle("User")
        self.dbOperation=DBOperation()
        widget=QWidget()
        widget.setStyleSheet("background:rgb(0, 0, 0)")
        layout_horizontal=QHBoxLayout()
        menu_vertical_layout=QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.btn_home=QPushButton("Home")
        self.btn_add = QPushButton("Make a Booking")
        self.btn_manage = QPushButton("Manage Bookings")
        self.btn_history = QPushButton("Bookings History")
        self.btn_logout = QPushButton("Log Out")

        menu_vertical_layout.setContentsMargins(0,0,0,0)
        menu_vertical_layout.setSpacing(0)
        self.btn_home.setStyleSheet("width:200px;height:100px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")

        self.btn_add.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_logout.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")

        self.connect = self.btn_manage.clicked.connect(self.showManage)
        self.btn_add.clicked.connect(self.showAdd)
        self.btn_history.clicked.connect(self.showHistory)
        self.btn_logout.clicked.connect(self.showLogout)

        menu_frame=QFrame()
        menu_vertical_layout.addWidget(self.btn_add)
        menu_vertical_layout.addWidget(self.btn_manage)
        menu_vertical_layout.addWidget(self.btn_history)
        menu_vertical_layout.addWidget(self.btn_logout)

        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        #menu_frame.setMinimumWidth(200)
        #menu_frame.setMaximumHeight(200)




        parent_vertical=QVBoxLayout()
        parent_vertical.setContentsMargins(0,0,0,0)
        self.vertical_1=QVBoxLayout()
        self.addHomePageData()


        self.vertical_2=QVBoxLayout()
        self.vertical_2.setContentsMargins(0,0,0,0)
        self.addBookingPage()

        self.vertical_3=QVBoxLayout()
        self.vertical_3.setContentsMargins(0,0,0,0)
        self.addManagePage()

        self.vertical_4=QVBoxLayout()
        self.addHistoryPage()


        #CHECK
        self.frame_1=QFrame()
        self.frame_1.setMinimumWidth(self.width())
        self.frame_1.setMaximumWidth(self.width())
        self.frame_1.setMaximumHeight(self.width())
        self.frame_1.setMaximumHeight(self.width())

        self.frame_1.setLayout(self.vertical_1)
        self.frame_2=QFrame()
        self.frame_2.setLayout(self.vertical_2)
        self.frame_3=QFrame()
        self.frame_3.setLayout(self.vertical_3)
        self.frame_4=QFrame()
        self.frame_4.setLayout(self.vertical_4)


        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)




        layout_horizontal.addWidget(menu_frame)
        layout_horizontal.addLayout(parent_vertical)
        layout_horizontal.setContentsMargins(0,0,0,0)
        parent_vertical.setContentsMargins(0,0,0,0)
        parent_vertical.addStretch()
        #menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()
        widget.setLayout(layout_horizontal)

        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()

        self.setCentralWidget(widget)

    def showHistory(self):
        self.btn_home.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:100px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_logout.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()

    def showManage(self):
        self.btn_home.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:100px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_logout.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_4.hide()
        self.frame_3.show()

    def showAdd(self):
        self.btn_home.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:100px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_logout.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.frame_1.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_2.show()

    def showHome(self):
        self.btn_home.setStyleSheet("width:200px;height:100px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_logout.setStyleSheet("width:200px;height:100px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_1.show()






    def showLogout(self):
        self.close()

    def refreshHome(self):
        #TODO
        pass


    def addHomePageData(self):
        #TODO
        pass




    def addBookingPage(self):
        layout=QVBoxLayout()
        frame=QFrame()

        vechicle_label=QLabel("Vehicle No : ")
        vechicle_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vechicle_type=QLabel("Vehicle Type : ")
        vechicle_type.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        wait_label = QLabel("Wait Time: ")
        wait_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")

        error_label=QLabel("")
        error_label.setStyleSheet("color:red;padding:8px 0px;font-size:20px")


        vehicle_input=QLineEdit()
        vehicle_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;border:1px solid white")
        wait_input = QComboBox()
        wait_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;border:1px solid white")
        t=[1,10,20,30,40,50,60,90,120]
        for i in t:
            wait_input.addItem(str(i)+"min")
        vtype=QComboBox()
        vtype.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;border:1px solid white")
        vtype.addItem("2 Wheeler")
        vtype.addItem("4 Wheeler")

        button=QPushButton("Book slot")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")


        layout.addWidget(vechicle_label)
        layout.addWidget(vehicle_input)
        layout.addWidget(vechicle_type)
        layout.addWidget(vtype)
        layout.addWidget(wait_label)
        layout.addWidget(wait_input)




        layout.addWidget(button)
        layout.addWidget(error_label)

        layout.setContentsMargins(0,0,0,0)
        frame.setMinimumHeight(self.height())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.width())
        frame.setMaximumWidth(self.width())

        layout.addStretch()
        frame.setLayout(layout)
        button.clicked.connect(lambda:self.book(self.name,vehicle_input.text(),vtype.currentIndex(),error_label,vehicle_input,wait_input.currentIndex()))
        self.vertical_2.addWidget(frame)


    def check_vehicle(self,vehicleno):
        data = self.dbOperation.getCurrentbookings()
        for i in data:
            if(i[6]==vehicleno):
                return True
        return False





    def book(self,name,vehicleno,index,error_label,vehicle_input,wait_input):
        error_label.setText("")
        if (vehicleno == ""):
            error_label.setText("Enter Vehicle No")
            return
        if(self.check_vehicle(vehicleno)):
            error_label.setText("Booking is already made for this vehicle")
            return

        if index==0:
            vtp="2W"
        else:
            vtp="4W"
        t=[1,10,20,30,40,50,60,90,120]
        wait=t[wait_input]


        data=self.dbOperation.book(name,vehicleno,vtp,wait)
        if data==True:
            QMessageBox.about(self, "Hurray!!", "Booking Successful")
            vehicle_input.setText("")

        elif data==False:
            QMessageBox.about(self, "Oops :(", "Booking Failed, Try Again!")
        else:
            error_label.setText(str(data))

    def addManagePage(self):

        data= self.dbOperation.getUserCurrentbookings(self.name)
        self.table=QTableWidget()
        self.table.setStyleSheet("background:#fff")
        self.table.resize(self.width(),self.height())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(8)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("VehicleNo"))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("Slot"))
        self.table.setHorizontalHeaderItem(4,QTableWidgetItem("Type"))
        self.table.setHorizontalHeaderItem(5,QTableWidgetItem("Wait"))
        self.table.setHorizontalHeaderItem(6,QTableWidgetItem("Check-In"))
        self.table.setHorizontalHeaderItem(7,QTableWidgetItem("Cancel"))

        #name,slot,entry_time,exit_time,is_exit,vehicle_no,vehicle_type,book_time, wait

        #1,6,2,7,9,3


        loop=0
        current = datetime.now().strftime("%d-%m %H:%M")


        for smalldata in data:
            self.table.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop,5,QTableWidgetItem(str(smalldata[9])+"min"))
            self.table.setItem(loop,6, QTableWidgetItem(str(smalldata[3])))



            self.button_cancel = QPushButton("Cancel")


            self.button_cancel.setStyleSheet("color:#fff;padding:0px 0px;font-size:15px;background:green;border:1px solid white")


            self.table.setCellWidget(loop, 9, self.button_cancel)


            id = (str(smalldata[0]))
            self.button_cancel.clicked.connect(self.CancelCall)
            loop=loop+1

        frame=QFrame()
        #self.table.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
        layout=QVBoxLayout()
        button=QPushButton("Current Bookings")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshManage)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(button)
        layout.addWidget(self.table)
        frame.setLayout(layout)
        frame.setContentsMargins(0,0,0,0)
        frame.setMaximumWidth(self.width())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.height())
        frame.setMinimumHeight(self.height())
        self.vertical_3.addWidget(frame)
        self.vertical_3.addStretch()


    def refreshManage(self):
        data= self.dbOperation.getUserCurrentbookings(self.name)
        self.table.setRowCount(len(data))
        self.table.setColumnCount(8)
        loop=0
        current = datetime.now().strftime("%d-%m %H:%M")
        self.time_out()


        for smalldata in data:
            checked = 0
            print(str(smalldata))
            self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[9])+"min"))
            self.table.setItem(loop, 6, QTableWidgetItem(str(smalldata[3])))


            self.button_cancel = QPushButton("Cancel")
            self.button_cancel.setStyleSheet("color:#fff;padding:0px 0px;font-size:15px;background:green;border:1px solid white")
            self.table.setCellWidget(loop, 7, self.button_cancel)
            self.button_cancel.clicked.connect(self.CancelCall)
            loop=loop+1




    def CancelCall(self):
        btton=self.sender()
        if btton:
            row=self.table.indexAt(btton.pos()).row()
            id =str(self.table.item(row,0).text())
            self.dbOperation.CancelCall(id,"Cancel")
            self.table.removeRow(row)

    def time_out(self):
        data = self.dbOperation.getCurrentbookings()
        current = datetime.now().strftime("%d-%m %H:%M")
        time=list(current.split())[1]
        hrs=list(map(int,time.split(":")))
        min1=hrs[0]*60 + hrs[1]


        for smalldata in data:
            if(smalldata[3]==""):
                current=smalldata[8]
                time = list(current.split())[1]
                hrs = list(map(int, time.split(":")))
                min2 = hrs[0] * 60 + hrs[1]
                d=min1-min2
                if(d>int(smalldata[9])):
                    self.dbOperation.CancelCall(str(smalldata[0]), "Time-out")
                    self.refreshManage()



    def addUserPage(self):
        pass

    def refreshHistory(self):
        self.table1.clearContents()
        id=1

        data= self.dbOperation.getUserbookings(self.name)
        loop=0
        self.table1.setRowCount(len(data))
        self.table1.setColumnCount(7)
        for smalldata in data:
            self.table1.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop,6,QTableWidgetItem(str(smalldata[4])))
            loop=loop+1

    def addHistoryPage(self):
        id=1

        data= self.dbOperation.getUserbookings(self.name)
        self.table1=QTableWidget()
        self.table1.resize(self.width(),self.height())
        self.table1.setRowCount(len(data))
        self.table1.setStyleSheet("background:#fff")
        self.table1.setColumnCount(7)

        button=QPushButton("Past Bookings")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshHistory)


        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table1.setHorizontalHeaderItem(0,QTableWidgetItem("ID"))
        self.table1.setHorizontalHeaderItem(1,QTableWidgetItem("Name"))
        self.table1.setHorizontalHeaderItem(2,QTableWidgetItem("VEHICLE No"))
        self.table1.setHorizontalHeaderItem(3,QTableWidgetItem("SLOT"))
        self.table1.setHorizontalHeaderItem(4,QTableWidgetItem("TYPE"))
        self.table1.setHorizontalHeaderItem(5,QTableWidgetItem("ENTRY TIME"))
        self.table1.setHorizontalHeaderItem(6,QTableWidgetItem("EXIT TIME"))

        loop=0
        for smalldata in data:
            self.table1.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop,6,QTableWidgetItem(str(smalldata[4])))
            loop=loop+1

        self.frame5=QFrame()
        self.layout1=QVBoxLayout()
        self.layout1.setContentsMargins(0,0,0,0)
        self.layout1.setSpacing(0)
        self.layout1.addWidget(button)
        self.layout1.addWidget(self.table1)
        self.frame5.setLayout(self.layout1)
        self.frame5.setContentsMargins(0,0,0,0)
        self.frame5.setMaximumWidth(self.width())
        self.frame5.setMinimumWidth(self.width())
        self.frame5.setMaximumHeight(self.height())
        self.frame5.setMinimumHeight(self.height())
        self.vertical_4.addWidget(self.frame5)
        self.vertical_4.addStretch()



