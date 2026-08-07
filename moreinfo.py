#Laptop details window styled to match the supplied dark-blue reference

from __future__ import annotations
import os
import html
import re
import sys
from pathlib import Path
from typing import Any

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPainterPath, QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QVBoxLayout, QWidget


FIELDS = ("model", "ram", "storage", "brand", "year", "cpu", "os", "last_os", "price")
LABELS = {
    "model": "Model", "ram": "RAM", "storage": "Storage", "brand": "Brand",
    "year": "Year", "cpu": "CPU", "os": "OS", "last_os": "Last OS", "price": "Price",
}
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".bmp")


def rounded_pixmap(pixmap: QPixmap, radius: int = 12) -> QPixmap:
    # Return a rounded-corner copy of an image
    result = QPixmap(pixmap.size())
    result.fill(Qt.GlobalColor.transparent)
    painter = QPainter(result)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    clip = QPainterPath()
    clip.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
    painter.setClipPath(clip)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
    return result


def filename_key(value: str) -> str:
    # Compare filenames without making spaces, hyphens, or case significant
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


class more_info(QMainWindow):
    #A dark themed laptop information window

    def __init__(self, laptop_data: Any = None) -> None:
        super().__init__()
        self.laptop_data = laptop_data
        self.details = self._normalise_data(laptop_data)
        self.project_dir = Path(__file__).resolve().parent
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "Icon Images")
        icon_path = os.path.join(assets_dir, "info_icon.png")

        self.setWindowTitle("Details")
        self.resize(880, 690)
        self.setWindowIcon(QIcon(icon_path))
        self.setMinimumSize(700, 520)
        self._build_ui()

    @staticmethod
    def _normalise_data(data: Any) -> dict[str, str]:
        #Turn list- or dictionary-shaped data into one predictable mapping
        details = {field: "" for field in FIELDS}

        if isinstance(data, dict):
            cleaned = {str(key).strip().casefold(): value for key, value in data.items()}
            aliases = {"last_os": ("last_os", "last os", "lastos", "last operating system")}
            for field in FIELDS:
                keys = aliases.get(field, (field,))
                value = next((cleaned[key] for key in keys if key in cleaned), "")
                details[field] = "" if value is None else str(value).strip()

        elif isinstance(data, (list, tuple)):
            for index, field in enumerate(FIELDS):
                if index < len(data) and data[index] is not None:
                    details[field] = str(data[index]).strip()

        return details

    def _build_ui(self) -> None:
        root = QWidget()
        root.setObjectName("root")
        layout = QVBoxLayout(root)
        layout.setContentsMargins(22, 24, 22, 22)
        layout.setSpacing(18)

        # The image area deliberately has no border, like the reference window.
        self.image_label = QLabel()
        self.image_label.setObjectName("image")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumHeight(290)
        self.image_label.setWordWrap(True)
        self._load_image()
        layout.addWidget(self.image_label, 1)

        details_card = QFrame()
        details_card.setObjectName("detailsCard")
        details_card.setMinimumHeight(306)
        card_layout = QVBoxLayout(details_card)
        card_layout.setContentsMargins(18, 18, 18, 20)
        card_layout.setSpacing(14)

        heading = QLabel(self.details["model"] or "Laptop details")
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setWordWrap(True)
        card_layout.addWidget(heading)

        specification_label = QLabel(self._specification_html())
        specification_label.setObjectName("specifications")
        specification_label.setTextFormat(Qt.TextFormat.RichText)
        specification_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        specification_label.setWordWrap(True)
        specification_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        card_layout.addWidget(specification_label, 1)
        layout.addWidget(details_card)

        self.setCentralWidget(root)
        self.setStyleSheet(
            """
            QMainWindow { background-color: #0e182d; }
            QWidget#root { background-color: #0e182d; }
            QLabel#image { color: #f4f6fa; font-size: 14px; }
            QFrame#detailsCard {
                background-color: rgba(74, 67, 91, 105);
                border: none;
                border-radius: 12px;
            }
            QLabel#heading {
                color: #ffffff;
                font-family: "Segoe UI";
                font-size: 23px;
                font-weight: 700;
            }
            QLabel#specifications {
                color: #f4f6fa;
                font-family: "Segoe UI";
                font-size: 17px;
                line-height: 1.25;
            }
        """)

    def _image_folder(self) -> Path:
        return self.project_dir / "Computer Images"

    def _find_image(self) -> Path | None:
        #Locate an image with exact matching first, then a forgiving match
        model = self.details["model"]
        folder = self._image_folder()
        if not model or not folder.is_dir():
            return None

        for extension in IMAGE_EXTENSIONS:
            candidate = folder / f"{model}{extension}"
            if candidate.is_file():
                return candidate

        desired_key = filename_key(model)
        for candidate in folder.iterdir():
            if candidate.is_file() and candidate.suffix.casefold() in IMAGE_EXTENSIONS:
                if filename_key(candidate.stem) == desired_key:
                    return candidate
        return None

    def _load_image(self) -> None:
        #Load the image, leaving a clear message in the same position if it fails
        image_path = self._find_image()
        model = self.details["model"]

        print("\n========== IMAGE DEBUG ==========")
        print("Image folder:", self._image_folder())
        print("Model name:  ", repr(model))
        print("Image path:  ", image_path or "not found")

        if image_path is None:
            self.image_label.setText("Image not found")
            return

        pixmap = QPixmap(str(image_path))
        print("Pixmap null: ", pixmap.isNull())
        if pixmap.isNull():
            self.image_label.setText("Image could not be read")
            return

        scaled = pixmap.scaled(
            250,
            250,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.image_label.setPixmap(rounded_pixmap(scaled))

    def _specification_html(self) -> str:
        rows = []
        for field in FIELDS:
            value = html.escape(self.details[field]) or "Not available"
            rows.append(f"<b>{LABELS[field]}:</b> {value}")
        return "<br>".join(rows)


def main() -> None:
    app = QApplication(sys.argv)
    sample_data = [
        "MacBook M4 Pro", "16 GB", "512 GB SSD", "Apple", "2025",
        "Apple M4 4.4 GHz", "macOS 15.1 Sequoia", "macOS 15 Sequoia", "169900",
    ]
    window = more_info(sample_data)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()