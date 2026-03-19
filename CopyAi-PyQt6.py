import sys
import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel
)
from PyQt6.QtCore import Qt


class CopyAI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CopyAI - Text Cleaner")
        self.resize(1000, 600)

        self.dark_mode = False

        self.init_ui()
        self.apply_light_theme()

    # ================= UI =================
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # HEADER
        header_layout = QHBoxLayout()

        self.title = QLabel("CopyAI Text Cleaner")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.theme_btn = QPushButton("Dark")
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.theme_btn.setFixedWidth(120)

        header_layout.addWidget(self.title)
        header_layout.addStretch()
        header_layout.addWidget(self.theme_btn)

        # TEXT AREA
        text_layout = QHBoxLayout()

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Input text here...")

        self.output_box = QTextEdit()
        self.output_box.setPlaceholderText("Clean result...")
        self.output_box.setReadOnly(True)

        text_layout.addWidget(self.input_box)
        text_layout.addWidget(self.output_box)

        # BUTTON (KANAN)
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.clean_btn = QPushButton("Clean Text")
        self.clean_btn.clicked.connect(self.clean_text)

        self.copy_btn = QPushButton("Copy")
        self.copy_btn.clicked.connect(self.copy_text)

        button_layout.addWidget(self.clean_btn)
        button_layout.addWidget(self.copy_btn)

        # ADD ALL
        main_layout.addLayout(header_layout)
        main_layout.addLayout(text_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    # ================= LOGIC =================
    def clean_text(self):
        text = self.input_box.toPlainText()

        text = re.sub(r'[-–—]', ' ', text)
        text = re.sub(r'[•*#]', '', text)
        text = re.sub(r'\s+([,.!?])', r'\1', text)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)

        text = text.strip()

        self.output_box.setPlainText(text)

    def copy_text(self):
        result = self.output_box.toPlainText()
        QApplication.clipboard().setText(result)

    # ================= THEME =================
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.apply_dark_theme()
            self.theme_btn.setText("Light")
        else:
            self.apply_light_theme()
            self.theme_btn.setText("Dark")

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                color: #000000;
            }

            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 8px;
            }

            QPushButton {
                background-color: #121211;
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 8px 16px;
            }

            QPushButton:hover {
                background-color: #4338ca;  /* sedikit lebih gelap */
            }

            QPushButton:pressed {
                background-color: #3730a3;  /* lebih dalam, bukan ungu beda tone */
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121214;
                color: #ffffff;
            }

            QTextEdit {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 10px;
                padding: 8px;
                color: white;
            }

            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 8px 16px;
            }

            QPushButton:hover {
                background-color: #4f46e5;
            }
        """)


# ================= RUN =================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CopyAI()
    window.show()
    sys.exit(app.exec())