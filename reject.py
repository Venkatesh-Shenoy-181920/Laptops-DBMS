# All imports
import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QLabel, QGridLayout, QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Shown when there is no data on the laptop "JUST IN CASE"
class rejected(QMainWindow):
    def __init__(self, laptop_name):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        icon_path = os.path.join(assets_dir, "access-denied.jpg")
        self.setWindowTitle("Access Denied")
        self.setGeometry(100, 100, 400, 150)
        self.setWindowIcon(QIcon(icon_path))
        self.message(laptop_name)

    def message(self, laptop_name):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        self.no_data = QLabel(f"No data on the Laptop \n {laptop_name}", self)
        self.no_data.setStyleSheet("color:white;"
                                           "font-family: SF Pro Display;"
                                           "font-size: 20px;"
                                           "font-weight:bold;")
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet("color:white;"
                                     "background-color:blue;"
                                     "font-family:SF Pro Display;"
                                     "font-weight:bold;")
        self.ok_button.clicked.connect(self.Close)

        self.grid.addWidget(self.no_data, 0, 0, 1, 4, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.ok_button, 1, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

    def Close(self):
        self.close()

# Shown when data is deleted succcessfully
class deleted(QMainWindow):
    def __init__(self, laptop_name):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        icon_path = os.path.join(assets_dir, "done.jpg")
        self.setWindowTitle("Data Deletion Complete")
        self.setGeometry(100, 100, 400, 150)
        self.setWindowIcon(QIcon(icon_path))
        self.message(laptop_name)

    def message(self, laptop_name):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        self.no_data = QLabel(f"All data related to the laptop: \n {laptop_name} has been deleted", self)
        self.no_data.setStyleSheet("color:white;"
                                   "font-family: SF Pro Display;"
                                   "font-size: 20px;"
                                   "font-weight:bold;")
        self.no_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet("color:white;"
                                     "background-color:blue;"
                                     "font-family:SF Pro Display;"
                                     "font-weight:bold;")
        self.ok_button.clicked.connect(self.Close)

        self.grid.addWidget(self.no_data, 0, 0, 1, 4, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.ok_button, 1, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

    # To show that access has been denied
    def Close(self):
        self.close()