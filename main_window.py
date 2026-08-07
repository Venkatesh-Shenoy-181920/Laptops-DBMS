#=====================================================
#================LapDex HOME SCREEN===================
#=====================================================

# All imports
import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget,QTableWidgetItem, 
                             QHeaderView, QDialog)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QFont
import mysql.connector as m
import moreinfo
import app
import admin 
import reject
import credit
import edit_window
import confirm_delete

# Creating the connection object and the cursor object
con = m.connect(host = 'localhost',
                user = 'root',
                passwd = '192021',
                database = 'CS_Project',
                connection_timeout = 5)
cur = con.cursor()

# The home screen
class MainWindow(QMainWindow):
    def __init__(self, user_name):
        # Setting up everything
        super().__init__()
        self.user = user_name
        self.selected_laptop = None
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        icon_path = os.path.join(assets_dir, "retro.webp")

        # Window Conifguration
        self.setWindowTitle("Laptops Database")
        self.showFullScreen()
        self.setWindowIcon(QIcon(icon_path))

        # Initialising the Widgets for UI
        self.initUI()

    # UI element initialising function
    def initUI(self):
        # The main widget object
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout(central_widget)
        

        # Title Label
        self.title_label = QLabel("LapDex", self)
        self.title_label.setStyleSheet("color:white;"
                                       "font-size:30px;"
                                       "font-weight:bold;"
                                       "font-family:SF Pro Display;")
        
        # Textbox for entering the company name
        self.comp_name = QLineEdit()
        self.comp_name.setPlaceholderText("Company name")
        self.comp_name.setStyleSheet("color:black;"
                                     "background-color:white;"
                                     "font-size:20px;"
                                     "font-family:SF Pro Display;"
                                     "border:2px solid;"
                                     "border-color:#808080 ;"
                                     "border-radius:0px;")
        
        # Textbox for entering the release year
        self.rel_year = QLineEdit()
        self.rel_year.setPlaceholderText("Year of release")
        self.rel_year.setStyleSheet("color:black;"
                                    "background-color:white;"
                                    "font-size:20px;"
                                    "font-family:SF Pro Display;"
                                    "border:2px solid;"
                                    "border-color:#808080 ;"
                                    "border-radius:0px;")

        #The table widget
        self.table = QTableWidget()
        self.table.setMinimumWidth(750)
        self.table.itemClicked.connect(self.on_row_clicked)
        
        # Search button
        self.search = QPushButton("Search")
        self.search.setStyleSheet("color:white;"
                                  "background-color:Blue;"
                                  "font-weight:bold;"
                                  "font-family:SF Pro Display;"
                                  "font-size:20px;")
        self.search.clicked.connect(self.click)

        # Refresh button
        self.refresh = QPushButton("Refresh")
        self.refresh.setStyleSheet("color:white;"
                                   "background-color:blue;"
                                   "font-size:20px;"
                                   "font-family:SF Pro Display;"
                                   "font-weight:bold;")
        self.refresh.clicked.connect(self.reload)

        # More info button
        self.more = QPushButton("Info")
        self.more.setStyleSheet("color:white;"
                                "background-color:blue;"
                                "font-size:20px;"
                                "font-family:SF Pro Display;"
                                "font-weight:bold;")
        self.more.clicked.connect(self.more_info)

        # Allows the admin to add newer releases to the list
        self.add = QPushButton("Add")
        self.add.setFixedHeight(35)
        self.add.setFixedWidth(150)
        self.add.setStyleSheet("color:white;"
                               "background-color:blue;"
                               "font-weight:bold;"
                               "font-family:SF Pro Display;")
        self.add.clicked.connect(self.add_data)

        # Switch user
        self.user_switch = QPushButton("Switch User")
        self.user_switch.setFixedHeight(35)
        self.user_switch.setFixedWidth(150)
        self.user_switch.setStyleSheet("color:white;"
                                       "background-color:blue;"
                                       "font-weight:bold;"
                                       "font-family:SF Pro Display;")
        self.user_switch.clicked.connect(self.switch_user)

        # Credits button
        self.credit = QPushButton("Credits")
        self.credit.setFixedHeight(35)
        self.credit.setFixedWidth(150)
        self.credit.setStyleSheet("color:white;"
                                  "background-color:blue;"
                                  "font-weight:bold;"
                                  "font-family:SF Pro Display;")
        self.credit.clicked.connect(self.credit_window)

        # Edit for admin User
        self.Edit = QPushButton("Edit")
        self.Edit.setFixedHeight(35)
        self.Edit.setFixedWidth(150)
        self.Edit.setStyleSheet("color:white;"
                                "background-color:blue;"
                                "font-weight:bold;"
                                "font-family:SF Pro Display;")
        self.Edit.clicked.connect(self.edit_data)

        # The button to exit the program
        self.exit = QPushButton("Exit")
        self.exit.setFixedHeight(35)
        self.exit.setFixedWidth(150)
        self.exit.setStyleSheet("color:white;"
                                "background-color:red;"
                                "font-weight:bold;"
                                "font-family:SF Pro Display;")
        self.exit.clicked.connect(self.Exit)

        # Deleting the data about a computer
        self.Delete = QPushButton("Delete")
        self.Delete.setFixedHeight(35)
        self.Delete.setFixedWidth(150)
        self.Delete.setStyleSheet("color:white;"
                                  "background-color: red;"
                                  "font-weight:bold;"
                                  "font-family:SF Pro Display;")
        self.Delete.clicked.connect(self.delete)

        # The left panel where the data is shown
        self.left_panel = QWidget()
        self.left_layout = QVBoxLayout(self.left_panel)
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.comp_name)
        self.search_layout.addWidget(self.rel_year)
        self.search_layout.addWidget(self.search)
        self.search_layout.addWidget(self.more)
        self.search_layout.addWidget(self.refresh)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.user_switch)
        self.button_layout.addWidget(self.credit)

        # Admin only access buttons
        if self.user == "admin" or self.user == 'admin2':
            self.button_layout.addWidget(self.add)
            self.button_layout.addWidget(self.Edit)
            self.button_layout.addWidget(self.Delete)

        # Everyone buttons
        self.button_layout.addWidget(self.exit)

        self.left_layout.addWidget(self.title_label)
        self.left_layout.addLayout(self.search_layout)
        self.left_layout.addWidget(self.table)
        self.left_layout.addLayout(self.button_layout)

        # Right panel with WELCOME and Instructions
        self.right_panel = QWidget()
        self.right_panel.setMinimumWidth(350)
        self.right_panel.setStyleSheet("background-color: #252538;"
                                       "border-radius: 10px;"
                                       "padding: 20px;")
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(15, 65, 15, 20)

        self.welcome_title = QLabel("WELCOME 😊")
        self.welcome_title.setStyleSheet("color: white;"
                                         "font-size: 22px;"
                                         "font-weight:bold;"
                                         "font-family:SF Pro Display")
        self.welcome_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # The instructions
        instruction = (
            "'LapDex' is a program with which you can manage the database laptops which contains the details of all the laptops which where released in and after 2000\n\n"
            "💻 Select a laptop to view its details.\n\n"
            "💻 Use the search bar to filter.\n\n"
            "💻 Only admins can make changes to the data.\n\n"
            "💻 To see the credits press the credits button at the bottom\n\n"
            "💻 If any issues are encountered either restart the program or the lead developer\n\n"
        )

        # Displaying the WELCOME and Instructions on the panel
        self.welcome_text = QLabel(instruction)
        self.welcome_text.setStyleSheet("color: #CBD5E1;"
                                        "font-size: 16px;"
                                        "font-family:SF Pro Display")
        self.welcome_text.setWordWrap(True)
        self.welcome_text.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.right_layout.addWidget(self.welcome_title)
        self.right_layout.addSpacing(20)
        self.right_layout.addWidget(self.welcome_text)
        self.right_layout.addStretch()

        self.main_layout.addWidget(self.left_panel)
        self.main_layout.addWidget(self.right_panel)

        self.main_layout.setStretchFactor(self.left_panel, 85)
        self.main_layout.setStretchFactor(self.right_panel, 15)

    # The function that executes when the search is clicked
    def click(self):
        company = self.comp_name.text().strip()
        year = self.rel_year.text().strip()
        
        # Query based on the input given by the user
        if company == "" and year == "":
            query = "SELECT * FROM LAPTOPS ORDER BY YEAR DESC"
        elif company == "":
            query = "SELECT * FROM LAPTOPS WHERE YEAR = %s ORDER BY COMPANY" % year
        elif year == "":
            query = "SELECT * FROM LAPTOPS WHERE COMPANY = '%s' ORDER BY YEAR DESC" % company
        else:
            query = "SELECT * FROM LAPTOPS WHERE COMPANY = '%s' AND YEAR = %s ORDER BY COMPANY" % (company, year)
        
        # For the window display
        cur.execute(query)
        datas = cur.fetchall()
        self.display_data(datas)

        print("Debug data:")
        print(company)
        print(year)
        
        # Printing the data in the terminal
        for data in datas:
            print(data)

        
    # Function to display the table in the window
    def display_data(self, data):
        self.table.clearContents()
        self.table.setRowCount(0)

        if not data:
            return
        
        # Setting row and column counds 
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        # Setting the column headers and resizing the table to fit the window
        self.table.setHorizontalHeaderLabels(["Laptop", 'RAM', 'Storage', 'Company', 'Year','CPU', 'OS', 'Last OS', 'Price'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(0 ,QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setStyleSheet("font-family:Arial;"
                                                    "font-weight:bold;")
        cell_font = QFont("Arial", 10)

        # Using for loop to get the data to be displayed in the cells of the table
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setFont(cell_font)
                self.table.setItem(
                    row_idx, 
                    col_idx,
                    item
                )
    
    # To clear the table contents
    def reload(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        global con
        global cur

        con.close()
        con = m.connect(host = 'localhost',
                        user = 'root',
                        passwd = '192021',
                        database = 'CS_PROJECT',
                        connection_timeout = 5)
        
        cur = con.cursor()
        cur.execute('SELECT * FROM LAPTOPS ORDER BY YEAR DESC')
        data = cur.fetchall()
        self.display_data(data)

        print("Table was refreshed")
    
    # To get more information like higher models etc.
    def more_info(self):
        if not self.selected_laptop:
            print("No laptop selected")
            return

        query = 'SELECT * FROM LAPTOPS WHERE LAPTOP = "{}"'.format(self.selected_laptop,)
        cur.execute(query)
        laptop_record = cur.fetchone()
        print(self.selected_laptop)

        if laptop_record:
            self.info = moreinfo.more_info(laptop_record)
            self.info.show()
        else:
            self.no_data = reject.rejected()
            self.no_data.show()
        
        
    # Adding the data ONLY FOR ADMIN
    def add_data(self):
        if self.user == "admin":
            self.admin_add_data = admin.admin_add_data()
            self.admin_add_data.show()
        else:
            self.rejected = reject.rejected()
            self.rejected.show()
    
    # Switch user mid run
    def switch_user(self):
        self.login = app.LoginWindow()
        self.login.show()
        self.hide()

    # Edit data for admin only
    def edit_data(self):
        if self.user == "admin":
            self.edit = edit_window.edit()
            self.edit.show()
        else:
            self.rejected = reject.rejected()
            self.rejected.show()
        

    # Launch the credit window
    def credit_window(self):
        self.creditS = credit.credits()
        self.creditS.show()

    # Exist button
    def Exit(self):
        self.close()
        self.Credits = credit.credits()
        self.Credits.show()
        QTimer.singleShot(5000, self.Credits.close)
        con.close()

    # Selecting the laptop for anything
    def on_row_clicked(self, item):

        self.row = item.row()

        laptop_name = self.table.item(self.row, 0)
        if laptop_name:
            self.selected_laptop = laptop_name.text().strip()
            print(f"Selected laptops: {self.selected_laptop}")

    # Deleting the selected laptop by clicking on it and then delete button
    def delete(self):
        laptop_name = self.table.item(self.row, 0)

        self.confirm = confirm_delete.confirmed()
        self.confirm.show()
        
        state = self.confirm.proceed() # Gets the 1 that confirms the delete process
        print(state)

        if state == 1:
            try:
                # Getting the laptop name to be deleted
                self.selected_laptop = laptop_name.text().strip()

                    # Deleting and showing the delete success window
                query = "DELETE FROM LAPTOPS WHERE LAPTOP = '{}'".format(self.selected_laptop,)
                cur.execute(query)
                con.commit()

                self.confirm.close()
                self.deleted = reject.deleted(self.selected_laptop)
                self.deleted.show()

            except Exception as e:
                print(e)
                self.delete_fail = confirm_delete.delete_failed()
                self.delete_fail.show()