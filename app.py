# All imports
import os
import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QGridLayout, QLineEdit, 
                              QFormLayout,QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import main_window
import json
from styles import style

# Login page
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        key_path = os.path.join(assets_dir, "key_edit.jpg")
        bg_path = os.path.join(assets_dir, "bg.jpg")
        Image_path = os.path.join(assets_dir, "images.jpg")

        # Window Config
        self.setWindowTitle("LOGIN")
        self.setGeometry(400, 200, 500, 500)
        self.setWindowIcon(QIcon(key_path))

        self.initLogin(bg_path, Image_path)
        self.users = self.load_users()
    
    # Fetch user credentials
    def load_users(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        creds_path = os.path.join(current_dir, "credentials.json")
        
        if os.path.exists(creds_path):
            with open(creds_path, "r") as f:
                return json.load(f)
        return{}
    
    # Login Page UI initialising
    def initLogin(self, bg_path, image_path):
        central = QWidget() # Central Widget and mainlayout
        self.setCentralWidget(central)
        self.mainLayout = QHBoxLayout()
        central.setLayout(self.mainLayout)
        
        # Image on login page
        image_label = QLabel()
        pixmap = QPixmap(bg_path)
        image_label.setPixmap(pixmap.scaled(300, 400,
                                             Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                             Qt.TransformationMode.SmoothTransformation))
        image_label.setScaledContents(True)        
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # The user image
        image_label2 = QLabel()
        pixmap = QPixmap(image_path)
        image_label2.setPixmap(pixmap.scaled(300, 400, Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                             Qt.TransformationMode.SmoothTransformation ))
        image_label2.setScaledContents(False)
        image_label2.setAlignment(Qt.AlignmentFlag.AlignRight)

        # RHS 
        form_container = QGroupBox("Login")
        form_layout = QFormLayout()
        form_container.setLayout(form_layout)
        
        # Username
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet("color:black;"
                               "background-color:white;"
                               "font-family:Google Sans;")

        # Password
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setStyleSheet("color:black;"
                               "background-color:white;"
                               "font-family:Google Sans;")
        
        # Sign in button
        self.sign_in = QPushButton("Sign In") 
        self.sign_in.setFixedSize(100, 30)
        self.sign_in.setStyleSheet("color:white;"
                                   "background-color:blue;" 
                                   "font-weight:bold;"
                                   "font-family:Google Sans;")
        self.sign_in.clicked.connect(self.log_in)

        # Sign up button updates the credentials.json file
        self.sign_up = QPushButton("Sign Up")
        self.sign_up.setFixedSize(100, 30)
        self.sign_up.setStyleSheet("color:white;"
                                   "background-color:blue;"
                                   "font-weight:bold;"
                                   "font-family:Google Sans;")
        self.sign_up.clicked.connect(self.create_user)

        # Username, Password button layout on login page
        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(self.sign_in)
        button_row.addWidget(self.sign_up)
        button_row.addStretch()

        form_layout.addRow("Username: ", self.username)
        form_layout.addRow("Password: ", self.password)
        form_layout.addRow(button_row)

        # Setting the widgets on the window
        right_wrapper = QWidget()
        right_layout = QVBoxLayout()
        right_wrapper.setLayout(right_layout)
        right_layout.addStretch()
        right_layout.addWidget(form_container)
        right_layout.addStretch()

        self.mainLayout.addWidget(image_label, stretch = 2)
        self.mainLayout.addWidget(right_wrapper, stretch = 1)

     # Credential checker
    def log_in(self):
        user_name = self.username.text().strip()
        pass_word = self.password.text().strip()
        self.user = user_name
        print(user_name)
        print(pass_word)
        if user_name in self.users:
            if pass_word == self.users[user_name]:
                self.main_Window = main_window.MainWindow(user_name)
                self.main_Window.show()
                self.close()
            elif pass_word != self.users[user_name]:
                self.wrong_pass = wrong_passwd(user_name)
                self.wrong_pass.show()
                print("Wrong Password")
        else:
            print("Invalid Username")
            self.wrong = no_user(user_name)
            self.wrong.show()

    # Signing a user up
    def create_user(self):
        global user_name
        user_name = self.username.text().strip()
        pass_word = self.password.text().strip()

        if user_name == "" or pass_word == "":
            self.close()
        
        if user_name in self.users:
            self.log_in(self)
        self.users[user_name] = pass_word

        current_dir = os.path.dirname(os.path.abspath(__file__))
        cred_path = os.path.join(current_dir, "credentials.json")

        with open(cred_path, 'w') as f:
            json.dump(self.users, f, indent = 2)
            print(f"New user {user_name} added successfully")

class no_user(QMainWindow):
    def __init__(self, name):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        asset = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(asset, "Failed")

        self.setWindowTitle("No User")
        self.setWindowIcon(QIcon(icon))
        self.setFixedSize(350, 150)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)
        
        self.text = QLabel(f"❌ No user named:\n\t{name}")
        self.text.setStyleSheet("font-size:22px;"
                                "font-weight:bold;")

        self.grid.addWidget(self.text, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        
class wrong_passwd(QMainWindow):
    def __init__(self, name):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        asset = os.path.join(current_dir, "Icon Images")
        icon = os.path.join(asset, "Failed")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        self.setWindowTitle("Wrong Passord")
        self.setWindowIcon(QIcon(icon))
        self.setFixedSize(350, 150)

        self.text = QLabel(f"❌ Wrong password for user:\n\t{name}")
        self.text.setStyleSheet("font-size:22px;"
                                "font-weight:bold;")
        self.grid.addWidget(self.text, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

# Function to start the window
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()