# All imports
import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import mysql.connector as m

# Connecting to the database
con = m.connect(host = 'localhost',
                user = '<username>',
                passwd = '<password>',
                database = 'CS_Project')
cur = con.cursor()

# This window appears when the data addition is successful
class added(QMainWindow):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(assets, "done.jpg")

        self.setWindowTitle("Data Addition Success")
        self.setFixedSize(350, 150)
        self.setWindowIcon(QIcon(icon))

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        self.done = QLabel("Data added to the database successfully!", self)
        
        self.ok = QPushButton("OK")
        self.ok.setStyleSheet("color:white;"
                           "background-color:blue;"
                           "font-weight:bold;"
                           "font-family:SF Pro Display;"
                           "font-size:15px;")
        self.ok.clicked.connect(self.Close)

        self.grid.addWidget(self.done, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.ok, 1, 0, 1, 3, Qt.AlignmentFlag.AlignRight)

    def Close(self):
        self.close()

# This is shown when the data addition fails
class failed(QMainWindow):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(assets, "access-denied.jpg")

        self.setWindowTitle("Data Addition Failed")
        self.setFixedSize(350, 150)
        self.setWindowIcon(QIcon(icon))

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        self.fail = QLabel("Data addition to databases unsuccessful", self)
        
        self.ok = QPushButton("OK")
        self.ok.setStyleSheet("color:white;"
                           "background-color:blue;"
                           "font-weight:bold;"
                           "font-family:SF Pro Display;"
                           "font-size:15px;")
        self.ok.clicked.connect(self.Close)

        self.grid.addWidget(self.fail, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.ok, 1, 0, 1, 3, Qt.AlignmentFlag.AlignRight)
    def Close(self):
        self.close()

# When admin is adding the data to the database
class admin_add_data(QMainWindow):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(assets, "images.jpg")
        self.setWindowTitle("Add Data")
        self.setFixedSize(400, 200)
        self.setWindowIcon(QIcon(icon))
        
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        # Line edits to get the required data
        self.laptop_name = QLineEdit()
        self.laptop_name.setPlaceholderText("Laptop Name or Model")
        self.laptop_name.setStyleSheet("color:black;"
                               "background-color:white;"
                               "font-weight:bold;"
                               "font-family:SF Pro Display;")
        
        self.RAM = QLineEdit()
        self.RAM.setPlaceholderText("RAM")
        self.RAM.setStyleSheet("color:black;"
                               "background-color:white;"
                               "font-weight:bold;"
                               "font-family:SF Pro Display;")
        
        self.storage = QLineEdit()
        self.storage.setPlaceholderText("Storage")
        self.storage.setStyleSheet("color:black;"
                                   "background-color:white;"
                                   "font-weight:bold;"
                                   "font-family:SF Pro Display;")
        
        self.comp = QLineEdit()
        self.comp.setPlaceholderText("Company")
        self.comp.setStyleSheet("color:black;"
                                "background-color:white;"
                                "font-weight:bold;"
                                "font-family:SF Pro Display;")
        
        self.year = QLineEdit()
        self.year.setPlaceholderText("Year")
        self.year.setStyleSheet("color:black;"
                                "background-color:white;"
                                "font-weight:bold;"
                                "font-family:SF Pro Display;")
        
        self.cpu = QLineEdit()
        self.cpu.setPlaceholderText("CPU")
        self.cpu.setStyleSheet("color:black;"
                               "background-color:white;"
                               "font-weight:bold;"
                               "font-family:SF Pro Display;")
        
        self.ship_os = QLineEdit()
        self.ship_os.setPlaceholderText("Shipped OS")
        self.ship_os.setStyleSheet("color:black;"
                                   "background-color:white;"
                                   "font-weight:bold;"
                                   "font-family:SF Pro Display;")
        
        self.sup_os = QLineEdit()
        self.sup_os.setPlaceholderText("Last Supported OS")
        self.sup_os.setStyleSheet("color:black;"
                                  "background-color:white;"
                                  "font-weight:bold;"
                                  "font-family:SF Pro Display;")
        
        self.price = QLineEdit()
        self.price.setPlaceholderText("Price")
        self.price.setStyleSheet("color:black;"
                                  "background-color:white;"
                                  "font-weight:bold;"
                                  "font-family:SF Pro Display;")
        

        self.enter = QPushButton("SUBMIT")
        self.enter.setStyleSheet("color:white;"
                           "background-color:blue;"
                           "font-weight:bold;"
                           "font-family:SF Pro Display;"
                           "font-size:15px;")
        self.enter.clicked.connect(self.submit)

        # Adding the elements to the window
        self.grid.addWidget(self.laptop_name, 0, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.RAM, 0, 0, 1, 3, Qt.AlignmentFlag.AlignRight)
        self.grid.addWidget(self.storage, 1, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.comp, 1, 0, 1, 3, Qt.AlignmentFlag.AlignRight)
        self.grid.addWidget(self.year, 2, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.cpu, 2, 0, 1, 3, Qt.AlignmentFlag.AlignRight)
        self.grid.addWidget(self.ship_os, 3, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.sup_os, 3, 0, 1, 3, Qt.AlignmentFlag.AlignRight)
        self.grid.addWidget(self.price, 4, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.enter, 4, 0, 1, 3, Qt.AlignmentFlag.AlignRight)

    # The data from the text is added to the database
    def submit(self):
        try:
            laptop = self.laptop_name.text().strip()
            RAM = self.RAM.text().strip()
            storage = self.storage.text().strip()
            comp = self.comp.text().strip()
            year = int(self.year.text().strip())
            CPU = self.cpu.text().strip()
            shipped_os = self.ship_os.text().strip()
            sup_os = self.sup_os.text().strip()
            price = int(self.price.text().strip())
            
            query = """INSERT INTO LAPTOPS 
            VALUES ('{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', {})""".format(laptop, RAM, storage, comp, year, CPU, shipped_os, sup_os, price)
            
            cur.execute(query)
            con.commit()

            self.added = added()
            self.added.show()
            
        except:
            self.failed = failed()
            self.failed.show()
