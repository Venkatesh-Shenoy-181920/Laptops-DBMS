# All imports
import os
from PyQt6.QtWidgets import (QLabel, QHBoxLayout, QVBoxLayout, QDialog)
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QIcon, QPainter, QPixmap, QPainterPath

# To round of the image corners
def round(pixmap: QPixmap, radius: int = 20) -> QPixmap:
    rounded = QPixmap(pixmap.size())
    rounded.fill(Qt.GlobalColor.transparent)

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    path = QPainterPath()
    rect = QRectF(0, 0, pixmap.width(), pixmap.height())
    path.addRoundedRect(rect, radius, radius)
    painter.setClipPath(path)

    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return rounded

# Main credit window
class credits(QDialog):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        icon_path = os.path.join(assets_dir, "team.png")

        self.setWindowTitle("CREDITS")
        self.setFixedSize(600, 350)
        self.setWindowIcon(QIcon(icon_path))
        self.people()

    # Setting the images and credits
    def people(self):
        main_layout = QVBoxLayout()

        self.title = QLabel("Meet the Team!", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-family:SF Pro Display;")
        self.title.setFixedHeight(50)
        self.title.setObjectName("title")

        thanks = QLabel("Thank You For Using our Program 😊")
        thanks.setStyleSheet("font-size:16px;"
                            "font-weight: bold;"
                            "font-family:SF Pro Display")        
        thanks.setFixedHeight(20)
        thanks.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(thanks)
        main_layout.addWidget(self.title)

        # Getting and displaying the data of team members
        current_dir = os.path.dirname(os.path.abspath(__file__))
        asset = os.path.join(current_dir, "Icon Images")
        shenoy = os.path.join(asset, "shenoy.jpg")
        surya = os.path.join(asset, "surya.jpeg")

        team_layout = QHBoxLayout()

        team_members = [
            (shenoy , "S.VENKATESH SHENOY", "Lead Developer", "E-Mail: v66201200@gmail.com"),
            (surya, "SURYANAND A.", "UI Designer & Data Collector", 'E-Mail: asuryanand3@gmail.com')
        ]

        for photo_path, name, role, email in team_members:
            card_layout = QVBoxLayout()
            image_label = QLabel()
            pixmap = QPixmap(photo_path)

            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    120, 
                    120, Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )

                rounded_pixmap = round(scaled_pixmap, radius = 16)
                image_label.setPixmap(rounded_pixmap)

            else:
                image_label.setText("[Image Missing]")

            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            name_label = QLabel(name)
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            name_label.setStyleSheet("font-family:SF Pro Display")
            name_label.setObjectName("name_label")

            role_label = QLabel(role)
            role_label.setStyleSheet("font-family:SF Pro Display")
            role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            role_label.setObjectName("role_label")
            
            email = QLabel(email)
            email.setStyleSheet("font-family:SF Pro Display")
            email.setAlignment(Qt.AlignmentFlag.AlignCenter)
            email.setObjectName("email")

            card_layout.addWidget(image_label)
            card_layout.addWidget(name_label)
            card_layout.addWidget(role_label)
            card_layout.addWidget(email)

            team_layout.addLayout(card_layout)

        main_layout.addLayout(team_layout)
        self.setLayout(main_layout)