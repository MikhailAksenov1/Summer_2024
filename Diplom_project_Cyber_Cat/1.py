from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QMessageBox, QGridLayout, \
    QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QPixmap, QBrush
import json
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()

    def set_background_image(self, image_path):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_width = screen_geometry.width()
        window_height = screen_geometry.height()

        # Загрузка изображения
        image = QPixmap(image_path).scaled(window_width, window_height, Qt.AspectRatioMode.IgnoreAspectRatio)

        # Создание палитры
        palette = QPalette()
        brush = QBrush(image)
        palette.setBrush(QPalette.ColorRole.Window, brush)

        # Установка палитры в качестве фона
        self.setPalette(palette)

    def init_window(self):
        self.setWindowTitle("Config Generation Cyber_Cat ")

        # Получение размеров экрана
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_width = screen_geometry.width()
        window_height = screen_geometry.height()
        self.setGeometry(0, 0, window_width, window_height)  # Установка геометрии окна на весь экран

        # Установка фона с помощью QPalette и QBrush
        self.set_background_image("cat-cyberpunk.jpg")

        layout = QGridLayout()
        self.setLayout(layout)

        # Настройка стилей для текстовых полей и меток
        font_label = QFont("Arial", 18, QFont.Weight.Bold)
        font_text = QFont("Arial", 20)
        font_button = QFont("Arial", 16, QFont.Weight.Bold)

        # Настройка стилей для текстовых полей и меток
        self.setStyleSheet("""
                    QLabel, QLineEdit, QTextEdit, QComboBox {
                        color: #E0E0E0;
                        font-family: Arial;
                    }
                    QLineEdit {
                        background-color: rgba(0, 0, 0, 0.3);
                        border: 1px solid #00BFFF;
                        color: #E0E0E0;
                        padding: 5px;
                    }
                    QTextEdit {
                        background-color: rgba(0, 0, 0, 0.3);
                        border: 1px solid #00BFFF;
                        color: #E0E0E0;
                        padding: 5px;
                    }
                    QComboBox {
                        background-color: rgba(0, 0, 0, 0.3);
                        border: 1px solid #00BFFF;
                        color: #E0E0E0;
                        padding: 5px;
                    }
                    QComboBox QAbstractItemView {
                        background-color: rgba(0, 0, 0, 0.9);
                        color: #E0E0E0;
                        selection-background-color: #00BFFF;
                        padding: 5px;
                    }
                    QPushButton {
                        background-color: rgba(0, 0, 0, 0.3);
                        border: 1px solid #00BFFF;
                        color: #E0E0E0;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: rgba(0, 0, 0, 0.5);
                    }
                    QMessageBox {
                        color: #000000;
                        background-color: #FFFFFF;
                    }
                """)

        # Продукт
        product_label = QLabel("Продукт:")
        product_label.setFont(font_label)
        self.product_combobox = QComboBox()
        self.product_combobox.setEditable(True)  # Выпадающий список редактируемый
        self.product_combobox.addItems(
            ["Kaspersky Anti-Virus", "Kaspersky Secure Connection", "Kaspersky Password Manager"])
        self.product_combobox.setFont(font_text)
        self.product_combobox.setFixedWidth(500)
        layout.addWidget(product_label, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.product_combobox, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.product_combobox.activated.connect(self.combo_change)

        # Версия продукта
        poversion_label = QLabel("Версия ПО:")
        poversion_label.setFont(font_label)
        self.poversion_entry = QComboBox()
        self.poversion_entry.addItems(['v1', 'v2', 'v3', 'v4', 'v5'])
        self.poversion_entry.setFont(font_text)
        self.poversion_entry.setFixedWidth(350)
        layout.addWidget(poversion_label, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.poversion_entry, 2, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        build_label = QLabel("№ Сборки:")
        build_label.setFont(font_label)
        self.build_entry = QLineEdit()
        self.build_entry.setFont(font_text)
        self.build_entry.setFixedWidth(350)
        layout.addWidget(build_label, 3, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.build_entry, 3, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        config_label = QLabel("№ Сборки с тестами:")
        config_label.setFont(font_label)
        self.config_entry = QLineEdit()
        self.config_entry.setFont(font_text)
        self.config_entry.setFixedWidth(350)
        layout.addWidget(config_label, 4, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.config_entry, 4, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        checkbox_label = QLabel('FireFox')
        checkbox_label.setFont(font_label)
        self.firefox = QCheckBox()
        self.firefox.setCheckState(Qt.CheckState.Checked)
        self.firefox.stateChanged.connect(self.show_state)
        layout.addWidget(checkbox_label, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.firefox, 1, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        checkbox_label = QLabel('GoogleChrome')
        checkbox_label.setFont(font_label)
        self.gh = QCheckBox()
        self.gh.setCheckState(Qt.CheckState.Checked)
        self.gh.stateChanged.connect(self.show_state)
        layout.addWidget(checkbox_label, 2, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.gh, 2, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        checkbox_label = QLabel('Safari')
        checkbox_label.setFont(font_label)
        self.safari = QCheckBox()
        self.safari.setCheckState(Qt.CheckState.Checked)
        self.safari.stateChanged.connect(self.show_state)
        layout.addWidget(checkbox_label, 3, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.safari, 3, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        checkbox_label = QLabel('Yandex')
        checkbox_label.setFont(font_label)
        self.yandex = QCheckBox()
        self.yandex.setCheckState(Qt.CheckState.Checked)
        self.yandex.stateChanged.connect(self.show_state)
        layout.addWidget(checkbox_label, 4, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.yandex, 4, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        language_label = QLabel("Системный язык:")
        language_label.setFont(font_label)
        self.language_combobox = QComboBox()
        self.language_combobox.setEditable(True)  # Выпадающий список редактируемый
        self.language_combobox.addItems(
            ["en", "ru", "ar", "ee", "es"])
        self.language_combobox.setFont(font_text)
        self.language_combobox.setFixedWidth(100)
        layout.addWidget(language_label, 5, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.language_combobox, 5, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        reg_label = QLabel("Регион:")
        reg_label.setFont(font_label)
        self.reg_combobox = QComboBox()
        self.reg_combobox.setEditable(True)  # Выпадающий список редактируемый
        self.reg_combobox.addItems(
            ["en_US", "ru_RU", "ar_AE", "ee_EE", "es_MX"])
        self.reg_combobox.setFont(font_text)
        self.reg_combobox.setFixedWidth(200)
        layout.addWidget(reg_label, 6, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.reg_combobox, 6, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        # Кнопка "Сохранить"
        save_button = QPushButton("Сохранить")
        save_button.setFont(font_button)
        save_button.clicked.connect(self.save_data)
        layout.addWidget(save_button, 7, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)

    def save_data(self):
        product_selection = self.product_combobox.currentText()
        poversion_text = self.poversion_entry.currentText()
        configuration_text = self.config_entry.text()
        test_build = self.build_entry.text()
        firefox = self.firefox.isChecked()
        google_chrome = self.gh.isChecked()
        safari = self.safari.isChecked()
        yandex = self.yandex.isChecked()
        system_language = self.language_combobox.currentText()
        region = self.reg_combobox.currentText()

        filename = "config.json"
        example = {'Product': product_selection, 'ProductVersion': poversion_text, 'BuildNumber': configuration_text,
                   'TestBuild': test_build, 'FireFox': firefox, 'GoogleChrome': google_chrome, 'safari': safari,
                   'Yandex': yandex, 'SystemLanguage': system_language, 'Region': region}
        with open(filename, 'w') as f:
            json.dump(example, f)

        # Установка стиля для QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Успех")
        msg.setText("Данные успешно сохранены в файл 'config.json'")
        msg.setStyleSheet("QLabel { color: black; }")  # Установка черного цвета для текста
        msg.exec()

    def combo_change(self, newitem):
        combo = self.sender()

        if self.product_combobox.currentText() == "Kaspersky Anti-Virus":
            self.poversion_entry.clear()
            self.poversion_entry.addItems(['v1', 'v2', 'v3', 'v4', 'v5'])
        elif self.product_combobox.currentText() == "Kaspersky Secure Connection":
            self.poversion_entry.clear()
            self.poversion_entry.addItems(['v11', 'v22', 'v33', 'v44', 'v55'])
        elif self.product_combobox.currentText() == "Kaspersky Password Manager":
            self.poversion_entry.clear()
            self.poversion_entry.addItems(['v111', 'v222', 'v333', 'v444', 'v555'])
        combo.setProperty("lastitem", newitem)

    def show_state(self, s):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
