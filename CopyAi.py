import sys
import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QCheckBox, QFrame
)
from PyQt6.QtCore import Qt

class CopyAI(QWidget):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.init_ui()
        self.apply_theme()

    def init_ui(self):
        self.setWindowTitle("CopyAI - Professional Text Cleaner")
        self.resize(1100, 700)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        # Header Section
        header = QHBoxLayout()
        self.title_label = QLabel("CopyAI Engine")
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.theme_btn = QPushButton("Toggle Theme")
        self.theme_btn.setFixedWidth(120)
        self.theme_btn.clicked.connect(self.toggle_theme)
        
        header.addWidget(self.title_label)
        header.addStretch()
        header.addWidget(self.theme_btn)

        # Configuration Section
        config_layout = QHBoxLayout()
        self.keep_para = QCheckBox("Preserve Paragraphs")
        self.keep_para.setChecked(True)
        self.auto_copy = QCheckBox("Auto-Copy on Clean")
        self.auto_copy.setChecked(True)
        
        config_layout.addWidget(self.keep_para)
        config_layout.addWidget(self.auto_copy)
        config_layout.addStretch()

        # Text Area Section
        text_container = QHBoxLayout()
        
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Paste your AI-generated text here...")
        
        self.output_box = QTextEdit()
        self.output_box.setPlaceholderText("Cleaned professional text will appear here...")
        self.output_box.setReadOnly(True)

        text_container.addWidget(self.input_box)
        text_container.addWidget(self.output_box)

        # Action Buttons
        button_layout = QHBoxLayout()
        
        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_fields)
        self.clear_btn.setFixedWidth(100)
        
        self.clean_btn = QPushButton("Clean & Process Text")
        self.clean_btn.setFixedHeight(40)
        self.clean_btn.clicked.connect(self.process_text)
        
        self.copy_btn = QPushButton("Copy Result")
        self.copy_btn.setFixedHeight(40)
        self.copy_btn.clicked.connect(self.copy_to_clipboard)

        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.clean_btn)
        button_layout.addWidget(self.copy_btn)

        # Assembly
        layout.addLayout(header)
        layout.addWidget(self.create_line())
        layout.addLayout(config_layout)
        layout.addLayout(text_container)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

    def create_line(self): # Baris ini harus sejajar dengan def fungsi lainnya
            line = QFrame()
            line.setFrameShape(QFrame.Shape.HLine)
            line.setFrameShadow(QFrame.Shadow.Sunken)
            return line

    def process_text(self):
        raw_text = self.input_box.toPlainText()
        if not raw_text.strip():
            return

        # 1. Remove Markdown Artefacts (Bold, Italic, Strikethrough)
        text = re.sub(r'[*_~#]', '', raw_text)
        
        # 2. Clean specific AI bullet points but keep indentation sense
        text = re.sub(r'^[ \t]*[•\-\+\*][ \t]+', ' ', text, flags=re.MULTILINE)
        
        # 3. Handle Newlines
        if self.keep_para.isChecked():
            # Keep double newlines (paragraphs), but collapse multiple spaces
            paragraphs = text.split('\n\n')
            cleaned_paras = []
            for p in paragraphs:
                p_clean = re.sub(r'\s+', ' ', p).strip()
                cleaned_paras.append(p_clean)
            text = '\n\n'.join(cleaned_paras)
        else:
            # Flatten everything
            text = re.sub(r'\s+', ' ', text).strip()

        # 4. Final Punctuation Fix
        text = re.sub(r'\s+([,.!?])', r'\1', text)
        
        self.output_box.setPlainText(text)
        
        if self.auto_copy.isChecked():
            self.copy_to_clipboard()

    def copy_to_clipboard(self):
        QApplication.clipboard().setText(self.output_box.toPlainText())

    def clear_fields(self):
        self.input_box.clear()
        self.output_box.clear()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QWidget { background-color: #1a1a1a; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }
                QTextEdit { background-color: #2d2d2d; border: 1px solid #3d3d3d; border-radius: 6px; padding: 10px; font-size: 14px; }
                QPushButton { background-color: #3d5afe; color: white; border-radius: 6px; padding: 5px 15px; font-weight: bold; }
                QPushButton:hover { background-color: #536dfe; }
                QCheckBox { spacing: 8px; }
            """)
        else:
            self.setStyleSheet("""
                QWidget { background-color: #f5f5f7; color: #1d1d1f; font-family: 'Segoe UI', sans-serif; }
                QTextEdit { background-color: #ffffff; border: 1px solid #d2d2d7; border-radius: 6px; padding: 10px; font-size: 14px; }
                QPushButton { background-color: #000000; color: #ffffff; border-radius: 6px; padding: 5px 15px; font-weight: bold; }
                QPushButton:hover { background-color: #333333; }
                QCheckBox { spacing: 8px; }
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CopyAI()
    window.show()
    sys.exit(app.exec())