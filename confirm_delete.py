# All imports
import os
from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Getting confirmation from the user to delete the data
class confirmed(QDialog):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(assets, "question_mark.jpg")   # Change if your icon has another name

        self.setWindowTitle("Confirm Delete")
        self.setWindowIcon(QIcon(icon))
        self.setFixedSize(350, 150)

        self.initUI()

    def initUI(self):
        central = QWidget()
        self.setLayout(QGridLayout())

        self.label = QLabel("Are you sure you want to delete this laptop?")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.yes = QPushButton("YES")
        self.yes.setStyleSheet("color:white;"
                               "background-color:blue;"
                               "font-family:SF Pro Display;"
                               "font-weight:bold;")
        
        self.no = QPushButton("NO")
        self.no.setStyleSheet("color:white;"
                              "background-color:blue;"
                              "font-family:SF Pro Display;"
                              "font-weight:bold;")

        self.layout().addWidget(self.label, 0, 0, 1, 2)
        self.layout().addWidget(self.yes, 1, 0)
        self.layout().addWidget(self.no, 1, 1)

        self.yes.clicked.connect(self.accept)
        self.no.clicked.connect(self.reject)

    def proceed(self):
        if self.exec():
            return 1
        return 0

# Incase the data delete fails
class delete_failed(QDialog):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(assets, "access_denied.jpg")   # Change if your icon has another name

        self.setWindowTitle("Confirm Delete")
        self.setWindowIcon(QIcon(icon))
        self.setFixedSize(350, 150)

        self.initUI()

    def initUI(self):
        central = QWidget()
        self.setLayout(QGridLayout())

        self.label = QLabel("Are you sure you want to delete this laptop?")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.yes = QPushButton("OK")
        self.yes.setFixedSize(400, 35)
        self.yes.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.layout().addWidget(self.label, 0, 0, 1, 2)
        self.layout().addWidget(self.yes, 1, 0)

        self.yes.clicked.connect(self.closed)
        
    def closed(self): 
        self.close()