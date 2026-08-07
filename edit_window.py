# All imports
import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import mysql.connector as m
from admin import added, failed

# Connecting to the database
con = m.connect(host = 'localhost',
                user = 'root',
                passwd = '192021',
                database = 'CS_PROJECT',
                connection_timeout = 5)

cur = con.cursor()

# Window to edit data on laptops
class edit(QMainWindow):
    def __init__(self):
        super().__init__()
        # Getting the path for icons
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        icon_path = os.path.join(assets_dir, "images.jpg")

        # Setting the window geometry and icon
        self.setWindowTitle("Edit Data")
        self.setFixedSize(400, 200)
        self.setWindowIcon(QIcon(icon_path))

        #Initialising the UI elements
        self.initUI()

    # Function for initialising the UI elements 
    def initUI(self):
        # Defining the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        # The title and the line edits to access the user input
        self.title = QLabel("EDIT DATABASE")
        self.title.setStyleSheet("font-size: 20px;"
                                 "font-weight:bold;"
                                 "font-family:SF Pro Display;")

        self.laptop_name = QLineEdit()
        self.laptop_name.setFixedSize(350, 30)
        self.laptop_name.setPlaceholderText("Laptop name")
        self.laptop_name.setStyleSheet("color:black;"
                                       "background-color:white;"
                                       "font-size:20px;"
                                       "font-family:SF Pro Display;"
                                       "border:2px solid;"
                                       "border-color:#808080 ;"
                                       "border-radius:0px;")
        
        self.change_value_of = QLineEdit()
        self.change_value_of.setFixedSize(350, 30)
        self.change_value_of.setPlaceholderText("Which item do you wish to change?")
        self.change_value_of.setStyleSheet("color:black;"
                                            "background-color:white;"
                                            "font-size:20px;"
                                            "font-family:SF Pro Display;"
                                            "border:2px solid;"
                                            "border-color:#808080 ;"
                                            "border-radius:0px;")

        self.new_value = QLineEdit()
        self.new_value.setFixedSize(350, 30)
        self.new_value.setPlaceholderText("Enter the new value")
        self.new_value.setStyleSheet("color:black;"
                                            "background-color:white;"
                                            "font-size:20px;"
                                            "font-family:SF Pro Display;"
                                            "border:2px solid;"
                                            "border-color:#808080 ;"
                                            "border-radius:0px;")

        self.enter = QPushButton("COMMIT CHANGES")
        self.enter.setStyleSheet("color:white;"
                           "background-color:blue;"
                           "font-weight:bold;"
                           "font-family:SF Pro Display;"
                           "font-size:15px;")
        self.enter.clicked.connect(self.submit)

        # Adding the elements to the central widget
        self.grid.addWidget(self.title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.laptop_name, 1, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.change_value_of, 2, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.new_value, 3, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)
        self.grid.addWidget(self.enter, 4, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

    # Function to submit the changes
    def submit(self):            
            try:
                laptop = self.laptop_name.text().strip()
                change_value_of = self.change_value_of.text().strip().upper()

                if change_value_of == "YEAR":
                    new_value = int(self.new_value.text().strip())
                    query = """
                    UPDATE LAPTOPS 
                    SET YEAR = {}
                    WHERE LAPTOP = '{}'
                    """.format(new_value, laptop)
                elif change_value_of == "PRICE":
                    new_value = int(self.new_value.text().strip())
                    query = """
                        UPDATE LAPTOPS 
                        SET PRICE = {}
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                elif change_value_of == "LAPTOP":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET LAPTOP = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                elif change_value_of == "LAST OS":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET LAST_OS = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)                
                elif change_value_of == "RAM":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET RAM = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                elif change_value_of == "CPU":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET CPU = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                elif change_value_of == "STORAGE":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET STORAGE = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                elif change_value_of == "OS":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET OS = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                elif change_value_of == "COMPANY":
                    new_value = self.new_value.text().strip()
                    query = """
                        UPDATE LAPTOPS 
                        SET COMPANY = '{}'
                        WHERE LAPTOP = '{}'
                        """.format(new_value, laptop)
                else:
                    self.close()
                cur.execute(query)
                con.commit()

                self.done = added()
                self.done.show()

            except Exception as e:
                print(e)
                self.fail = failed()
                self.fail.show()