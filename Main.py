import sys
from PyQt6.QtWidgets import QApplication, QWidget,QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

class loginWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('loginWindow.ui', self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Disable the default title bar
        #self.output_button.clicked.connect(self.close)
        self.createbutton.clicked.connect(self.create)
        self.loginbutton.clicked.connect(self.login)
        self.output_button.clicked.connect(self.back)

    def back(self):
        self.back_ = mainWindow()
        self.back_.show()
        self.close()
    
    def login(self):
            QMessageBox.information(self, "نجاح", f" تم التسجيل بنجاح")

    def create(self):
        self.create_ = createAccount()
        self.create_.show()
        self.close()

class createAccount(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('CreateAcountWindow.ui', self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Disable the default title bar
        #self.output_button.clicked.connect(self.close)
        self.loginbutton.clicked.connect(self.login)
        self.createbutton.clicked.connect(self.create)
        self.output_button.clicked.connect(self.back)

    def back(self):
        self.back_ = mainWindow()
        self.back_.show()
        self.close()

    def create(self):
            QMessageBox.information(self, "نجاح", f" تم انشاء الحساب بنجاح")

    def login(self):
        self.log = loginWindow()
        self.log.show()
        self.close()


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('MainWindow.ui', self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Disable the default title bar
        self.login_button.clicked.connect(self.login)
        self.create_button.clicked.connect(self.create)
        self.output_button.clicked.connect(self.close)


    def create(self):
        self.create_ = createAccount()
        self.create_.show()
        self.close()

    def login(self):
        self.log = loginWindow()
        self.log.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())